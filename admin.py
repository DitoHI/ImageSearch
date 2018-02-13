from django.contrib import admin
from .models import Photo, Upload

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["quote", "updated", "timestamp"]
    class Meta:
        model = Photo

class KeyWordAdmin(admin.ModelAdmin):
    list_display = ["pic", "updated", "timestamp"]
    class Meta:
        model = Upload

admin.site.register(Photo, PostModelAdmin)
admin.site.register(Upload, KeyWordAdmin)
