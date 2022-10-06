	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq $1, -8(%rbp)
	movq $2, -16(%rbp)
	movq -8(%rbp), %r11
	addq -16(%rbp), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r11
	movq %r11, -32(%rbp)
	pushq %rdi
	pushq %rax
	movq -32(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
