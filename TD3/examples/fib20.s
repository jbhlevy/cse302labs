	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $88, %rsp
	movq $20, -8(%rbp)
	movq $0, -16(%rbp)
	movq $1, -24(%rbp)
	movq $0, -32(%rbp)
	.L0:
	movq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	movq $0, -48(%rbp)
	movq -40(%rbp), %r11
	subq -48(%rbp), %r11
	movq %r11, -40(%rbp)
	movq $0, %r11
	cmpq %r11, -40(%rbp)
	jg .L1
	jmp .L2
	.L1:
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	movq $1, -64(%rbp)
	movq -56(%rbp), %r11
	subq -64(%rbp), %r11
	movq %r11, -8(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -72(%rbp)
	pushq %rdi
	pushq %rax
	movq -72(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq -16(%rbp), %r11
	movq %r11, -80(%rbp)
	movq -24(%rbp), %r11
	movq %r11, -88(%rbp)
	movq -80(%rbp), %r11
	addq -88(%rbp), %r11
	movq %r11, -32(%rbp)
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -32(%rbp), %r11
	movq %r11, -24(%rbp)
	jmp .L0
	.L2:
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
