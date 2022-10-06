	.section .rodata
.lprintfmt:
	.string "%ld\n"
	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $488, %rsp
	movq $10, -8(%rbp)
	movq $20, -16(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -24(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -32(%rbp)
	movq -24(%rbp), %r11
	subq -32(%rbp), %r11
	movq %r11, -24(%rbp)
	movq $0, %r11
	cmpq %r11, -24(%rbp)
	je .L0
	jmp .L1
	.L0:
	movq $0, -40(%rbp)
	pushq %rdi
	pushq %rax
	movq -40(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L2
	.L1:
	.L2:
	movq -8(%rbp), %r11
	movq %r11, -48(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -56(%rbp)
	movq -48(%rbp), %r11
	subq -56(%rbp), %r11
	movq %r11, -48(%rbp)
	movq $0, %r11
	cmpq %r11, -48(%rbp)
	jne .L3
	jmp .L4
	.L3:
	movq $1, -64(%rbp)
	pushq %rdi
	pushq %rax
	movq -64(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L5
	.L4:
	.L5:
	movq -8(%rbp), %r11
	movq %r11, -72(%rbp)
	movq $2, -80(%rbp)
	movq -72(%rbp), %rax
	imulq -80(%rbp)
	movq %rax, -88(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -96(%rbp)
	movq -88(%rbp), %r11
	subq -96(%rbp), %r11
	movq %r11, -88(%rbp)
	movq $0, %r11
	cmpq %r11, -88(%rbp)
	je .L6
	jmp .L7
	.L6:
	movq $2, -104(%rbp)
	pushq %rdi
	pushq %rax
	movq -104(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L8
	.L7:
	.L8:
	jmp .L9
	.L12:
	jmp .L9
	.L9:
	movq $3, -112(%rbp)
	pushq %rdi
	pushq %rax
	movq -112(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L11
	.L10:
	.L11:
	movq $1, -120(%rbp)
	movq $1, -128(%rbp)
	movq -120(%rbp), %r11
	subq -128(%rbp), %r11
	movq %r11, -120(%rbp)
	movq $0, %r11
	cmpq %r11, -120(%rbp)
	je .L13
	jmp .L16
	.L16:
	jmp .L14
	.L13:
	movq $4, -136(%rbp)
	pushq %rdi
	pushq %rax
	movq -136(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L15
	.L14:
	.L15:
	movq -8(%rbp), %r11
	movq %r11, -144(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -152(%rbp)
	movq -144(%rbp), %r11
	subq -152(%rbp), %r11
	movq %r11, -144(%rbp)
	movq $0, %r11
	cmpq %r11, -144(%rbp)
	jl .L17
	jmp .L18
	.L17:
	movq $5, -160(%rbp)
	pushq %rdi
	pushq %rax
	movq -160(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L19
	.L18:
	.L19:
	movq -8(%rbp), %r11
	movq %r11, -168(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -176(%rbp)
	movq -168(%rbp), %r11
	subq -176(%rbp), %r11
	movq %r11, -168(%rbp)
	movq $0, %r11
	cmpq %r11, -168(%rbp)
	jg .L20
	jmp .L21
	.L20:
	movq $6, -184(%rbp)
	pushq %rdi
	pushq %rax
	movq -184(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L22
	.L21:
	.L22:
	movq -8(%rbp), %r11
	movq %r11, -192(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -200(%rbp)
	movq -192(%rbp), %r11
	subq -200(%rbp), %r11
	movq %r11, -192(%rbp)
	movq $0, %r11
	cmpq %r11, -192(%rbp)
	jl .L23
	jmp .L24
	.L23:
	movq $7, -208(%rbp)
	pushq %rdi
	pushq %rax
	movq -208(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L25
	.L24:
	.L25:
	movq -8(%rbp), %r11
	movq %r11, -216(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -224(%rbp)
	movq -216(%rbp), %r11
	subq -224(%rbp), %r11
	movq %r11, -216(%rbp)
	movq $0, %r11
	cmpq %r11, -216(%rbp)
	jle .L26
	jmp .L27
	.L26:
	movq $8, -232(%rbp)
	pushq %rdi
	pushq %rax
	movq -232(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L28
	.L27:
	.L28:
	movq -8(%rbp), %r11
	movq %r11, -240(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -248(%rbp)
	movq -240(%rbp), %r11
	subq -248(%rbp), %r11
	movq %r11, -240(%rbp)
	movq $0, %r11
	cmpq %r11, -240(%rbp)
	jge .L29
	jmp .L30
	.L29:
	movq $9, -256(%rbp)
	pushq %rdi
	pushq %rax
	movq -256(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L31
	.L30:
	.L31:
	movq -8(%rbp), %r11
	movq %r11, -264(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -272(%rbp)
	movq -264(%rbp), %r11
	subq -272(%rbp), %r11
	movq %r11, -264(%rbp)
	movq $0, %r11
	cmpq %r11, -264(%rbp)
	jle .L32
	jmp .L33
	.L32:
	movq $10, -280(%rbp)
	pushq %rdi
	pushq %rax
	movq -280(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L34
	.L33:
	.L34:
	movq -8(%rbp), %r11
	movq %r11, -288(%rbp)
	movq -16(%rbp), %r11
	movq %r11, -296(%rbp)
	movq -288(%rbp), %r11
	subq -296(%rbp), %r11
	movq %r11, -288(%rbp)
	movq $0, %r11
	cmpq %r11, -288(%rbp)
	jle .L35
	jmp .L38
	.L38:
	movq -16(%rbp), %r11
	movq %r11, -304(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -312(%rbp)
	movq -304(%rbp), %r11
	subq -312(%rbp), %r11
	movq %r11, -304(%rbp)
	movq $0, %r11
	cmpq %r11, -304(%rbp)
	jle .L35
	jmp .L36
	.L35:
	movq $11, -320(%rbp)
	pushq %rdi
	pushq %rax
	movq -320(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L37
	.L36:
	.L37:
	movq -8(%rbp), %r11
	movq %r11, -328(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -336(%rbp)
	movq -328(%rbp), %r11
	subq -336(%rbp), %r11
	movq %r11, -328(%rbp)
	movq $0, %r11
	cmpq %r11, -328(%rbp)
	je .L39
	jmp .L40
	.L39:
	movq $12, -344(%rbp)
	pushq %rdi
	pushq %rax
	movq -344(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L41
	.L40:
	.L41:
	movq $1, -352(%rbp)
	movq $1, -360(%rbp)
	movq -352(%rbp), %r11
	subq -360(%rbp), %r11
	movq %r11, -352(%rbp)
	movq $0, %r11
	cmpq %r11, -352(%rbp)
	je .L42
	jmp .L43
	.L42:
	movq $13, -368(%rbp)
	pushq %rdi
	pushq %rax
	movq -368(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L44
	.L43:
	.L44:
	movq $1, -376(%rbp)
	movq $0, -384(%rbp)
	movq -376(%rbp), %r11
	subq -384(%rbp), %r11
	movq %r11, -376(%rbp)
	movq $0, %r11
	cmpq %r11, -376(%rbp)
	je .L45
	jmp .L46
	.L45:
	movq $14, -392(%rbp)
	pushq %rdi
	pushq %rax
	movq -392(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L47
	.L46:
	.L47:
	movq $0, -400(%rbp)
	movq $0, -408(%rbp)
	movq -400(%rbp), %r11
	subq -408(%rbp), %r11
	movq %r11, -400(%rbp)
	movq $0, %r11
	cmpq %r11, -400(%rbp)
	je .L48
	jmp .L49
	.L48:
	movq $15, -416(%rbp)
	pushq %rdi
	pushq %rax
	movq -416(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L50
	.L49:
	.L50:
	movq $0, -424(%rbp)
	movq $1, -432(%rbp)
	movq -424(%rbp), %r11
	subq -432(%rbp), %r11
	movq %r11, -424(%rbp)
	movq $0, %r11
	cmpq %r11, -424(%rbp)
	je .L51
	jmp .L52
	.L51:
	movq $16, -440(%rbp)
	pushq %rdi
	pushq %rax
	movq -440(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L53
	.L52:
	.L53:
	movq -8(%rbp), %r11
	movq %r11, -448(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -456(%rbp)
	movq -448(%rbp), %r11
	subq -456(%rbp), %r11
	movq %r11, -448(%rbp)
	movq $0, %r11
	cmpq %r11, -448(%rbp)
	je .L55
	jmp .L54
	.L54:
	movq $17, -464(%rbp)
	pushq %rdi
	pushq %rax
	movq -464(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L56
	.L55:
	.L56:
	movq -8(%rbp), %r11
	movq %r11, -472(%rbp)
	movq -8(%rbp), %r11
	movq %r11, -480(%rbp)
	movq -472(%rbp), %r11
	subq -480(%rbp), %r11
	movq %r11, -472(%rbp)
	movq $0, %r11
	cmpq %r11, -472(%rbp)
	jne .L58
	jmp .L57
	.L57:
	movq $18, -488(%rbp)
	pushq %rdi
	pushq %rax
	movq -488(%rbp), %rdi
	callq bx_print_int
	popq %rax
	popq %rdi
	jmp .L59
	.L58:
	.L59:
	movq %rbp, %rsp
	popq %rbp
	xorq %rax, %rax
	retq
