from django.db import models

class MyEmail(models.Model):
    toEmail = models.EmailField(max_length=100, verbose_name='кому отпправляем письмо')
    textmessage = models.CharField(max_length= 250, verbose_name='текст сообщения')
    createdate = models.DateTimeField(auto_now_add=True ,verbose_name='Дата создания')
    timedelta = models.PositiveSmallIntegerField(verbose_name='промежуток задержки отправки пиьсма')
    boolsend = models.BooleanField(default=False, verbose_name='Признак отправки')

