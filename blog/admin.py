from django.contrib import admin
from .models import Post, Category
# class PostAdmin(admin.ModelAdmin):
#     list_filter = ('categories',)
#     fields = ('author', 'categories', ('title', 'slug'), 'description', 'content')
#
#     class Meta:
#         model = Post

admin.site.register(Post)
admin.site.register(Category)

# class CategoryAdmin(admin.ModelAdmin):
#
#     class Meta:
#         model = Category

# admin.site.register(Category, CategoryAdmin)
