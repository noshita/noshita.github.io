#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, json

class IdCounter(object):
	def __init__(self,config):
		pass

	def countAll(self):

		result = {"max":, "skipped":, }
		return result

	def countId(self):
		return result

	def _setPostList(self, path):


	def _crawl(self,path):
		self
		aPath = self._toAbsolutePath(path)


	def _toAbsolutePath(self,relativePath):

		return absolutePath

def metaInfo(object):

	now = datetime.datetime.now()

	meta = {"update": now, }

	return meta


def main():
	PARENTDIR=os.path.dirname(os.path.abspath(__file__))
	CONFIG_PATH = os.path.normpath(os.path.join(PARENTDIR, "./config.json"))
	STATUS_PATH = os.path.normpath(os.path.join(PARENTDIR, "./status.json"))

	argvs = sys.argv
	argc = len(argvs)
	if (argc > 2):
		print("Usage: python %s or python %s all", argvs[0])
		quit()
	
	# load settings
	with open(CONFIG_PATH,"rb") as f:
		config = json.
	with open(STATUS_PATH,"rb") as f:
		status = 

	# main
	counter = IdCounter(config)
	if argc == 2:
		if argvs[1] != "all":
			print("Usage: python %s or python %s all", argvs[0])
			quit()
		else:
			result = counter.countId()
	else: # arcg == 1
		result = counter.countId()

	# Export to status.json
	meta = metaInfo()
	with open(STATUS_PATH,"wb") as f:
		outputData = {"meta":meta, "idInfo":result}


if __name__ == '__main__':
    main()