	.globl x
	.data
x: .quad 0
	.globl y
	.data
y: .quad 6
	.globl z
	.data
z: .quad 12
	.globl a
	.data
a: .quad 1
	.globl b
	.data
b: .quad 0
	.globl c
	.data
c: .quad 1
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	callq subroutine1
	movq %rax, -8(%rbp)
movq a(%rip), %r11
movq %r11, -16(%rbp)
	movq -16(%rbp), %rdi
movq b(%rip), %r11
movq %r11, -24(%rbp)
	movq -24(%rbp), %rsi
movq x(%rip), %r11
movq %r11, -32(%rbp)
	movq -32(%rbp), %rdx
movq z(%rip), %r11
movq %r11, -40(%rbp)
	movq -40(%rbp), %rcx
	callq subroutine2
	movq %rax, -8(%rbp)
movq $0, -48(%rbp)
	callq fun1
	movq %rax, -48(%rbp)
movq $0, -56(%rbp)
movq c(%rip), %r11
movq %r11, -64(%rbp)
	movq -64(%rbp), %rdi
	callq fun2
	movq %rax, -56(%rbp)
	xorq %rax, %rax
.Lend_main:
	movq %rbp, %rsp
	popq %rbp
	retq

	.globl subroutine1
	.text
subroutine1:
	pushq %rbp
	movq %rsp, %rbp
	subq $112, %rsp
.L0:
movq b(%rip), %r11
movq %r11, -16(%rbp)
movq $0, -24(%rbp)
movq -16(%rbp), %r11
subq -24(%rbp), %r11
movq %r11, -16(%rbp)
	movq -16(%rbp), %r11
	cmpq $0, %r11
	je .L1
jmp .L2
.L1:
movq a(%rip), %r11
movq %r11, -32(%rbp)
movq $1, -40(%rbp)
movq -32(%rbp), %r11
subq -40(%rbp), %r11
movq %r11, -32(%rbp)
	movq -32(%rbp), %r11
	cmpq $0, %r11
	je .L3
jmp .L4
.L3:
movq z(%rip), %r11
movq %r11, -56(%rbp)
movq $6, -64(%rbp)
movq -56(%rbp), %r11
addq -64(%rbp), %r11
movq %r11, -48(%rbp)
	movq -48(%rbp), %rdi
	callq __bx_print_int
	movq %rax, -8(%rbp)
movq $0, a(%rip)
jmp .L5
.L4:
movq c(%rip), %r11
movq %r11, -72(%rbp)
	movq -72(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq x(%rip), %r11
movq %r11, -80(%rbp)
movq z(%rip), %r11
movq %r11, -88(%rbp)
movq -80(%rbp), %r11
addq -88(%rbp), %r11
movq %r11, x(%rip)
.L5:
movq x(%rip), %r11
movq %r11, -96(%rbp)
movq $36, -104(%rbp)
movq -96(%rbp), %r11
subq -104(%rbp), %r11
movq %r11, -96(%rbp)
	movq -96(%rbp), %r11
	cmpq $0, %r11
	je .L6
jmp .L7
.L6:
movq $1, b(%rip)
movq b(%rip), %r11
movq %r11, -112(%rbp)
	movq -112(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
jmp .L8
.L7:
.L8:
jmp .L0
.L2:
.Lend_subroutine1:
	movq %rbp, %rsp
	popq %rbp
	retq

	.globl subroutine2
	.text
subroutine2:
	pushq %rbp
	movq %rsp, %rbp
	subq $144, %rsp
	movq %rdi, -120(%rbp)
	movq %rsi, -128(%rbp)
	movq %rdx, -136(%rbp)
	movq %rcx, -144(%rbp)
.L0:
movq -128(%rbp), %r11
movq %r11, -16(%rbp)
movq $0, -24(%rbp)
movq -16(%rbp), %r11
subq -24(%rbp), %r11
movq %r11, -16(%rbp)
	movq -16(%rbp), %r11
	cmpq $0, %r11
	je .L1
jmp .L2
.L1:
movq -120(%rbp), %r11
movq %r11, -32(%rbp)
movq $1, -40(%rbp)
movq -32(%rbp), %r11
subq -40(%rbp), %r11
movq %r11, -32(%rbp)
	movq -32(%rbp), %r11
	cmpq $0, %r11
	je .L3
jmp .L4
.L3:
movq y(%rip), %r11
movq %r11, -56(%rbp)
movq $6, -64(%rbp)
movq -56(%rbp), %r11
addq -64(%rbp), %r11
movq %r11, -48(%rbp)
	movq -48(%rbp), %rdi
	callq __bx_print_int
	movq %rax, -8(%rbp)
movq $0, -120(%rbp)
jmp .L5
.L4:
movq c(%rip), %r11
movq %r11, -72(%rbp)
	movq -72(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq -136(%rbp), %r11
movq %r11, -80(%rbp)
movq -144(%rbp), %r11
movq %r11, -88(%rbp)
movq -80(%rbp), %r11
addq -88(%rbp), %r11
movq %r11, -136(%rbp)
.L5:
movq -136(%rbp), %r11
movq %r11, -96(%rbp)
movq $36, -104(%rbp)
movq -96(%rbp), %r11
subq -104(%rbp), %r11
movq %r11, -96(%rbp)
	movq -96(%rbp), %r11
	cmpq $0, %r11
	je .L6
jmp .L7
.L6:
movq $1, -128(%rbp)
movq -128(%rbp), %r11
movq %r11, -112(%rbp)
	movq -112(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
jmp .L8
.L7:
.L8:
jmp .L0
.L2:
.Lend_subroutine2:
	movq %rbp, %rsp
	popq %rbp
	retq

	.globl fun1
	.text
fun1:
	pushq %rbp
	movq %rsp, %rbp
	subq $192, %rsp
.L0:
movq b(%rip), %r11
movq %r11, -16(%rbp)
movq $0, -24(%rbp)
movq -16(%rbp), %r11
subq -24(%rbp), %r11
movq %r11, -16(%rbp)
	movq -16(%rbp), %r11
	cmpq $0, %r11
	je .L1
jmp .L2
.L1:
movq a(%rip), %r11
movq %r11, -32(%rbp)
movq $1, -40(%rbp)
movq -32(%rbp), %r11
subq -40(%rbp), %r11
movq %r11, -32(%rbp)
	movq -32(%rbp), %r11
	cmpq $0, %r11
	je .L3
jmp .L4
.L3:
movq z(%rip), %r11
movq %r11, -56(%rbp)
movq $6, -64(%rbp)
movq -56(%rbp), %r11
addq -64(%rbp), %r11
movq %r11, -48(%rbp)
	movq -48(%rbp), %rdi
	callq __bx_print_int
	movq %rax, -8(%rbp)
movq $0, a(%rip)
movq $1, -72(%rbp)
	movq -72(%rbp), %rax
	jmp .Lend_fun1
jmp .L5
.L4:
movq c(%rip), %r11
movq %r11, -80(%rbp)
	movq -80(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq x(%rip), %r11
movq %r11, -88(%rbp)
movq z(%rip), %r11
movq %r11, -96(%rbp)
movq -88(%rbp), %r11
addq -96(%rbp), %r11
movq %r11, x(%rip)
movq x(%rip), %r11
movq %r11, -104(%rbp)
	movq -104(%rbp), %rax
	jmp .Lend_fun1
.L5:
movq x(%rip), %r11
movq %r11, -112(%rbp)
movq $36, -152(%rbp)
movq -112(%rbp), %r11
subq -152(%rbp), %r11
movq %r11, -112(%rbp)
	movq -112(%rbp), %r11
	cmpq $0, %r11
	je .L6
jmp .L7
.L6:
movq $1, b(%rip)
movq b(%rip), %r11
movq %r11, -160(%rbp)
	movq -160(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq $0, -168(%rbp)
	movq -168(%rbp), %rax
	jmp .Lend_fun1
jmp .L8
.L7:
.L8:
movq $1, -176(%rbp)
	movq -176(%rbp), %rax
	jmp .Lend_fun1
jmp .L0
.L2:
movq x(%rip), %r11
movq %r11, -184(%rbp)
	movq -184(%rbp), %rax
	jmp .Lend_fun1
.Lend_fun1:
	movq %rbp, %rsp
	popq %rbp
	retq

	.globl fun2
	.text
fun2:
	pushq %rbp
	movq %rsp, %rbp
	subq $192, %rsp
	movq %rdi, -128(%rbp)
.L0:
movq -128(%rbp), %r11
movq %r11, -16(%rbp)
movq $0, -24(%rbp)
movq -16(%rbp), %r11
subq -24(%rbp), %r11
movq %r11, -16(%rbp)
	movq -16(%rbp), %r11
	cmpq $0, %r11
	je .L1
jmp .L2
.L1:
movq a(%rip), %r11
movq %r11, -32(%rbp)
movq $1, -40(%rbp)
movq -32(%rbp), %r11
subq -40(%rbp), %r11
movq %r11, -32(%rbp)
	movq -32(%rbp), %r11
	cmpq $0, %r11
	je .L3
jmp .L4
.L3:
movq z(%rip), %r11
movq %r11, -56(%rbp)
movq $6, -64(%rbp)
movq -56(%rbp), %r11
addq -64(%rbp), %r11
movq %r11, -48(%rbp)
	movq -48(%rbp), %rdi
	callq __bx_print_int
	movq %rax, -8(%rbp)
movq $0, a(%rip)
movq a(%rip), %r11
movq %r11, -72(%rbp)
	movq -72(%rbp), %rax
	jmp .Lend_fun2
jmp .L5
.L4:
movq c(%rip), %r11
movq %r11, -80(%rbp)
	movq -80(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq x(%rip), %r11
movq %r11, -88(%rbp)
movq z(%rip), %r11
movq %r11, -96(%rbp)
movq -88(%rbp), %r11
addq -96(%rbp), %r11
movq %r11, x(%rip)
movq c(%rip), %r11
movq %r11, -104(%rbp)
	movq -104(%rbp), %rax
	jmp .Lend_fun2
.L5:
movq x(%rip), %r11
movq %r11, -112(%rbp)
movq $36, -152(%rbp)
movq -112(%rbp), %r11
subq -152(%rbp), %r11
movq %r11, -112(%rbp)
	movq -112(%rbp), %r11
	cmpq $0, %r11
	je .L6
jmp .L7
.L6:
movq $1, -128(%rbp)
movq -128(%rbp), %r11
movq %r11, -160(%rbp)
	movq -160(%rbp), %rdi
	callq __bx_print_bool
	movq %rax, -8(%rbp)
movq -128(%rbp), %r11
movq %r11, -168(%rbp)
	movq -168(%rbp), %rax
	jmp .Lend_fun2
jmp .L8
.L7:
.L8:
movq $0, -176(%rbp)
	movq -176(%rbp), %rax
	jmp .Lend_fun2
jmp .L0
.L2:
movq a(%rip), %r11
movq %r11, -184(%rbp)
	movq -184(%rbp), %rax
	jmp .Lend_fun2
.Lend_fun2:
	movq %rbp, %rsp
	popq %rbp
	retq

