# URL Integrity Scanner
Scans URLs using the VirusTotal API to check for malware/malicious URLs and potential phishing atacks.

## Demonstration
This is a short demonstration on how to use this particular API in a Python application.

Store your API key in the API_VIRUS_TOTAL_KEY environment variable as well as your secret key. Then run:
```
python3 flask_server.py
```
to run the application in debug mode (by default).

Upon getting an email request to send a report to (this isn't implemented), the command line will display
a summary of your scan results done by various security venders like this:

```
CLEAN MX >  {'detected': True, 'result': 'phishing site'}
DNS8 >  {'detected': False, 'result': 'clean site'}
OpenPhish >  {'detected': False, 'result': 'clean site'}
VX Vault >  {'detected': False, 'result': 'clean site'}
ZDB Zeus >  {'detected': False, 'result': 'clean site'}
ZCloudsec >  {'detected': False, 'result': 'clean site'}
PhishLabs >  {'detected': False, 'result': 'unrated site'}
Zerofox >  {'detected': False, 'result': 'clean site'}
K7AntiVirus >  {'detected': False, 'result': 'clean site'}
FraudSense >  {'detected': False, 'result': 'clean site'}
...
```
Once email's configured, these results will be formatted in the response and an email
will be sent with the scan results. This is more useful for bulk scans where a single
read from a single screen (terminal/web browser etc.) isn't practical.

This is strictly for demoing purposes but can be used to analyse links for suspicious activity
(if you'd like).

Ideally check out the VirusTotal API directly and get your free API key:
https://www.virustotal.com/en/documentation/public-api/

written by @AlysonBelle
