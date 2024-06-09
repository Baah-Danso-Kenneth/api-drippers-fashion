from django.contrib import admin

from apps.fashionStyles.models import FashionInspo, FashionInspoImage, Like, Rating, Styles


@admin.register(FashionInspo)
class FashionStyleAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags', 'likes_count', 'average_rating', 'styles']
    search_fields = ['title', 'tags']

admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Styles)
admin.site.register(FashionInspoImage)


