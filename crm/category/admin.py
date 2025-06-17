from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'parent', 'slug', 'category_image')
    list_filter = ('is_active', 'parent')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    def category_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height:40px;">'
        return ''
    category_image.short_description = 'Rasm'
    category_image.allow_tags = True
