from django.contrib import admin

from .models import Bboard


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )


admin.site.register(Bboard, BboardAdmin)
