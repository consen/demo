;
; print_string function
;
print_string:
  pusha
  mov ah, 0x0e

loop:
  mov al, [bx]
  cmp al, 0
  je exit
  int 0x10
  add bx, 1
  jmp loop

exit:
  popa
  ret
