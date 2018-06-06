from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog',views.blog ,name= 'blog'), 
    path('contact',views.contact,name = 'contact'),
    path('about',views.about, name='about'),
    path('post',views.post, name = 'post'),
    path('',views.home, name='home'),
    
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)