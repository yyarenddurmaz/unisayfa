from django.db import models


class Haberler(models.Model):
    haber_baslik = models.CharField(max_length=50, default="haber_baslik")
    haber_kisaltma = models.CharField(max_length=20, default="haber_kisaltma")
    haber = models.TextField(max_length=400, default="haber")
    tarih = models.DateTimeField()

    def __str__(self):
        return f" {self.haber_baslik} {self.haber} {self.tarih}"


class Kampus(models.Model):
    kampus_adi = models.CharField(max_length=50, default="kampus_adi")
    kampus_adres = models.CharField(max_length=100, default="kampus_adres")

    def __str__(self):
        return f"{self.kampus_adi}"


class Fakulte(models.Model):
    fakulte_no = models.IntegerField(default=0)
    fakulte_ad = models.CharField(max_length=50, default="fakulte_ad")
    fakulte_kisaltma = models.TextField(max_length=5, default="ttt")
    fakulte_dekan = models.CharField(max_length=50, default="fakulte_dekan")
    fakulte_tel = models.CharField(max_length=50, default="fakulte_tel")
    fakulte_mail = models.CharField(max_length=50, default="fakulte_mail")
    fakulte_url = models.CharField(max_length=200, default="fakulte_url")
    fakulte_logo = models.CharField(max_length=50, default="fakulte_logo")
    kampus = models.ForeignKey(Kampus,
                               on_delete=models.CASCADE,
                               related_name='fakulteler',
                               default=1)

    def __str__(self):
        return f"{self.fakulte_ad}"


class Bolum(models.Model):
    bolum_no = models.IntegerField(default=0)
    bolum_ad = models.CharField(max_length=50, default="bolum_ad")
    bolum_kisaltma = models.TextField(max_length=5, default="ttt")
    bolum_baskan = models.CharField(max_length=50, default="bolum_baskan")
    bolum_tel = models.CharField(max_length=50, default="bolum_tel")
    bolum_mail = models.CharField(max_length=50, default="bolum_mail")
    bolum_adres = models.CharField(max_length=100, default="bolum_adres")
    bolum_url = models.CharField(max_length=200, default="bolum_url")
    bolum_logo = models.CharField(max_length=50, default="bolum_logo")
    bolum_staj = models.TextField(max_length=400, default="bolum_staj")
    bolum_erasmus = models.TextField(max_length=400, default="bolum_erasmus")
    bolum_ciftyan = models.TextField(max_length=400, default="bolum_ciftyan")
    bolum_mezun = models.TextField(max_length=400, default="bolum_mezun")
    bolum_profil = models.TextField(max_length=400, default="bolum_profil")
    bolum_firsat = models.TextField(max_length=400, default="bolum_firsat")
    fakulte = models.ForeignKey(Fakulte,
                                on_delete=models.CASCADE,
                                related_name='bolumler',
                                default=1)

    def __str__(self):
        return f"{self.bolum_ad}"
