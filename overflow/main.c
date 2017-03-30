#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Created by Mitch McAffee for U of U CTF 2017
 *
 * Solution: Overflow the buf variable to replace the return address with that of success()
 */

// We really don't care about deprecated functions lol
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
bool checkpass(void)
{
    char buf[8];
    gets(buf);
    printf("Entered: %s\n", buf);
    // Always return false
    return false;
}

void success(void) {
    // Print out the flag
    FILE *fp;
    char buff[20];

    fp = fopen("./FLAG.txt", "r");
    fgets(buff, 20, (FILE*)fp);
    printf("You hacked the gibson! Here's the flag: %s\n", buff);
}

void failure(void) {
    printf("Nope!");
}

int main(void)
{
    printf("Enter the password:\n");
    if (checkpass()) {
        success();
    } else {
        failure();
    }
    return 0;
}
#pragma clang diagnostic pop