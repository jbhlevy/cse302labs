	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $40, %rsp
	movq $10, -8(%rbp)
	movq $20, -8(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	pushq %rdi
	pushq %rax
	movq -16(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq -8(%rbp), %r11
	movq %r11, -24(%rbp)
	movq $1, -32(%rbp)
	movq -24(%rbp), %r11
	addq -32(%rbp), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	pushq %rdi
	pushq %rax
	movq -40(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
