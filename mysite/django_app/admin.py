from django.contrib import admin

from .models import BookInfo
from .models import LineInfo

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_data']

class LineInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'line', 'name','value']

admin.site.register(BookInfo, BookInfoAdmin)

admin.site.register(LineInfo, LineInfoAdmin)


