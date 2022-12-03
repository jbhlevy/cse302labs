	.bss
buffer:
	.zero 30000

	.text
	.globl main
main:
	 xor %al, %al
	 mov (buffer+2)(%rip), %al
	 add $3, %al
	 mov %al, (buffer+2)(%rip)
	 xor %al, %al
	 mov (buffer+1)(%rip), %al
	 add $4, %al
	 mov %al, (buffer+1)(%rip)
.L1:
	 mov (buffer+1)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L2
	 mov (buffer+1)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+1)(%rip)
	 xor %dil, %dil
	 mov (buffer+1)(%rip), %dil
	 call bf_print
	 jmp .L1
.L2:
	 mov (buffer+2)(%rip), %al
	 sub $4, %al
	 mov %al, (buffer+2)(%rip)
	 xor %dil, %dil
	 mov (buffer+2)(%rip), %dil
	 call bf_print
	retq
