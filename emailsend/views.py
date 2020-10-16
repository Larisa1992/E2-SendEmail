from django.shortcuts import render
from emailsend.models import MyEmail
from django.core.mail import send_mail,get_connection
from django.core import mail
from django.http import HttpResponse
# from django_mandrill.mail.mandrillmail import MandrillTemplateMail

# import sendgrid
from sendemail.settings import DEFAULT_FROM_EMAIL
# from sendgrid.helpers.mail import Mail

def worker(text):
    send_email_with_text(text, EMAIL_FROM, EMAIL_TO)
    

def add_email_to_emails(text, timer):
    TASKS.append({"text": text, "timer": timer})
    t = threading.Timer(timer, worker, args=(text, ))
    t.start()

def index(request):   
    # if request.method == 'POST':
        # _toEmail = request.POST['form_mail']
        # _textmessage = request.POST['user_message']
        # _timedelta = request.POST['timedelta']
    
        # new_mail = MyEmail.objects.create(toEmail = _toEmail, textmessage = _textmessage, timedelta = _timedelta)
        # print(new_mail)
    return render(request, 'index.html')

def success(request):
    
    if request.method == 'POST':

        _toEmail = request.POST['form_mail']
        _textmessage = request.POST['user_message']
        _timedelta = request.POST['timedelta']
    
        new_mail = MyEmail.objects.create(toEmail = _toEmail, textmessage = _textmessage, timedelta = _timedelta)
        print('success(request)')

        try:
            send_mail(
            'Subject here',
            _textmessage,
            DEFAULT_FROM_EMAIL,
            [_toEmail],
            fail_silently=False,
            )
            new_mail.save()
            print('save success in success view')
        except:
            return HttpResponse('Ошибка при отправки письма.')

    
    ten_emails = MyEmail.objects.all()
    context = {
        'ten_emails' : ten_emails,}
    return render(request, 'emails.html', context)
