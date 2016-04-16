from django.contrib import admin
from .models import Post, Category
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('categories',)
    fields = ('author', 'categories', ('title', 'slug'), 'description', 'content')

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
