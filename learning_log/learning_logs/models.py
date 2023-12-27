from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    # text adında bir CharField tanımlıyoruz. Bu veritabanında bir sütun oluşturacak.
    text = models.CharField(max_length=200)  # max karakter uzunluğu 200
    # date_added adından bir DateTimeField tanımlıyoruz. Bu veritabanında bir sütun oluşturacak.
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Modelin string temsilini yazalım.
    def __str__(self):
        return self.text


# Topic (başlıklar) altında belirli bir girdi girebilmek için Entry isimli model
class Entry(models.Model):
    """Something specific learned about a topic"""
    # ForeignKey field'ı 'çoktan bire' ilişkiyi temsil eder. Her Entry bir Topic ile ilişkilidir.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # on_delete eğer ilgili Topic silinirse altındaki tüm Entry'ler de silinir.
    text = models.TextField()   # Kullanıcının bir topic altında girdiği Entry'i tutar.
    date_added = models.DateTimeField(auto_now_add=True)  # Entry'nin oluşturulduğu zaman

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
