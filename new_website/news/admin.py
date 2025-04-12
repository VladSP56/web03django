from django.contrib import admin
from .models import Group, News

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')
    list_filter = ('publication_date',)
    search_fields = ('title',)

admin.site.register(Group, GroupAdmin)
admin.site.register(News, NewsAdmin)