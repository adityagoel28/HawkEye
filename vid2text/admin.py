from django.contrib import admin
from vid2text.models import videoUploader

# from api.models import leetcodeUsername

class videoUploaderAdmin(admin.ModelAdmin):
    list_display = ('video', 'url')
    search_fields = ('video',)

# Register your models here.
admin.site.register(videoUploader, videoUploaderAdmin)