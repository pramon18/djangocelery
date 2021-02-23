from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from celery_app import celery_t
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    task_id = celery_t.download.delay()
    html = '<html>\
                <body>\
                    <h1>O id da task a ser checada é: {%s} </h1>\
                </body>\
            </html>' % task_id
    return HttpResponse(html)

@csrf_exempt
def progress(request, task_id):
    res = AsyncResult(task_id)
    print(res.state, task_id)
    if res.ready():
        html = "<html><body>O resultado do seu JOB é: {%s}.</body></html>" % res.result    
    else:
        html = "<html><body>O resultado do seu JOB ainda não está pronto.</body></html>"    
    return HttpResponse(html)

# @csrf_exempt
# def upload_file(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         print(type(request.FILES['myfile']), request.FILES['myfile'].size)
#         if request.FILES['myfile'].size < 3000000:
#             # If file size is less than 3MB
#             # Django does it
#             file = request.FILES['myfile']
#             with open('txt_de_upload.txt', 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#         else:
#             file = request.FILES['myfile']
#             with open('txt_de_upload', 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#     html = "<html><body>Arquivo chegou no Django</body></html>"
#     return HttpResponse(html)