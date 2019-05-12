import os
import time

from flask import url_for
from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms import TextField
from flask import redirect
from wtforms import SubmitField
from flask import request
from werkzeug import secure_filename

from scraping_urls import scrape_urls 
from retrieve_scan_report import retrieve_scan_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
if not os.environ.get('SECRET_KEY'):
	app.config['SECRET_KEY'] = '123456' 

class VirusTotalForm(Form):
	scan = SubmitField('Scan URL')

class EmailForm(Form):
	send = SubmitField('Submit')

@app.route('/none', methods=['GET', 'POST'])
def index():
	return render_template('upload.html')


@app.route('/send-email')
def send_email() -> str:
	print('sending email report')
	retrieve_scan_report()	
	return render_template('email_sent.html')


@app.route('/upload-success', methods=['GET', 'POST'])
def upload_success() -> str:
	email = EmailForm()
	return render_template('scan_success.html', email=email)	


@app.route('/loading')
def loading() -> str:
	return render_template('loading.html')

	
@app.route('/', methods=['GET', 'POST'])
def uplaod() -> str:
	vir = VirusTotalForm()

	if vir.validate_on_submit():
		if vir.scan.data is True:
			if len(request.form['url_input']) == 0:
				return render_template('input_field.html', vir=vir, value=True, value2=False, cooldown=False)
			print('RUN single link scan')
			if scrape_urls(request.form['url_input'], True) is False:
				return render_template('input_field.html', vir=vir, value=True, value2=True, cooldown=True)
			return redirect(url_for('upload_success'))
		else:
			if 'file' not in request.files:
				return render_template('input_field.html', vir=vir, value=False, value2=True, cooldown=False)
			print('RUN Multi-Scan')
			filename = request.files['file']
			filename.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename.filename)))
			if scrape_urls(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename.filename))) is False:
				return render_template('input_field.html', vir=vir, value=True, value2=True, cooldown=True)
			return redirect(url_for('upload_success'))
	return render_template('input_field.html', vir=vir, value=True, value2=True, cooldown=False)


if __name__ == '__main__':
	app.run(debug=True, port=8080)
