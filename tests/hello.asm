section .text
     use16
     org  0x7C00
start:
     mov  ax, cs
     mov  ds, ax

     mov  si, message
     cld
     mov  ah, 0x0E
     mov  bh, 0x00
puts_loop:
     lodsb
     test al, al
     jz   puts_loop_exit
     int  0x10        ; calling a BIOS function
     jmp  puts_loop
puts_loop_exit:
     jmp  $

message: ; helloworld in assembler :)
     db   'Hello World! (omg why this thing doing in flash burning script repo)', 0 :
finish:
     times 0x1FE-finish+start db 0
     db   0x55, 0xAA  ; bootsector signature
