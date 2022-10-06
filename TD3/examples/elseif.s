	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $208, %rsp
	movq $833779, -8(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	movq $2, -24(%rbp)
	movq -16(%rbp), %rax
	cqto
	idivq -24(%rbp)
	movq %rdx, -32(%rbp)
	movq $0, -40(%rbp)
	movq -32(%rbp), %r11
	subq -40(%rbp), %r11
	movq %r11, -32(%rbp)
	movq $0, %r11
	cmpq %r11, -32(%rbp)
	je .L0
	jmp .L1
	.L0:
	movq $2, -48(%rbp)
	pushq %rdi
	pushq %rax
	movq -48(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L2
	.L1:
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	movq $3, -64(%rbp)
	movq -56(%rbp), %rax
	cqto
	idivq -64(%rbp)
	movq %rdx, -72(%rbp)
	movq $0, -80(%rbp)
	movq -72(%rbp), %r11
	subq -80(%rbp), %r11
	movq %r11, -72(%rbp)
	movq $0, %r11
	cmpq %r11, -72(%rbp)
	je .L3
	jmp .L4
	.L3:
	movq $3, -88(%rbp)
	pushq %rdi
	pushq %rax
	movq -88(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L5
	.L4:
	movq -8(%rbp), %r11
	movq %r11, -96(%rbp)
	movq $5, -104(%rbp)
	movq -96(%rbp), %rax
	cqto
	idivq -104(%rbp)
	movq %rdx, -112(%rbp)
	movq $0, -120(%rbp)
	movq -112(%rbp), %r11
	subq -120(%rbp), %r11
	movq %r11, -112(%rbp)
	movq $0, %r11
	cmpq %r11, -112(%rbp)
	je .L6
	jmp .L7
	.L6:
	movq $5, -128(%rbp)
	pushq %rdi
	pushq %rax
	movq -128(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L8
	.L7:
	movq -8(%rbp), %r11
	movq %r11, -136(%rbp)
	movq $7, -144(%rbp)
	movq -136(%rbp), %rax
	cqto
	idivq -144(%rbp)
	movq %rdx, -152(%rbp)
	movq $0, -160(%rbp)
	movq -152(%rbp), %r11
	subq -160(%rbp), %r11
	movq %r11, -152(%rbp)
	movq $0, %r11
	cmpq %r11, -152(%rbp)
	je .L9
	jmp .L10
	.L9:
	movq $7, -168(%rbp)
	pushq %rdi
	pushq %rax
	movq -168(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L11
	.L10:
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	movq $11, -184(%rbp)
	movq -176(%rbp), %rax
	cqto
	idivq -184(%rbp)
	movq %rdx, -192(%rbp)
	movq $0, -200(%rbp)
	movq -192(%rbp), %r11
	subq -200(%rbp), %r11
	movq %r11, -192(%rbp)
	movq $0, %r11
	cmpq %r11, -192(%rbp)
	je .L12
	jmp .L13
	.L12:
	movq $11, -208(%rbp)
	pushq %rdi
	pushq %rax
	movq -208(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L14
	.L13:
	.L14:
	.L11:
	.L8:
	.L5:
	.L2:
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
