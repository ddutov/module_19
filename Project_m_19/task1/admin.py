from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    # fields = [('title', 'cost', 'size'), 'description']
    fieldsets = (
        ('info', {
            'fields':
                ('title', 'cost', 'size')
        }),
        ('footer', {
            'fields':
                ('description',)
        })
    )
    search_fields = ('title',)
    list_filter = ('cost',)


admin.site.register(Buyer)

