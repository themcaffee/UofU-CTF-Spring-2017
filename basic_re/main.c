#include<stdio.h>

#pragma clang diagnostic push
#pragma ide diagnostic ignored "OCDFAInspection"
void main() {
    const char FLAG[] = "REPLACEMEWITHFLAG";
    printf("The rich need me. The poor have me. Don't eat me or you'll die! What am I?");
    char buf[10];
    if(fgets(buf, sizeof buf, stdin) != NULL) {
        if(1) {
            printf("Wrong!");
        } else {
            printf("The flag is %s", FLAG);
        }
    }
}

#pragma clang diagnostic pop