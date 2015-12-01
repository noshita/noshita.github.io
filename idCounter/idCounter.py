#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re, json
from datetime import datetime
import pytz


PARENTDIR=os.path.dirname(os.path.abspath(__file__))
def toAbsPath(relativePath, pDir = PARENTDIR):
	return os.path.normpath(os.path.join(pDir,relativePath))
CONFIG_PATH = toAbsPath("./config.json")
STATUS_PATH = toAbsPath("./status.json")

PTN_SLUG = re.compile(r"^(Slug:|:slug:)\s*(\w+)\s*$")

class IdCounter(object):
	def __init__(self,config, status):
		self.postsPath = toAbsPath(config["postsPath"])
		self.target =  re.compile(config["target"]) 
		self.ignore = re.compile(config["ignore"])
		if "idInfo" in status:
			if isinstance(status["idInfo"], dict):
				self.idInfo = status["idInfo"]
			else:
				self.idInfo = {}
		else:
			self.idInfo = {}
		if "idInfo" in status:
			self.meta = status["meta"]
		else:
			self.meta = {}

	# 全部カウント
	def recountAll(self):
		postList = self._setPostList(self.postsPath)
		idList = []
		for post in postList:
			with open(post,"r") as f:
				txtlines = f.readlines()
			for line in txtlines:
				m = PTN_SLUG.match(line)
				if not m is None:
					try :
						idList.append(int(m.group(2))) # PTN_SLUGの2番目の引数要素
					except ValueError:
						print("%s has no NumberTypeId slug." % post) 
		maxID = max(idList)
		self.idInfo["max"] = maxID
		self.idInfo["skipped"] = list(set(range(1,maxID+1)) - set(idList))
		return self.idInfo

	# ズルするカウント
	def count(self):
		self.idInfo["max"] += 1
		# print(self.idInfo["max"])
		return self.idInfo

	# IDを得るために使う
	# 一番利用する
	# 利用後はcountかrecountAllを実行
	def getNextID(self):
		# print(type(self.idInfo["max"]))
		return self.idInfo["max"] + 1

	def _setPostList(self, path):
		postList = []
		for root, dirs, files in os.walk(path):
			for file in files:
				# print(self.target.pattern, file)
				if self.target.match(file):
					# print(file, "Passed")
					if self.ignore.match(file) is None:
						# print(file, "Also Passed")
						postList.append(os.path.join(root, file))
		return postList


def metaInfo():

	now = datetime.now(pytz.timezone('Asia/Tokyo'))
	update = now.strftime("%Y-%m-%d-%X-%Z")

	meta = {"update": update}

	return meta


def main():
	argvs = sys.argv
	argc = len(argvs)
	if (argc > 2):
		print("Usage: python %s or python %s all", argvs[0])
		quit()
	
	# load settings
	with open(CONFIG_PATH) as f:
		config = json.load(f)
	with open(STATUS_PATH) as f:
		status = json.load(f)

	# main
	counter = IdCounter(config,status)
	if argc == 2:
		if argvs[1] == "all":
			idInfo = counter.recountAll()
			
		elif argvs[1] == "cheat":
			idInfo = counter.count()
		else:
			print("Usage: python %s or python %s all", argvs[0])
			quit()
			# Export to status.json
		meta = metaInfo()
		outputData = {"meta":meta, "idInfo":idInfo}
		# print(outputData)
		with open(STATUS_PATH,"w") as f:
			json.dump(outputData,f,sort_keys=True,indent=4)
	else: # arcg == 1
		nextId = counter.getNextID()
		print("Next Slug (post id) is %05d." % nextId)


if __name__ == '__main__':
    main()