from django.shortcuts import render
from emailsend.models import MyEmail
from django.core.mail import send_mail, get_connection
from django.http import HttpResponse
import threading

from sendemail.settings import DEFAULT_FROM_EMAIL

def worker(message, from_email, to_email, id_email):
    # html_message
    send_mail('Subject here', message, from_email, [to_email], fail_silently=False,)
    update_status = MyEmail.objects.get(id=id_email)
    update_status.boolsend = True
    update_status.save()
    print(f'worker id_email = {id_email} ')

def index(request):   
    return render(request, 'index.html')

def success(request):
    
    if request.method == 'POST':

        _toEmail = request.POST['form_mail']
        _textmessage = request.POST['user_message']
        _timedelta = int(request.POST['timedelta'])
    
        new_mail = MyEmail.objects.create(toEmail = _toEmail, textmessage = _textmessage, timedelta = _timedelta)

        try:
            print(f' try new_mail.id = {new_mail.id}')
            t = threading.Timer(_timedelta, worker, args=(_textmessage, DEFAULT_FROM_EMAIL, _toEmail, new_mail.id, ))
            t.start()
        except:
            return HttpResponse('Ошибка отправки')
    
    ten_emails = MyEmail.objects.order_by('-id')[:10]
    context = {'ten_emails' : ten_emails,}
    return render(request, 'emails.html', context)
