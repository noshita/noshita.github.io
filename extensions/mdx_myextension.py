import markdown
from markdown.inlinepatterns import SimpleTagPattern
from markdown.preprocessors import Preprocessor
import re


# Insert u tag
U_RE = r"(\_\_)(.+?)\_\_"

# Embed gist
# 
# [gist:id=noshita/811a6bd47f03387ae0a4,file= test.py]
# To
# <script src="https://gist.github.com/noshita/811a6bd47f03387ae0a4.js?file=test.py"></script>
#
# [gist:id=noshita/811a6bd47f03387ae0a4]
# To
# <script src="https://gist.github.com/noshita/811a6bd47f03387ae0a4.js"></script>
#
GIST_REGEX = re.compile(r"\[gist:\s*(.+?)\s*\]")
GITHUB_REGEX = re.compile(r"\[github:\s*(.+?)\s*\]")
ToDICT_REGEX = re.compile(r"(?P<key>\w+)\s*=\s*(?P<value>[\w\./]+)")

class MyPreprocessor(Preprocessor):
	def run(self, lines):
	    new_lines = []
	    for line in lines:
	        m = GIST_REGEX.match(line)
	        if m:
	        	dict = {key:value for key,value in ToDICT_REGEX.findall(m.group(1))}
	        	replaced_line = '<script src="https://gist.github.com/'
	        	# print(dict)
	        	if "id" in dict:
	        		replaced_line += dict["id"]+'.js'
	        		if "file" in dict:
	        			replaced_line+= '?file='+ dict["file"]
	        		replaced_line += '"></script>'
	        	else:
	        		print('Error: This gist short code has no "id" key')
	        		return
	        	new_lines.append(replaced_line)
	        else:
	        	new_lines.append(line)
	    return new_lines

# Set Extension
class MyExtension(markdown.Extension):
	def extendMarkdown(self, md, md_globals):
		# Embed gist
		preprocessor = MyPreprocessor(md)
		preprocessor.config = self.getConfigs()
		md.preprocessors.add("preprocessor", preprocessor, "_end")
		# Insert u tag
		md.inlinePatterns.add('u', SimpleTagPattern(U_RE, 'u'), '<not_strong')

def makeExtension(configs={}):
    return MyExtension(configs=dict(configs))
