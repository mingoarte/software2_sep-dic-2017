import ply.lex as lex
import ply.yacc as yacc
	
tokens = (
	'BOLD_START',
	'BOLD_END',
	'ITALIC_START',
	'ITALIC_END',
	'NEW_LINE',
	'TEXT'
	)
	
t_BOLD_START = r'\[b\]'
t_BOLD_END = r'\[/b\]'
t_ITALIC_START = r'\[i\]'
t_ITALIC_END = r'\[/i\]'
t_NEW_LINE = r'\n'
t_TEXT = r'.'
"""
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
"""
def t_error(t):
	print("Illegal char '%s'" %t.value[0])
	#print(t)
	t.lexer.skip(1)
		
lexer = lex.lex()
string = 'PUTAS [b]PUTAS EN NEGRITA[/b] [i]PUTAS EN ITALICA[/i] [b] ME VOLVI [i] LOCO [/b] AAAH [/i]\n\nNOJODA SALTO DELINEA OP'
lexer.input(string)
lists=[]
while True:
	tok = lexer.token()
	
	if not tok:
		break
	
	lists.append(tok.value)
	
print(lists)
