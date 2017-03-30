# Binary Tweak

- build.sh : Build the event binaries
- lib/tweak.c : Included library file for event

- ./build_solution.sh : Builds the solution file
- lib_solution/tweaksolution.c : Example solution library that should be included

Solution:

Change LD_LOAD_LIBRARY_PATH environment variable to point to a new library file that reads the FLAG.txt file with the permissions gained from the program execution.
 
Environment: 

- FLAG.txt : Should be only be readable to binary_tweak_user, writable by root. 
- binary_tweak : Should be executable by anyone, writable by root.
- lib/libtweak : TODO
