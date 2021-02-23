from celery import Celery

app = Celery('tasks')

import os
import requests

#os.environ['DJANGO_SETTINGS_MODULE'] = "djangocelery.settings"
app.config_from_object('celery_app.celeryconfig')

@app.task(ignore_result=False)
def add(x, y):
    return x + y

@app.task()
def download():
    print("Iniciando o download dentro da task")
    response = {}
    url = "http://eforexcel.com/wp/wp-content/uploads/2020/09/5m-Sales-Records.zip"
    r = requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4412.0 Safari/537.36 Edg/90.0.796.0"})
    
    if r.status_code == 200:
        with open('/usr/src/app/teste.zip', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
        f.close()
    response['status'] = r.status_code
    response['headers'] = r.headers
    return dict({"status": r.status_code})