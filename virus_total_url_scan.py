



import sys
import os
import requests

if len(sys.argv) != 2:
	print('Usage: URL to scan')
	sys.exit(1)

params = {'apikey': os.environ.get('API_VIRUS_TOTAL_KEY'), 'url': sys.argv[1]}
response = requests.post('https://virustotal.com/vtapi/v2/url/scan', data=params)
json_response = response.json()

print('response ', json_response)
