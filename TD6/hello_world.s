	.bss
buffer:
	.zero 30000

	.text
	.globl main
main:
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $8, %al
	 mov %al, (buffer+1)(%rip)
.L1:
	 mov (buffer+1)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L2
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $9, %al
	 mov %al, (buffer+0)(%rip)
	 mov (buffer+1)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+1)(%rip)
	 jmp .L1
.L2:
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $4, %al
	 mov %al, (buffer+1)(%rip)
.L3:
	 mov (buffer+1)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L4
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $7, %al
	 mov %al, (buffer+0)(%rip)
	 mov (buffer+1)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+1)(%rip)
	 jmp .L3
.L4:
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $7, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $3, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+2)(%rip), %al
	 add $6, %al
	 mov %al, (buffer+2)(%rip)
.L5:
	 mov (buffer+2)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L6
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $7, %al
	 mov %al, (buffer+1)(%rip)
	 mov (buffer+2)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+2)(%rip)
	 jmp .L5
.L6:
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $2, %al
	 mov %al, (buffer+1)(%rip)
	 xor %dil, %dil
	 mov (buffer+1)(%rip), %dil
	 call bf_print
	 mov (buffer+1)(%rip), %al
	 sub $12, %al
	 mov %al, (buffer+1)(%rip)
	 xor %dil, %dil
	 mov (buffer+1)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+2)(%rip), %al
	 add $6, %al
	 mov %al, (buffer+2)(%rip)
.L7:
	 mov (buffer+2)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L8
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $9, %al
	 mov %al, (buffer+1)(%rip)
	 mov (buffer+2)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+2)(%rip)
	 jmp .L7
.L8:
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+1)(%rip)
	 xor %dil, %dil
	 mov (buffer+1)(%rip), %dil
	 call bf_print
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+0)(%rip), %al
	 add $3, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 mov (buffer+0)(%rip), %al
	 sub $6, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 mov (buffer+0)(%rip), %al
	 sub $8, %al
	 mov %al, (buffer+0)(%rip)
	 xor %dil, %dil
	 mov (buffer+0)(%rip), %dil
	 call bf_print
	 xor %al, %al
	 mov (buffer+3)(%rip), %al
	 add $4, %al
	 mov %al, (buffer+3)(%rip)
.L9:
	 mov (buffer+3)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L10
	 xor %al, %al
	 mov (buffer+2)(%rip), %al
	 add $8, %al
	 mov %al, (buffer+2)(%rip)
	 mov (buffer+3)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+3)(%rip)
	 jmp .L9
.L10:
	 xor %al, %al
	 mov (buffer+2)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+2)(%rip)
	 xor %dil, %dil
	 mov (buffer+2)(%rip), %dil
	 call bf_print
	retq
