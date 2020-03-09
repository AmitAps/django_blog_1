from django.contrib import admin

# Register your models here.
from .models import Post

#https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','updated','timestamp')
    list_filter = ("updated","timestamp")
    search_fields = ('title','timestamp')
    list_display_links = ('updated',)

    #class Meta:
        # model = Post
#admin.site.register(Post, PostModelAdmin)
