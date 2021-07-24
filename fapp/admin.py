from django.contrib import admin
from .models import Register,UserPosts,Interaction

class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','age','img','date']

admin.site.register(Register,RegisterAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=['id','name','img','description','date','user']
    list_filter=['date','user']

admin.site.register(UserPosts,PostAdmin)

class InteractionAdmin(admin.ModelAdmin):
    list_display=['id','comment','user']
    list_filter=['comment','user']

admin.site.register(Interaction,InteractionAdmin)

