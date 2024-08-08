from django.contrib import admin
from .models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Call, Order

# Register your models here.
class VidCatAdmin(admin.ModelAdmin):
    list_display = ('title','en', )
    list_filter = ("title",'en', )
    search_fields = ['title', 'en', ]
    
class VidAdmin(admin.ModelAdmin):
    list_display = ('title', 'short', 'url', 'published',  'author', 'produced', 'created_on',)
    list_filter = ("title", 'short', 'url', 'published', 'author', 'produced', 'created_on',)
    search_fields = ['title', 'short', ]

class ReelCatAdmin(admin.ModelAdmin):
    list_display = ('title','en', )
    list_filter = ("title",'en', )
    search_fields = ['title', 'en', ]
    
class ReelAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'published', 'author', 'created_on',)
    list_filter = ("title", 'video', 'published', 'author', 'created_on',)
    search_fields = ['title', 'short', ]

class ImgCatAdmin(admin.ModelAdmin):
    list_display = ('title','en', )
    list_filter = ("title",'en', )
    search_fields = ['title', 'en', ]
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'author', 'published', 'date',)
    list_filter = ("title", 'image', 'author', 'published', 'date',)
    search_fields = ['title', 'category', ]

class GfxAdmin(admin.ModelAdmin):
    list_display = ('title', 'short', 'image', 'published', 'date', 'magn',)
    list_filter = ('title', 'short', 'image', 'published', 'date', 'magn',)
    search_fields = ['title', 'short', ]   
    
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image', 'published', 'created_on',)
    list_filter = ('title', 'url', 'image', 'published', 'created_on',)
    search_fields = ['title', ]    
    
admin.site.register(VidCat, VidCatAdmin)  
admin.site.register(Vid, VidAdmin)  
admin.site.register(ReelCat, ReelCatAdmin)  
admin.site.register(Reel, ReelAdmin) 
admin.site.register(ImgCat, ImgCatAdmin)  
admin.site.register(Image, ImageAdmin)
admin.site.register(Gfx, GfxAdmin) 
admin.site.register(Website, WebsiteAdmin)