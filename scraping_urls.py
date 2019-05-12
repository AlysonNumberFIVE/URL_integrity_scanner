

import requests
import time
import os


def scrape_urls(filename: str, url_only: str) -> bool:
	"""Access the VT API and run scans on single URLs or URL files.

	:param: filename: Either the file name of the URL file to be read
		or the name of the single URL to be scanned.
	:param: url_only: The boolean statement to determine if filename
		is either a file name or a URL to be scanned.
	:return: True on successful call (status code 200)
		and False otherwise.
	"""
	log = str()
	if url_only is True:
		params = {'apikey': os.environ.get('API_VIRUS_TOTAL_KEY'), 'url': filename} 
		response = requests.post('https://virustotal.com/vtapi/v2/url/scan', data=params)
		try:
			json_response = response.json()
		except:
			return False
		log = json_response['scan_id'] + '\t\t' + filename + '\n'
	else:
		file_content = open(filename).read().split('\n')
		for url in file_content:
			params = {'apikey': os.environ.get('API_VIRUS_TOTAL_KEY'), 'url': url}
			response = requests.post('https://virustotal.com/vtapi/v2/url/scan', data=params)
			try:
				json_response = response.json()
			except:
				return False
			log = log + json['scan_id'] + '\t\t' + filename + '\n'
	if len(log) > 0:
		scan_file = open('report/scan_log.log', 'a')
		scan_file.write(log)
		scan_file.close()
	return True

