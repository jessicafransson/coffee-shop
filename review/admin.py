from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'created_on',
        'rating',
        'user',
        'body',
    )

    ordering = ('-created_on', 'rating',)
    list_filter = ('product', 'rating',)


admin.site.register(Review, ReviewAdmin)
