	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $120, %rsp
	movq $10, -8(%rbp)
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
	movq $20, -32(%rbp)
	movq -24(%rbp), %r11
	addq -32(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	pushq %rdi
	pushq %rax
	movq -48(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq -40(%rbp), %r11
	movq %r11, -56(%rbp)
	movq $42, -64(%rbp)
	movq -56(%rbp), %rax
	imulq -64(%rbp)
	movq %rax, -72(%rbp)
	movq -72(%rbp), %r11
	movq %r11, -80(%rbp)
	pushq %rdi
	pushq %rax
	movq -80(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	movq -8(%rbp), %r11
	movq %r11, -88(%rbp)
	movq -40(%rbp), %r11
	movq %r11, -96(%rbp)
	movq -88(%rbp), %rax
	imulq -96(%rbp)
	movq %rax, -104(%rbp)
	movq -72(%rbp), %r11
	movq %r11, -112(%rbp)
	movq -104(%rbp), %r11
	subq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
