import formattedcontent.ply.lex as lex
import formattedcontent.ply.yacc as yacc
from functools import partial

class TranslatorOutput:
	def __init__(self, text, index):
		self.text = text
		self.index = index

tokens = (
	'BOLD_START',
	'BOLD_END',
	'ITALIC_START',
	'ITALIC_END',
	'SMALL_START',
	'SMALL_END',
	'HIGHLIGHTED_START',
	'HIGHLIGHTED_END',
	'DELETED_START',
	'DELETED_END',
	'UNDERLINED_START',
	'UNDERLINED_END',
	'SUPERINDEX_START',
	'SUPERINDEX_END',
	'SUBINDEX_START',
	'SUBINDEX_END',
	'IMG_START',
	'IMG_END',
	'LINK_START',
	'LINK_END',
	'NAME_START',
	'NAME_END',
	'QUOTE_START',
	'QUOTE_END',
	'NEW_LINE',
	'TEXT'
	)
	
t_BOLD_START = r'\[b\]'
t_BOLD_END = r'\[/b\]'
t_ITALIC_START = r'\[i\]'
t_ITALIC_END = r'\[/i\]'
t_SMALL_START = r'\[s\]'
t_SMALL_END = r'\[/s\]'
t_HIGHLIGHTED_START = r'\[h\]'
t_HIGHLIGHTED_END = r'\[/h\]'
t_DELETED_START = r'\[d\]'
t_DELETED_END = r'\[/d\]'
t_UNDERLINED_START = r'\[u\]'
t_UNDERLINED_END = r'\[/u\]'
t_SUPERINDEX_START = r'\[sup\]'
t_SUPERINDEX_END = r'\[/sup\]'
t_SUBINDEX_START = r'\[sub\]'
t_SUBINDEX_END = r'\[/sub\]'
t_IMG_START = r'\[img\]'
t_IMG_END = r'\[/img\]'
t_LINK_START = r'\[link\]'
t_LINK_END = r'\[/link\]'
t_NAME_START = r'\[name\]'
t_NAME_END = r'\[/name\]'
t_QUOTE_START = r'\[q\]'
t_QUOTE_END = r'\[/q\]'
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
			'[s]' : '<small>',
			'[/s]' : '</small>',
			'[h]' : '<mark>',
			'[/h]' : '</mark>',
			'[d]' : '<del>',
			'[/d]' : '</del>',
			'[u]' : '<ins>',
			'[/u]' : '</ins>',
			'[sup]' : '<sup>',
			'[/sup]' : '</sup>',
			'[sub]' : '<sub>',
			'[/sub]' : '</sub>',
			'[img]' : partial(self.imageOutput),
			'[/img]' : '',
			'[link]' : partial(self.linkOutput),
			'[/link]' : '',
			'[name]' : partial(self.nameOutput),
			'[/name]' : '',
			'[q]' : '<blockquote>',
			'[/q]' : '</blockquote>',
			'\n' : '</br>'
		}
		
	def getTokenList(self):
		tokenizeText(self)
		
	def translateTokens(self):
		i = 0
		while(i < len(self.tokenList)):
			aux = self.translations.get(self.tokenList[i], self.tokenList[i])
			if(type(aux) == str):
				self.translatedTokenList.append(aux)
				i += 1
			else:
				output = aux(i)
				self.translatedTokenList.append(output.text)
				i = output.index
				
	def joinTokens(self):
		self.translatedText += '<pre>'
		for token in self.translatedTokenList:
			self.translatedText += token
		self.translatedText += '</pre>'
			
	def translateText(self):
		self.getTokenList()
		self.translateTokens()
		self.joinTokens()
		
	def imageOutput(self, currIndex):
		i = currIndex+1
		link = ''
		while(i < len(self.tokenList)):
			if(self.tokenList[i] == '[/img]'):
				break
			link += self.tokenList[i]
			i += 1
			
		html = "<img src='"+str(link)+"'>"
		
		return TranslatorOutput(text = html, index = i+1)
		
	def linkOutput(self, currIndex):
		i = currIndex+1
		link = ''
		name = ''
		while(i<len(self.tokenList)):
			if(self.tokenList[i] == '[/link]'):
				break
			elif(self.tokenList[i] == '[name]'):
				nameOutput = self.nameOutput(i)
				name = nameOutput.text
				i = nameOutput.index
				continue
				
			link += self.tokenList[i]
			i += 1
		if( name == '' ):
			name = link
		html = "<a href='"+str(link)+"'>"+str(name)+"</a>"
		
		return TranslatorOutput(text = html, index = i+1)
		
	def nameOutput(self, currIndex):
		i = currIndex+1
		name = ''
		while(i<len(self.tokenList)):
			if(self.tokenList[i] == '[/name]'):
				break

			name += self.translations.get(self.tokenList[i], self.tokenList[i])
			i += 1
			
		return TranslatorOutput(text = name, index = i+1)
