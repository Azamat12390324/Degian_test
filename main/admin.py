from django.contrib import admin
from main.models import Home, About, Services, Contact


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    #list_filter = ('created_at',)


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    #list_filter = ('created_at',)


@admin.register(Services)
class Service(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icon',)
    list_display_links = ('title', 'sub_title',)

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)