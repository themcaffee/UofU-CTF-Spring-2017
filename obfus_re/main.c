#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#pragma clang diagnostic push
#pragma ide diagnostic ignored "OCDFAInspection"
#define LENGTH 19
void main() {
    // Output from key ^ RANDOM
    char const obfuscated[LENGTH] = "\x1e\x01\x03\x07\x0b\x05\x09\x12\x00\x07\x02\x14\x0e\x04\x00\x0f\x1f\x0b\x02";
    // Random characters
    char const random[LENGTH] = "LDSKJFLEISJFKELISJE";
    char buf[LENGTH];
    char xor_buf[LENGTH];
    printf("Give me the password:\n");
    if(fgets(buf, sizeof buf, stdin) != NULL) {
        // Calculate user input xor
        for(int i=0; i<LENGTH; ++i) {
            xor_buf[i] = (char)(buf[i] ^ random[i]);
        }
        if(strcmp(xor_buf, obfuscated)) {
            printf("Wrong!");
        } else {
            printf("You found the key!");
        }
    }
}

#pragma clang diagnostic pop