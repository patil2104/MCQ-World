org 100h

jmp start

;	setting varsnum1 dw 1

num2 dw 1

start:

  

mov 	cx, 20 ;	counter (for the Fibonacci function)

mov 	ax, num1

;	print twice to get "1 1 " at the start of the run     

Fibonacci:

    mov 	bx, num1

    add 	bx, num2

    mov 	dx, bx

    mov 	bx, num1

    mov 	num2, bx

    mov 	bx, dx

    mov 	num1, bx

    ;	this part is for printing ax you dont have to mov dx into ax...

    ;			dx = ax = current fibonacci number

    ;mov ax, dx

    ;	use print function!!

loop Fibonacci  ; loop for 20 times

mov ah, 0

int 16h

ret
