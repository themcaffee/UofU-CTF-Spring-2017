#include <stdio.h>
#include <string.h>

/**
 * Created by Mitch McAffee for U of U CTF 2017
 *
 * Solution: Overflow buf and inject shellcode to get a shell. Use the permissions of the executable to access
 * a file.
 */

// Change from 0 to 1 to enable printing the buffer location
#define EASY_MODE 0

// We really don't care about deprecated functions lol
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
void fillcup(void)
{
    char buf[150];
    gets(buf);
    printf("%s\n", buf);
    if(EASY_MODE) {
        printf("[+] buf %p\n", buf);
    }
}

int main(void)
{
    printf("Fill up my cup:\n");
    fillcup();
    printf("Thanks.\n");
    return 0;
}
#pragma clang diagnostic pop