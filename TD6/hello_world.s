	.bss
buffer:
	.zero 30000

	.text
	.globl main
main:
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 0)(%rip), %rax
	 addq $13, %rax
	 movq %rax, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 0)(%rip), %rax
	 addq $7, %rax
	 movq %rax, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 0)(%rip), %rax
	 addq $3, %rax
	 movq %rax, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 1)(%rip), %rax
	 addq $8, %rax
	 movq %rax, (buffer + 1)(%rip)
	 mov (buffer + 1)(%rip), %rax
	 call bf_print
	 mov (buffer + 1)(%rip), %al
	 sub $12, %al
	 mov %al, (buffer + 1)(%rip)
	 mov (buffer + 1)(%rip), %rax
	 call bf_print
	 movq (buffer + 1)(%rip), %rax
	 addq $7, %rax
	 movq %rax, (buffer + 1)(%rip)
	 mov (buffer + 1)(%rip), %rax
	 call bf_print
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 0)(%rip), %rax
	 addq $3, %rax
	 movq %rax, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 mov (buffer + 0)(%rip), %al
	 sub $6, %al
	 mov %al, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 mov (buffer + 0)(%rip), %al
	 sub $8, %al
	 mov %al, (buffer + 0)(%rip)
	 mov (buffer + 0)(%rip), %rax
	 call bf_print
	 movq (buffer + 2)(%rip), %rax
	 addq $5, %rax
	 movq %rax, (buffer + 2)(%rip)
	 mov (buffer + 2)(%rip), %rax
	 call bf_print
	 movq (buffer + 2)(%rip), %rax
	 addq $0, %rax
	 movq %rax, (buffer + 2)(%rip)
	retq
