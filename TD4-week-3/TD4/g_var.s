	.globl n
	.data
n:	.quad 0
	.globl i
	.data
i:	.quad 1
	.globl m
	.data
m:	.quad 1
	.globl b
	.data
b:	.quad True

	.globl @add3
	.text
@add3:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -24(%rbp), %r11
	movq %r11, -32(%rbp)
	movq -16(%rbp), %r11
	addq -32(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -48(%rbp), %r11
	movq %r11, -56(%rbp)
	movq -40(%rbp), %r11
	addq -56(%rbp), %r11
	movq %r11, -64(%rbp)
	movq %rbp, %rsp
	popq %rbp
	movq -64(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
