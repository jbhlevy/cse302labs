	.bss
buffer:
	.zero 30000

	.text
	.globl main
main:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+21)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+21)(%rip)
.L1:
	 mov (buffer+21)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L2
	 mov (buffer+21)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+21)(%rip)
.L3:
	 mov (buffer+21)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L4
	 jmp .L3
.L4:
.L5:
	 mov (buffer+21)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L6
	 mov (buffer+21)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+21)(%rip)
	 jmp .L5
.L6:
.L7:
	 mov (buffer+11)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L8
.L9:
	 mov (buffer+11)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L10
	 mov (buffer+11)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+11)(%rip)
	 xor %al, %al
	 mov (buffer+21)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+21)(%rip)
	 jmp .L9
.L10:
	 jmp .L7
.L8:
	 xor %al, %al
	 call bf_read
	 mov %al, (buffer+21)(%rip)
	 mov (buffer+21)(%rip), %al
	 sub $10, %al
	 mov %al, (buffer+21)(%rip)
	 jmp .L1
.L2:
.L11:
	 mov (buffer+31)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L12
	 mov (buffer+31)(%rip), %al
	 sub $37, %al
	 mov %al, (buffer+31)(%rip)
	 mov (buffer+40)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+40)(%rip)
	 jmp .L11
.L12:
.L13:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L14
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L15:
	 mov (buffer+31)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L16
	 xor %al, %al
	 mov (buffer+40)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+40)(%rip)
	 jmp .L15
.L16:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L13
.L14:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
.L17:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L18
	 xor %al, %al
	 mov (buffer+31)(%rip), %al
	 add $48, %al
	 mov %al, (buffer+31)(%rip)
	 xor %dil, %dil
	 mov (buffer+31)(%rip), %dil
	 call bf_print
	 mov (buffer+31)(%rip), %al
	 sub $48, %al
	 mov %al, (buffer+31)(%rip)
	 jmp .L17
.L18:
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $58, %al
	 mov %al, (buffer+30)(%rip)
	 xor %dil, %dil
	 mov (buffer+30)(%rip), %dil
	 call bf_print
	 mov (buffer+30)(%rip), %al
	 sub $26, %al
	 mov %al, (buffer+30)(%rip)
	 xor %dil, %dil
	 mov (buffer+30)(%rip), %dil
	 call bf_print
.L19:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L20
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L19
.L20:
	 xor %al, %al
	 mov (buffer+42)(%rip), %al
	 add $2, %al
	 mov %al, (buffer+42)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L21:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L22
.L23:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L24
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L23
.L24:
.L25:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L26
.L27:
	 mov (buffer+44)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L28
	 mov (buffer+44)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+44)(%rip)
	 jmp .L27
.L28:
.L29:
	 mov (buffer+45)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L30
	 mov (buffer+45)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+45)(%rip)
	 jmp .L29
.L30:
.L31:
	 mov (buffer+46)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L32
	 mov (buffer+46)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L31
.L32:
.L33:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L34
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 jmp .L33
.L34:
.L35:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L36
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L35
.L36:
.L37:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L38
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 jmp .L37
.L38:
.L39:
	 mov (buffer+42)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L40
	 mov (buffer+42)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+42)(%rip)
	 xor %al, %al
	 mov (buffer+45)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+45)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L39
.L40:
	 jmp .L25
.L26:
.L41:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L42
.L43:
	 mov (buffer+36)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L44
	 mov (buffer+36)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+36)(%rip)
	 xor %al, %al
	 mov (buffer+32)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+32)(%rip)
	 jmp .L43
.L44:
	 jmp .L41
.L42:
.L45:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L46
.L47:
	 mov (buffer+41)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L48
	 mov (buffer+41)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+41)(%rip)
	 xor %al, %al
	 mov (buffer+44)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+44)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L47
.L48:
	 jmp .L45
.L46:
.L49:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L50
.L51:
	 mov (buffer+36)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L52
	 mov (buffer+36)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+36)(%rip)
	 xor %al, %al
	 mov (buffer+31)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+31)(%rip)
	 jmp .L51
.L52:
	 jmp .L49
.L50:
.L53:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L54
.L55:
	 mov (buffer+43)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L56
	 mov (buffer+43)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+43)(%rip)
	 jmp .L55
.L56:
.L57:
	 mov (buffer+46)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L58
	 mov (buffer+46)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L57
.L58:
.L59:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L60
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 jmp .L59
.L60:
	 jmp .L53
.L54:
.L61:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L62
	 jmp .L61
.L62:
.L63:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L64
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L63
.L64:
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L65:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L66
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L65
.L66:
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L67:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L68
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
.L69:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L70
.L71:
	 mov (buffer+46)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L72
	 mov (buffer+46)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+46)(%rip)
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $2, %al
	 mov %al, (buffer+47)(%rip)
	 jmp .L71
.L72:
	 jmp .L69
.L70:
.L73:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L74
.L75:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L76
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L75
.L76:
.L77:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L78
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L77
.L78:
.L79:
	 mov (buffer+35)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L80
	 mov (buffer+35)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+35)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $2, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L79
.L80:
	 jmp .L73
.L74:
.L81:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L82
.L83:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L84
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L85:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L86
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L87:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L88
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L89:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L90
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L91:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L92
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L93:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L94
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L95:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L96
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L97:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L98
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L99:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L100
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
.L101:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L102
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 mov (buffer+49)(%rip), %al
	 sub $9, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+58)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+58)(%rip)
.L103:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L104
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
	 jmp .L103
.L104:
	 jmp .L101
.L102:
	 jmp .L99
.L100:
	 jmp .L97
.L98:
	 jmp .L95
.L96:
	 jmp .L93
.L94:
	 jmp .L91
.L92:
	 jmp .L89
.L90:
	 jmp .L87
.L88:
	 jmp .L85
.L86:
	 jmp .L83
.L84:
	 jmp .L81
.L82:
.L105:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L106
.L107:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L108
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+35)(%rip)
	 jmp .L107
.L108:
	 jmp .L105
.L106:
.L109:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L110
.L111:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L112
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L113:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L114
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L115:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L116
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L117:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L118
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L119:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L120
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L121:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L122
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L123:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L124
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L125:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L126
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L127:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L128
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
.L129:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L130
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 mov (buffer+46)(%rip), %al
	 sub $9, %al
	 mov %al, (buffer+46)(%rip)
	 xor %al, %al
	 mov (buffer+57)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+57)(%rip)
.L131:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L132
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L131
.L132:
	 jmp .L129
.L130:
	 jmp .L127
.L128:
	 jmp .L125
.L126:
	 jmp .L123
.L124:
	 jmp .L121
.L122:
	 jmp .L119
.L120:
	 jmp .L117
.L118:
	 jmp .L115
.L116:
	 jmp .L113
.L114:
	 jmp .L111
.L112:
	 jmp .L109
.L110:
.L133:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L134
.L135:
	 mov (buffer+34)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L136
	 mov (buffer+34)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+34)(%rip)
	 xor %al, %al
	 mov (buffer+37)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L135
.L136:
	 jmp .L133
.L134:
.L137:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L138
.L139:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L140
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+44)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+44)(%rip)
	 jmp .L139
.L140:
	 jmp .L137
.L138:
.L141:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L142
.L143:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L144
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L143
.L144:
.L145:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L146
.L147:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L148
.L149:
	 mov (buffer+29)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L150
	 mov (buffer+29)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+29)(%rip)
	 jmp .L149
.L150:
.L151:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L152
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 xor %al, %al
	 mov (buffer+29)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+29)(%rip)
	 jmp .L151
.L152:
	 jmp .L147
.L148:
	 jmp .L145
.L146:
	 jmp .L141
.L142:
.L153:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L154
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L155:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L156
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L157:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L158
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L159:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L160
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L161:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L162
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L163:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L164
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L165:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L166
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L167:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L168
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L169:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L170
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L171:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L172
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L173:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L174
.L175:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L176
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L175
.L176:
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L173
.L174:
	 jmp .L171
.L172:
	 jmp .L169
.L170:
	 jmp .L167
.L168:
	 jmp .L165
.L166:
	 jmp .L163
.L164:
	 jmp .L161
.L162:
	 jmp .L159
.L160:
	 jmp .L157
.L158:
	 jmp .L155
.L156:
	 jmp .L153
.L154:
	 jmp .L67
.L68:
.L177:
	 mov (buffer+46)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L178
.L179:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L180
.L181:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L182
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L181
.L182:
.L183:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L184
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 jmp .L183
.L184:
.L185:
	 mov (buffer+44)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L186
	 mov (buffer+44)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+44)(%rip)
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L185
.L186:
	 jmp .L179
.L180:
.L187:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L188
.L189:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L190
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+34)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+34)(%rip)
	 jmp .L189
.L190:
.L191:
	 mov (buffer+35)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L192
	 mov (buffer+35)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+35)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L191
.L192:
	 jmp .L187
.L188:
.L193:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L194
.L195:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L196
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+45)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+45)(%rip)
	 jmp .L195
.L196:
	 jmp .L193
.L194:
.L197:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L198
.L199:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L200
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 jmp .L199
.L200:
	 jmp .L197
.L198:
.L201:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L202
.L203:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L204
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L205:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L206
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L207:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L208
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L209:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L210
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L211:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L212
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L213:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L214
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L215:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L216
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L217:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L218
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L219:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L220
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L221:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L222
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
.L223:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L224
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $10, %al
	 mov %al, (buffer+47)(%rip)
.L225:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L226
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+47)(%rip)
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L225
.L226:
	 mov (buffer+57)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+57)(%rip)
	 jmp .L223
.L224:
	 jmp .L221
.L222:
	 jmp .L219
.L220:
	 jmp .L217
.L218:
	 jmp .L215
.L216:
	 jmp .L213
.L214:
	 jmp .L211
.L212:
	 jmp .L209
.L210:
	 jmp .L207
.L208:
	 jmp .L205
.L206:
	 jmp .L203
.L204:
	 jmp .L201
.L202:
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+47)(%rip)
.L227:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L228
.L229:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L230
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 jmp .L229
.L230:
.L231:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L232
.L233:
	 mov (buffer+34)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L234
	 mov (buffer+34)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+34)(%rip)
	 jmp .L233
.L234:
.L235:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L236
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+34)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+34)(%rip)
	 jmp .L235
.L236:
.L237:
	 mov (buffer+36)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L238
	 mov (buffer+36)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+36)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L237
.L238:
	 jmp .L231
.L232:
.L239:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L240
.L241:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L242
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+49)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+46)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+46)(%rip)
	 jmp .L241
.L242:
	 jmp .L239
.L240:
.L243:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L244
.L245:
	 mov (buffer+33)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L246
	 mov (buffer+33)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+33)(%rip)
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L245
.L246:
	 jmp .L243
.L244:
.L247:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L248
.L249:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L250
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L251:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L252
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L253:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L254
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L255:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L256
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L257:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L258
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L259:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L260
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L261:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L262
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L263:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L264
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L265:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L266
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
.L267:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L268
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 mov (buffer+43)(%rip), %al
	 sub $9, %al
	 mov %al, (buffer+43)(%rip)
	 xor %al, %al
	 mov (buffer+59)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+59)(%rip)
.L269:
	 mov (buffer+49)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L270
	 mov (buffer+49)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+49)(%rip)
	 xor %al, %al
	 mov (buffer+43)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+43)(%rip)
	 jmp .L269
.L270:
	 jmp .L267
.L268:
	 jmp .L265
.L266:
	 jmp .L263
.L264:
	 jmp .L261
.L262:
	 jmp .L259
.L260:
	 jmp .L257
.L258:
	 jmp .L255
.L256:
	 jmp .L253
.L254:
	 jmp .L251
.L252:
	 jmp .L249
.L250:
	 jmp .L247
.L248:
	 jmp .L227
.L228:
.L271:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L272
	 jmp .L271
.L272:
.L273:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L274
.L275:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L276
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L275
.L276:
.L277:
	 mov (buffer+46)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L278
	 mov (buffer+46)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+46)(%rip)
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+47)(%rip)
	 jmp .L277
.L278:
.L279:
	 mov (buffer+45)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L280
	 mov (buffer+45)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+45)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L279
.L280:
	 jmp .L273
.L274:
.L281:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L282
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L283:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L284
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L285:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L286
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+36)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+36)(%rip)
.L287:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L288
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L289:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L290
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+36)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+36)(%rip)
.L291:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L292
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L293:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L294
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+36)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+36)(%rip)
.L295:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L296
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L297:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L298
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+36)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+36)(%rip)
.L299:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L300
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L299
.L300:
	 jmp .L297
.L298:
	 jmp .L295
.L296:
	 jmp .L293
.L294:
	 jmp .L291
.L292:
	 jmp .L289
.L290:
	 jmp .L287
.L288:
	 jmp .L285
.L286:
	 jmp .L283
.L284:
.L301:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L302
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+37)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+37)(%rip)
	 jmp .L301
.L302:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L281
.L282:
.L303:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L304
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+26)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+26)(%rip)
	 jmp .L303
.L304:
.L305:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L306
.L307:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L308
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+36)(%rip), %al
	 add $5, %al
	 mov %al, (buffer+36)(%rip)
	 jmp .L307
.L308:
	 jmp .L305
.L306:
.L309:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L310
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L311:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L312
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L313:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L314
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+35)(%rip)
.L315:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L316
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L317:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L318
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+35)(%rip)
.L319:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L320
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L321:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L322
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+35)(%rip)
.L323:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L324
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L325:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L326
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+35)(%rip)
.L327:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L328
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L327
.L328:
	 jmp .L325
.L326:
	 jmp .L323
.L324:
	 jmp .L321
.L322:
	 jmp .L319
.L320:
	 jmp .L317
.L318:
	 jmp .L315
.L316:
	 jmp .L313
.L314:
	 jmp .L311
.L312:
.L329:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L330
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L329
.L330:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L309
.L310:
.L331:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L332
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+25)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+25)(%rip)
	 jmp .L331
.L332:
.L333:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L334
.L335:
	 mov (buffer+48)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L336
	 mov (buffer+48)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+48)(%rip)
	 xor %al, %al
	 mov (buffer+35)(%rip), %al
	 add $5, %al
	 mov %al, (buffer+35)(%rip)
	 jmp .L335
.L336:
	 jmp .L333
.L334:
.L337:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L338
	 jmp .L337
.L338:
	 jmp .L177
.L178:
.L339:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L340
.L341:
	 mov (buffer+43)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L342
	 mov (buffer+43)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+43)(%rip)
	 xor %al, %al
	 mov (buffer+47)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+48)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+48)(%rip)
	 jmp .L341
.L342:
	 jmp .L339
.L340:
.L343:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L344
.L345:
	 mov (buffer+37)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L346
	 mov (buffer+37)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+33)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+33)(%rip)
	 jmp .L345
.L346:
.L347:
	 mov (buffer+32)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L348
	 mov (buffer+32)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+32)(%rip)
	 xor %al, %al
	 mov (buffer+37)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+37)(%rip)
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L347
.L348:
	 jmp .L343
.L344:
.L349:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L350
.L351:
	 mov (buffer+47)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L352
	 mov (buffer+47)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+47)(%rip)
	 xor %al, %al
	 mov (buffer+42)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+42)(%rip)
	 jmp .L351
.L352:
	 jmp .L349
.L350:
.L353:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L354
.L355:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L356
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L355
.L356:
.L357:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L358
.L359:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L360
.L361:
	 mov (buffer+28)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L362
	 mov (buffer+28)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+28)(%rip)
	 jmp .L361
.L362:
.L363:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L364
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+28)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+28)(%rip)
	 jmp .L363
.L364:
	 jmp .L359
.L360:
	 jmp .L357
.L358:
	 jmp .L353
.L354:
.L365:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L366
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
.L367:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L368
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L369:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L370
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L371:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L372
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L373:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L374
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L375:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L376
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L377:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L378
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L379:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L380
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L381:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L382
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L383:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L384
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
.L385:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L386
.L387:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L388
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L387
.L388:
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L385
.L386:
	 jmp .L383
.L384:
	 jmp .L381
.L382:
	 jmp .L379
.L380:
	 jmp .L377
.L378:
	 jmp .L375
.L376:
	 jmp .L373
.L374:
	 jmp .L371
.L372:
	 jmp .L369
.L370:
	 jmp .L367
.L368:
	 jmp .L365
.L366:
	 xor %al, %al
	 mov (buffer+39)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+39)(%rip)
.L389:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L390
.L391:
	 mov (buffer+39)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L392
	 mov (buffer+39)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+39)(%rip)
	 jmp .L391
.L392:
.L393:
	 mov (buffer+38)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L394
	 mov (buffer+38)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+38)(%rip)
	 jmp .L393
.L394:
	 xor %al, %al
	 mov (buffer+38)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+38)(%rip)
	 xor %al, %al
	 mov (buffer+42)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+42)(%rip)
.L395:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L396
	 jmp .L395
.L396:
.L397:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L398
.L399:
	 mov (buffer+34)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L400
.L401:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L402
	 jmp .L401
.L402:
	 xor %al, %al
	 mov (buffer+34)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+34)(%rip)
	 jmp .L399
.L400:
	 jmp .L397
.L398:
.L403:
	 mov (buffer+60)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L404
	 jmp .L403
.L404:
.L405:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L406
	 jmp .L405
.L406:
	 mov (buffer+54)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+54)(%rip)
.L407:
	 mov (buffer+54)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L408
.L409:
	 mov (buffer+54)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L410
	 xor %al, %al
	 mov (buffer+54)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+54)(%rip)
	 jmp .L409
.L410:
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
.L411:
	 mov (buffer+60)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L412
.L413:
	 mov (buffer+61)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L414
	 mov (buffer+61)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+61)(%rip)
	 jmp .L413
.L414:
.L415:
	 mov (buffer+63)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L416
	 mov (buffer+63)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+63)(%rip)
	 xor %al, %al
	 mov (buffer+61)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+61)(%rip)
	 jmp .L415
.L416:
	 jmp .L411
.L412:
.L417:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L418
	 xor %al, %al
	 mov (buffer+50)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+50)(%rip)
.L419:
	 mov (buffer+52)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L420
	 xor %al, %al
	 mov (buffer+60)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+60)(%rip)
	 jmp .L419
.L420:
	 mov (buffer+50)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+50)(%rip)
	 jmp .L417
.L418:
	 mov (buffer+50)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+50)(%rip)
.L421:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L422
	 xor %al, %al
	 mov (buffer+52)(%rip), %al
	 add $48, %al
	 mov %al, (buffer+52)(%rip)
	 xor %dil, %dil
	 mov (buffer+52)(%rip), %dil
	 call bf_print
	 mov (buffer+52)(%rip), %al
	 sub $48, %al
	 mov %al, (buffer+52)(%rip)
	 jmp .L421
.L422:
	 xor %al, %al
	 mov (buffer+50)(%rip), %al
	 add $32, %al
	 mov %al, (buffer+50)(%rip)
	 xor %dil, %dil
	 mov (buffer+50)(%rip), %dil
	 call bf_print
.L423:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L424
	 mov (buffer+50)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+50)(%rip)
	 jmp .L423
.L424:
	 jmp .L407
.L408:
.L425:
	 mov (buffer+60)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L426
.L427:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L428
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L429:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L430
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L431:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L432
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L433:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L434
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L435:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L436
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L437:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L438
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L439:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L440
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L441:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L442
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L443:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L444
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
.L445:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L446
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 mov (buffer+67)(%rip), %al
	 sub $9, %al
	 mov %al, (buffer+67)(%rip)
	 xor %al, %al
	 mov (buffer+72)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+72)(%rip)
.L447:
	 mov (buffer+62)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L448
	 mov (buffer+62)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+62)(%rip)
	 xor %al, %al
	 mov (buffer+67)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+67)(%rip)
	 jmp .L447
.L448:
	 jmp .L445
.L446:
	 jmp .L443
.L444:
	 jmp .L441
.L442:
	 jmp .L439
.L440:
	 jmp .L437
.L438:
	 jmp .L435
.L436:
	 jmp .L433
.L434:
	 jmp .L431
.L432:
	 jmp .L429
.L430:
	 jmp .L427
.L428:
	 jmp .L425
.L426:
.L449:
	 mov (buffer+50)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L450
.L451:
	 mov (buffer+57)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L452
	 mov (buffer+57)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+57)(%rip)
	 xor %al, %al
	 mov (buffer+52)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+52)(%rip)
	 jmp .L451
.L452:
	 jmp .L449
.L450:
	 jmp .L389
.L390:
	 jmp .L21
.L22:
.L453:
	 mov (buffer+40)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L454
	 jmp .L453
.L454:
.L455:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L456
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+30)(%rip)
.L457:
	 mov (buffer+31)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L458
	 xor %al, %al
	 mov (buffer+40)(%rip), %al
	 add $1, %al
	 mov %al, (buffer+40)(%rip)
	 jmp .L457
.L458:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
	 jmp .L455
.L456:
	 mov (buffer+30)(%rip), %al
	 sub $1, %al
	 mov %al, (buffer+30)(%rip)
.L459:
	 mov (buffer+30)(%rip), %al
	 mov $0, %bl
	 cmp %al, %bl
	 je .L460
	 xor %al, %al
	 mov (buffer+31)(%rip), %al
	 add $48, %al
	 mov %al, (buffer+31)(%rip)
	 xor %dil, %dil
	 mov (buffer+31)(%rip), %dil
	 call bf_print
	 jmp .L459
.L460:
	 xor %al, %al
	 mov (buffer+30)(%rip), %al
	 add $10, %al
	 mov %al, (buffer+30)(%rip)
	 xor %dil, %dil
	 mov (buffer+30)(%rip), %dil
	 call bf_print
	retq
