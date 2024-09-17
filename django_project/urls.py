from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('fakulte/', views.fakulte),
    path('bolum/<str:bolum_kisaltma>/', views.bolum, name='bolum'),
    path('admin/', admin.site.urls),
    path('veriliste/', views.liste),
    path('veriliste/fakulte/ekle/', views.yenikayit, name='fakulte_ekle'),
    path('veriliste/bolum/ekle/', views.yenikayit1, name='bolum_ekle'),
    path('veriliste/fakulte/detay/<str:fakulte_kisaltma>/',
         views.fakulte_detay,
         name='fakultedetay'),
    path('veriliste/bolum/detay/<str:bolum_kisaltma>/',
         views.bolum_detay,
         name='bolumdetay'),
    path('veriliste/fakulte/duzenle/<str:fakulte_kisaltma>/',
         views.fakulte_duzenle),
    path('veriliste/bolum/duzenle/<str:bolum_kisaltma>/', views.bolum_duzenle),
    path('veriliste/haber/ekle/', views.yenikayit2, name='haber_ekle'),
    path('veriliste/haber/detay/<str:haber_kisaltma>/', views.haber_detay),
    path('veriliste/haber/duzenle/<str:haber_kisaltma>/', views.haber_duzenle),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register),
    path('logout/', views.user_logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
