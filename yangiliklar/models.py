from django.conf import settings
from tinymce import models as tinymce_models
from django.db import models
from django.urls import reverse

class Yangilik(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(verbose_name="Rasm",upload_to="media")
    qisqa = tinymce_models.HTMLField()
    body = tinymce_models.HTMLField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']  


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('more', args=[str(self.id)])