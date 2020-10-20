from django.shortcuts import render
from emailsend.models import MyEmail
from django.core.mail import send_mail, get_connection
from django.http import HttpResponse
import threading
from django.core import mail

from sendemail.settings import DEFAULT_FROM_EMAIL, TIME_ZONE

import datetime

def worker(message, from_email, to_email, id_email):    
    with mail.get_connection() as connection:
        mail.EmailMessage(
            'Subject here', message, from_email, [to_email],
            connection=connection,
        ).send()
  
    update_status = MyEmail.objects.get(id=id_email)
    update_status.boolsend = True
    update_status.save()

def index(request):   
    return render(request, 'index.html')

def success(request):
    
    if request.method == 'POST':

        _toEmail = request.POST['form_mail']
        _textmessage = request.POST['user_message']
        _timedelta = int(request.POST['timedelta'])
        CREATE_DRRM = datetime.datetime.now()

        new_mail = MyEmail.objects.create(toEmail = _toEmail, textmessage = _textmessage, timedelta = _timedelta, createdate = CREATE_DRRM)

        try:
            t = threading.Timer(_timedelta, worker, args=(_textmessage, DEFAULT_FROM_EMAIL, _toEmail, new_mail.id, ))
            t.start()
        except:
            return HttpResponse('Ошибка отправки')
    
    ten_emails = MyEmail.objects.order_by('-id')[:10]
    context = {'ten_emails' : ten_emails,}
    return render(request, 'emails.html', context)
