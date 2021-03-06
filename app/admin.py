from django.contrib import admin
from app.models import *


admin.site.register(Track)

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio',)
    fieldsets = (
        ('General information', {
            'fields': ('name', 'bio',)
        }),
        ('Social media', {
            'classes': ('collapse',),
            'fields': ('twitter', 'facebook',),
            'description': 'Add social media here'
        })
    )


admin.site.register(Speaker, SpeakerAdmin)

class SessionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'abstract')
    list_display = ['title', 'speaker', 'status']
    list_filter = ['track__title', 'speaker']
    actions = ['make_approved',]

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(status = 'a')
        if rows_updated == 1:
            message_bit = '1 session was'
        else:
            message_bit = '{num} sessions were'.format(num=rows_updated)

        self.message_user(request, '{mb} approved'.format(mb=message_bit))

    make_approved.short_description = 'Mark session(s) as approved'


admin.site.register(Session, SessionAdmin)
