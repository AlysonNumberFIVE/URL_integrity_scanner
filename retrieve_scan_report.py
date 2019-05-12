

import os
import requests

def sort_scans(scan):
	
	for key, value in scan.items():
		print(key, '> ', value)


def format_report(report_response) -> None:
	
	for report_line in report_response:
		if report_line == 'scans':
			sort_scans(report_response[report_line])
		else:
			print(': ', report_line, report_response[report_line])	

def retrieve_scan_report():
	scan_log = open('report/scan_log.log').read().split('\n')
	for log in scan_log:
		report_hash = log.split('\t\t')
		headers = {
			"Accept-Encoding": "gzip, deflate",
			"User-Agent" : "gzip,  My Python requests library example client or username"
		}
		params = {'apikey': os.environ.get('API_VIRUS_TOTAL_KEY'), 'resource': report_hash[0]}
		response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
		params=params, headers=headers)
		try:
			json_response = response.json()
		except:
			return ;
		format_report(json_response)

