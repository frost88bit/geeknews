from django.contrib import admin

from .forms import NewsForm
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'date', 'pic')
    form = NewsForm