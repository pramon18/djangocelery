from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from api.tasks import add

# Create your views here.
def index(request):
    task_id = add.delay(4, 4)
    html = "<html><body>O ID do seu JOB é {%s}.</body></html>" % task_id    
    return HttpResponse(html)

def progress(request, task_id):
    print(task_id)
    res = AsyncResult(task_id)
    print(res, res.ready(), res.result, res.state)
    if res.ready():
        html = "<html><body>O resultado do seu JOB é: {%s}.</body></html>" % res.result    
    else:
        html = res.result    
    return HttpResponse(html)