	.bss
buffer:
	.zero 30000
	.text
	.globl main
main:
	 mov 3(%rip), %al
	 add $2, %al
	 mov %al, 3(%rip)
	 mov 0(%rip), %al
	 add $2, %al
	 mov %al, 0(%rip)
	 mov 0(%rip), %al
	 call bf_print
	 mov 1(%rip), %al
	 sub $1, %al
	 mov %al, 1(%rip)
	 mov 3(%rip), %al
	 add $2, %al
	 mov %al, 3(%rip)
	 mov 2(%rip), %al
	 call bf_print
	 mov 2(%rip), %al
	 add $0, %al
	 mov %al, 2(%rip)
