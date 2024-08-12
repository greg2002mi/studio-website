from django.contrib import admin
from .models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Videosam, Forwhom, Wedo
from orders.models import Order, Call

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
    list_display = ('title', 'url', 'image', 'published', 'created_on', 'updated_on',)
    list_filter = ('title', 'url', 'image', 'published', 'created_on', 'updated_on',)
    search_fields = ['title', ]  
    
class SmmAdmin(admin.ModelAdmin):
    list_display = ('title', 'en', 'created_on', 'updated_on',)
    list_filter = ('title', 'en', 'created_on', 'updated_on',)
    search_fields = ['title', 'en', ]

class EgSmmAdmin(admin.ModelAdmin):
    list_display = ('title1', 'short1', 'image1',  'title2', 'short2', 'image2', 'published', 'lang', 'created_on', 'updated_on',)
    list_filter = ('title1', 'short1', 'image1',  'title2', 'short2', 'image2', 'published', 'lang', 'created_on', 'updated_on',)
    search_fields = ['title1', 'short1', 'title2', 'short2', 'lang',]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price',  'published', 'lang', 'currency', 'author',)
    list_filter = ('title', 'content', 'price',  'published', 'lang', 'currency', 'author',)
    search_fields = ['title', 'content', 'price',] 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',  'status', 'note', 'created_on',)
    list_filter = ('name', 'phone', 'email',  'status', 'note', 'created_on',)
    search_fields = ['name', 'phone', 'email', 'note',]  

class CallAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',  'status', 'note', 'created_on', 'question1', 'question2',)
    list_filter = ('name', 'phone', 'email',  'status', 'note', 'created_on', 'question1', 'question2',)
    search_fields = ['name', 'phone', 'email', 'note', 'question1', 'question2',]
    
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image',  'published', 'created_on', 'updated_on',)
    list_filter = ('title', 'url', 'image',  'published', 'created_on', 'updated_on',)
    search_fields = ['title', 'url',]  
    
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'team', 'studio', 'lang', 'published', 'updated_on', 'created_on',)
    list_filter = ('title', 'content', 'team', 'studio', 'lang', 'published', 'updated_on', 'created_on',)
    search_fields = ['title', 'content', ]    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company', 'content', 'rank', 'updated_on', 'created_on',)
    list_filter = ('name', 'role', 'company', 'content', 'rank', 'updated_on', 'created_on',)
    search_fields = ['name', 'role', 'company', 'content',]    

class VideosamAdmin(admin.ModelAdmin):
    list_display = ('video1', 'video2', 'video3',)
    list_filter = ('video1', 'video2', 'video3',)  
    
class ForwhomAdmin(admin.ModelAdmin):
    list_display = ('service', 'en', 'ko', )
    list_filter = ('service', 'en', 'ko', )
    search_fields = ['service', 'en', 'ko', ]    
    
class WedoAdmin(admin.ModelAdmin):
    list_display = ('service', 'en', 'ko', )
    list_filter = ('service', 'en', 'ko', )
    search_fields = ['service', 'en', 'ko', ]    
    
admin.site.register(VidCat, VidCatAdmin)  
admin.site.register(Vid, VidAdmin)
admin.site.register(ReelCat, ReelCatAdmin)  
admin.site.register(Reel, ReelAdmin) 
admin.site.register(ImgCat, ImgCatAdmin)  
admin.site.register(Image, ImageAdmin)
admin.site.register(Gfx, GfxAdmin) 
admin.site.register(Website, WebsiteAdmin)
admin.site.register(SMM, SmmAdmin)
admin.site.register(EgSMM, EgSmmAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientsAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Videosam, VideosamAdmin)
admin.site.register(Forwhom, ForwhomAdmin)
admin.site.register(Wedo, WedoAdmin)
admin.site.register(Call, CallAdmin)


