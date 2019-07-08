## /tests
Hmm.. there contains some test disk images..<br>
How to compile and get ISO:

```
$ yasm -f bin -o hello.bin hello.asm
$ dd if=/dev/zero of=hello.iso bs=1024 count=1440
$ dd if=hello.bin of=hello.iso conv=notrunc
```
