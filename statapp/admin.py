from django.contrib import admin

from statapp.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['date', 'email', 'message', 'status']

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
# Register your models here.
