from django.db import models
from django.forms import ModelForm

class Photo(models.Model):
    quote = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    pic = models.FileField()

    def __unicode__(self):
        return self.quote
    def __str__(self):
        return self.quote

class Upload(models.Model):
    pic = models.FileField(upload_to="keyword/")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.pic.name + " - " + self.pic.url

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('pic', )

