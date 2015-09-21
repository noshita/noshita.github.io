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
# [github: id=noshita/noshita.github.io, file=extensions/mdx_myextension.py, repo=gh-pages,slice=10:20,footer=minimal]
# to
# <script src="http://gist-it.appspot.com/github/noshita/noshita.github.io/blob/gh-pages/extensions/mdx_myextension.py?slice=10:20&footer=minimal"></script>
#
GIST_REGEX = re.compile(r"\[gist:\s*(.+?)\s*\]")
GITHUB_REGEX = re.compile(r"\[github:\s*(.+?)\s*\]")
ToDICT_REGEX = re.compile(r"(?P<key>\w+)\s*=\s*(?P<value>[^,\s]+)")

class MyPreprocessor(Preprocessor):
	def run(self, lines):
	    new_lines = []
	    for line in lines:
	    	# Gist
	        mGist = GIST_REGEX.match(line)
	        m=mGist
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
	        # Github
	        mGithub = GITHUB_REGEX.match(line)
	        m=mGithub
	        if m:
	        	dict = {key:value for key,value in ToDICT_REGEX.findall(m.group(1))}
	        	replaced_line = '<script src="http://gist-it.appspot.com/github/'
	        	# print(dict)
	        	if "id" in dict:
	        		replaced_line += dict["id"]+'/blob/'
	        		if "repo" in dict:
	        			replaced_line += dict["repo"]+"/"
	        		else:
	        			replaced_line += "master/"
	        		if "file" in dict:
	        			replaced_line+= dict["file"]
	        		else:
	        			print('Error: "file" is required in the github shortcord.')
	        		
	        		if "slice" in dict or "footer" in dict:
	        			replaced_line+="?"
	        			if "slice" in dict:
	        				replaced_line+="slice="+dict["slice"]
	        				if "footer" in dict:
	        					replaced_line+="&footer="+dict["footer"]
	        			elif "footer" in dict:
	        				replaced_line+="footer="+dict["footer"]
	        		replaced_line += '"></script>'
	        	else:
	        		print('Error: This github short code has no "id" key')
	        		return
	        	new_lines.append(replaced_line)
	        if not mGist:
	        	if not mGithub:
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
