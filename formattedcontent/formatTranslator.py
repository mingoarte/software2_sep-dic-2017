import formattedcontent.ply.lex as lex
import formattedcontent.ply.yacc as yacc
	
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

def t_error(t):
	print("Illegal char '%s'" %t.value[0])
	t.lexer.skip(1)

def tokenizeText(translator):
	
	translator.lexer.input(translator.text)
	while True:
		tok = translator.lexer.token()
		
		if not tok:
			break
		
		translator.tokenList.append(tok.value)
	
class FormatTranslator(object):
	
	def __init__(self, text):
		self.text = text
		self.lexer = lex.lex()
		self.tokenList = []
		self.translatedTokenList = []
		self.translatedText = ''
		
		# Dict containing correspondency between tags and html
		self.translations = {
			'[b]' : '<b>',
			'[/b]' : '</b>',
			'[i]' : '<i>',
			'[/i]' : '</i>',
			'\n' : '</br>'
		}
		
	def getTokenList(self):
		tokenizeText(self)
		
	def translateTokens(self):
		for token in self.tokenList:
			self.translatedTokenList.append(self.translations.get(token, token))
				
	def joinTokens(self):
		for token in self.translatedTokenList:
			self.translatedText += token
			
	def translateText(self):
		self.getTokenList()
		self.translateTokens()
		self.joinTokens()
