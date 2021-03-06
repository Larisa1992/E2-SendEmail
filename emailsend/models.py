from django.db import models
from django.utils import timezone

class MyEmail(models.Model):
    toEmail = models.EmailField(max_length=100, verbose_name='кому отпправляем письмо')
    textmessage = models.CharField(max_length= 250, verbose_name='текст сообщения')
    createdate = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    timedelta = models.PositiveSmallIntegerField(verbose_name='промежуток задержки отправки пиьсма')
    boolsend = models.BooleanField(default=False, verbose_name='Признак отправки')

