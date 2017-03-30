# Cup Overflow

### Solution

Buffer overflow with executable stack. The sploit.py script will exploit the program
even if ASLR is turned on. This can take many tries, it took 323 on mine, so be patient.

```bash
./sploit.py
```

### Notes

- Easy Mode: There is a toggleable variable in main.c that if enabled prints out 
the buffer location. This would make things much easier on the participants.
- Turn on ASLR randomization
```bash
sudo sysctl -w kernel.randomize_va_space=1
```
- Turn off ASLR randomization
```bash
sudo sysctl -w kernel.randomize_va_space=0
```
