from flask import Flask, render_template_string
import csv, os
from datetime import datetime
app = Flask(__name__)

def envoyer_et_loguer(numero, message):
    statut = "ENVOYE"
    with open('sms_logs.csv','a',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow([datetime.now().strftime("%d/%m %H:%M"),numero,message,statut])
    return True

HTML = """
<html><head><meta http-equiv="refresh" content="5">
<style>body{font-family:Arial;padding:15px} table{width:100%;background:white} th{background:#007bff;color:white}</style>
</head><body>
<h2>UBANGI FLOOD PREDICT - Controle Gemena</h2>
<p>Heure: {{heure}} | Total SMS: {{total}}</p>
<table border=1 cellpadding=8><tr><th>Heure</th><th>Numero</th><th>Message</th><th>Statut</th></tr>
{% for l in logs %}<tr><td>{{l[0]}}</td><td>{{l[1]}}</td><td>{{l[2]}}</td><td>{{l[3]}}</td></tr>{% endfor %}
</table></body></html>
"""

@app.route('/')
def dash():
    logs=[]
    if os.path.exists('sms_logs.csv'):
        with open('sms_logs.csv','r',encoding='utf-8') as f:
            logs=list(csv.reader(f))[-100:][::-1]
    return render_template_string(HTML,heure=datetime.now().strftime("%H:%M:%S"),logs=logs,total=len(logs))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
