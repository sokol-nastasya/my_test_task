from django.contrib import admin
from mainApp.models import MainView, Category, Keywords, News

from mptt.admin import MPTTModelAdmin

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'parent', ]
	mptt_level_indent = 20

class KeywordsAdmin(admin.ModelAdmin):
	fields = ['name', ]

admin.site.register(MainView)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(News)
