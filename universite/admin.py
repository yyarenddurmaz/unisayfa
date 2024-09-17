from django.contrib import admin
from .models import Bolum
from .models import Fakulte
from .models import Kampus
from .models import Haberler


class BolumAdmin(admin.ModelAdmin):
    list_display = ('bolum_no', 'bolum_ad', 'fakulte')


class FakulteAdmin(admin.ModelAdmin):
    list_display = ('fakulte_no', 'fakulte_ad', 'kampus')


class KampusAdmin(admin.ModelAdmin):
    list_display = ('kampus_adi', 'kampus_adres')


class HaberlerAdmin(admin.ModelAdmin):
    list_display = ('haber_baslik', 'haber', 'tarih')


admin.site.register(Bolum, BolumAdmin)
admin.site.register(Fakulte, FakulteAdmin)
admin.site.register(Kampus, KampusAdmin)
admin.site.register(Haberler, HaberlerAdmin)
