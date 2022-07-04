from django.contrib import admin
from feed.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

# Connect Post and PostAdmin 
# (inherit from admin.ModelAdmin)
admin.site.register(Post, PostAdmin)