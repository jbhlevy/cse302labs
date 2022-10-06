	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $8, %rsp
	movq $42, -8(%rbp)
	pushq %rdi
	pushq %rax
	movq -8(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
