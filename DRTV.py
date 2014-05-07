#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import urllib.request
import re
import json
import sys
import os

def getVideoData(url):
	videoData = "http://www.dr.dk/mu/programcard/expanded/"

	p = re.compile("dr\.dk/tv/se/.+/(.+)")

	try:
		videoTitle = p.search(url).groups()[0]
	except:
		print("Invalid URL")
		raise SystemExit

	res = urllib.request.urlopen(videoData + videoTitle)
	decodedResponse = res.read().decode("utf-8")
	data = json.loads(decodedResponse)

	if data["ResultSize"] == 0:
		print("Program not found.")
		raise SystemExit

	return videoTitle, data["Data"][0]

def getVideoStream(data, quality):
	videoStream = "";

	for asset in data["Assets"]:
		if asset["Kind"] == "VideoResource":
			links = asset["Links"]
			break

	streams = []
	for stream in links:
		if stream["Target"] == "Streaming":
			streams.append(stream)

	videoStream = streams[quality]["Uri"]

	if not videoStream:
		print("Video stream not found.")
		raise SystemExit

	p = re.compile("/mp4:(.+)\?ID=")
	downloadURL = p.search(videoStream).groups()[0]

	return downloadURL

if __name__ == "__main__":
	quality = 0
	if len(sys.argv) == 1:
		print("""Syntax:
		%s url [quality]
		Available qualities:
		0 - Best
		1 - High
		2 - Average
		3 - Low""" % os.path.basename(__file__) )
		raise SystemExit
	if len(sys.argv) > 1:
		if len(sys.argv) == 3:
			quality = int(sys.argv[2])
			if quality > 3 or quality < 0:
				print("Invalid quality")
				raise SystemExit
		if len(sys.argv) >= 2:
			url = sys.argv[1]

	videoTitle, data = getVideoData(url)

	baseURL = "http://vodfiles.dr.dk/"
	downloadURL = getVideoStream(data, quality)

	downloadURL = baseURL + downloadURL
	os.system("wget -O " + videoTitle + ".mp4 " + downloadURL)
