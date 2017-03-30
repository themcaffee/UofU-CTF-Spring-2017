#include <stdio.h>
#include <unistd.h>

/**
 * Created by Mitch McAffee for U of U CTF 2017
 *
 * Solution: Replace the executed library file with a new one
 */

void display(char *i);

int main(void) {
    // Replace with uid and gid of non-root user that has access to flag file
    setuid(0);
    setgid(0);
    // Function from separate shared library
    display("You are now authenticated");
}
