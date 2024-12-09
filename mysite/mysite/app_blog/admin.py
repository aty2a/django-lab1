from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')  # Display the slug in the list view
    prepopulated_fields = {'slug': ('category',)}  # Auto-generate slug from category
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),  # Include slug field in the admin form
        }),
    )

admin.site.register(Category, CategoryAdmin)

# ArticleImage Inline Admin
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )

# Article Admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}  # Prepopulate slug based on title
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description', 'main_page'),
        }),
        ('Додатково', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    # Custom delete file method
    def delete_file(self, pk, request):
        """Delete an image."""
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)
