from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from universite.models import Fakulte, Bolum, Kampus, Haberler
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm


def anasayfa(request):
    bilgi = {'haberliste': Haberler.objects.all().order_by('tarih')}
    return render(request, 'anasayfa.html', bilgi)


def fakulte(request):
    bilgi = {'fakulteliste': Fakulte.objects.all().order_by('fakulte_ad')}
    sablon = loader.get_template('fakulte.html')
    return HttpResponse(sablon.render(bilgi, request))


def bolum(request, bolum_kisaltma):
    bilgi = {'bolum': Bolum.objects.get(bolum_kisaltma=bolum_kisaltma)}
    sablon = loader.get_template('bolum.html')
    return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def user_login(request):
    if request.user.is_authenticated:
        return redirect("anasayfa")

    bilgi = {}

    if request.method == 'POST':
        kullaniciadi = request.POST['username']
        sifre = request.POST['password']
        kullanici = authenticate(request,
                                 username=kullaniciadi,
                                 password=sifre)

        if kullanici is not None:
            login(request, kullanici)
            return redirect("anasayfa")

        else:
            bilgi['login'] = 'Hata'

    sablon = loader.get_template('login.html')
    return HttpResponse(sablon.render(bilgi, request))


def user_register(request):
    sablon = loader.get_template('register.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            kullaniciadi = form.cleaned_data["username"]
            sifre = form.cleaned_data["password1"]
            kullanici = authenticate(request,
                                     username=kullaniciadi,
                                     password=sifre)
            login(request, kullanici)
            return redirect("anasayfa")
        else:
            bilgi = {"form": form}
            return HttpResponse(sablon.render(bilgi, request))
    form = UserCreationForm()
    bilgi = {"form": form}
    return HttpResponse(sablon.render(bilgi, request))


def user_logout(request):
    logout(request)
    return redirect("anasayfa")


def fakulte_detay(request, fakulte_kisaltma):
    fakulte = Fakulte.objects.get(fakulte_kisaltma=fakulte_kisaltma)
    bilgi = {'fakulte': fakulte}
    sablon = loader.get_template('fakulte_detay.html')
    return HttpResponse(sablon.render(bilgi, request))


def bolum_detay(request, bolum_kisaltma):
    bolum = Bolum.objects.get(bolum_kisaltma=bolum_kisaltma)
    bilgi = {'bolum': bolum}
    sablon = loader.get_template('bolum_detay.html')
    return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def fakulte_duzenle(request, fakulte_kisaltma):
    hatalar = []
    bilgi = {
        'fakulte': Fakulte.objects.get(fakulte_kisaltma=fakulte_kisaltma),
        'yenikayit': "False",
        'hatalistesi': hatalar
    }

    if request.method == 'POST':

        fakulte = Fakulte.objects.get(fakulte_kisaltma=fakulte_kisaltma)

        fakulte.kampus.kampus_adi = request.POST['kampus_adi']
        if len(fakulte.kampus.kampus_adi) == 0:
            hatalar.append("Geçersiz kampüs girişi.")
        fakulte.fakulte_no = request.POST['fakulte_no']
        if len(fakulte.fakulte_no) == 0 or len(fakulte.fakulte_no) > 3:
            hatalar.append("Geçersiz fakülte numarası.")
        fakulte.fakulte_ad = request.POST['fakulte_ad']
        if len(fakulte.fakulte_ad) == 0:
            hatalar.append("Geçersiz fakülte adı.")
        fakulte.fakulte_kisaltma = request.POST['fakulte_kisaltma']
        if len(fakulte.fakulte_kisaltma) == 0:
            hatalar.append("Geçersiz fakülte kısaltması.")
        fakulte.fakulte_dekan = request.POST['fakulte_dekan']
        if len(fakulte.fakulte_dekan) == 0:
            hatalar.append("Geçersiz fakülte dekanı.")
        fakulte.fakulte_tel = request.POST['fakulte_tel']
        if len(fakulte.fakulte_tel) == 0:
            hatalar.append("Geçersiz fakülte telefonu.")
        fakulte.fakulte_mail = request.POST['fakulte_mail']
        if len(fakulte.fakulte_mail) == 0:
            hatalar.append("Geçersiz fakülte mail adresi.")

        fakulte.fakulte_url = request.POST['fakulte_url']
        if len(fakulte.fakulte_url) == 0:
            hatalar.append("Geçersiz fakülte url'si.")

        fakulte.fakulte_logo = request.POST['fakulte_logo']

        if len(hatalar) == 0:
            fakulte.save()
            bilgi['fakulte'] = fakulte
            bilgi['yenikayit'] = "True"
        else:
            bilgi['hatalistesi'] = hatalar

    sablon = loader.get_template('fakulte_duzenle.html')
    return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def bolum_duzenle(request, bolum_kisaltma):
    fakulteliste = Fakulte.objects.all()
    hatalar = []
    bilgi = {
        'bolum': Bolum.objects.get(bolum_kisaltma=bolum_kisaltma),
        'yenikayit1': "False",
        'hatalistesi': hatalar,
        'fakulteliste': fakulteliste
    }

    if request.method == 'POST':

        bolum = Bolum.objects.get(bolum_kisaltma=bolum_kisaltma)

        fakulte_ad = request.POST['fakulte_ad']
        if len(fakulte_ad) == 0 or len(fakulte_ad) > 30:
            hatalar.append("Geçersiz fakülte girişi.")
        else:
            fakulte = Fakulte.objects.get(fakulte_ad=fakulte_ad)
        bolum.bolum_no = request.POST['bolum_no']
        if len(bolum.bolum_no) == 0 or len(bolum.bolum_no) > 3:
            hatalar.append("Geçersiz bölüm numarası.")
        bolum.bolum_ad = request.POST['bolum_ad']
        if len(bolum.bolum_ad) == 0:
            hatalar.append("Geçersiz bölüm adı.")
        bolum.bolum_kisaltma = request.POST['bolum_kisaltma']
        if len(bolum.bolum_kisaltma) == 0:
            hatalar.append("Geçersiz bölüm kısaltması.")
        bolum.bolum_baskan = request.POST['bolum_baskan']
        if len(bolum.bolum_baskan) == 0:
            hatalar.append("Geçersiz bölüm başkan.")
        bolum.bolum_tel = request.POST['bolum_tel']
        if len(bolum.bolum_tel) == 0:
            hatalar.append("Geçersiz bölüm telefonu.")
        bolum.bolum_mail = request.POST['bolum_mail']
        if len(bolum.bolum_mail) == 0:
            hatalar.append("Geçersiz bölüm mail adresi.")
        bolum.bolum_adres = request.POST['bolum_adres']
        if len(bolum.bolum_adres) == 0:
            hatalar.append("Geçersiz bölüm adresi.")
        bolum.bolum_url = request.POST['bolum_url']
        if len(bolum.bolum_url) == 0:
            hatalar.append("Geçersiz bölüm url'si.")

        bolum.bolum_logo = request.POST['bolum_logo']

        bolum.bolum_staj = request.POST['bolum_staj']
        if len(bolum.bolum_staj) == 0:
            hatalar.append("Geçersiz bölüm staj bilgisi.")
        bolum.bolum_erasmus = request.POST['bolum_erasmus']
        if len(bolum.bolum_erasmus) == 0:
            hatalar.append("Geçersiz bölüm erasmus bilgisi.")
        bolum.bolum_ciftyan = request.POST['bolum_ciftyan']
        if len(bolum.bolum_ciftyan) == 0:
            hatalar.append("Geçersiz bölüm çift anadal - yandal bilgisi.")
        bolum.bolum_mezun = request.POST['bolum_mezun']
        if len(bolum.bolum_mezun) == 0:
            hatalar.append("Geçersiz bölüm mezun bilgisi.")
        bolum.bolum_profil = request.POST['bolum_profil']
        if len(bolum.bolum_profil) == 0:
            hatalar.append("Geçersiz bölüm profil bilgisi.")
        bolum.bolum_firsat = request.POST['bolum_firsat']
        if len(bolum.bolum_firsat) == 0:
            hatalar.append("Geçersiz bölüm fırsat bilgisi.")

        if len(hatalar) == 0:
            bolum.fakulte_ad = fakulte
            bolum.save()
            bilgi['bolum'] = bolum
            bilgi['yenikayit1'] = "True"
        else:
            bilgi['hatalistesi'] = hatalar

    sablon = loader.get_template('bolum_duzenle.html')
    return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def fakulte_ekle(request):
    return render(request, 'fakulte_ekle.html')


@csrf_exempt
def bolum_ekle(request):
    return render(request, 'bolum_ekle.html')


@csrf_exempt
def haber_ekle(request):
    return render(request, 'haber_ekle.html')


def liste(request):
    fakulteliste = Fakulte.objects.all().order_by('fakulte_ad')
    bolumliste = Bolum.objects.all().order_by('fakulte', 'bolum_ad')
    haberliste = Haberler.objects.all().order_by('tarih')

    if request.method == 'POST':
        silinecek_fakulte = request.POST.get('sil1')
        if silinecek_fakulte:
            try:
                fakulte = Fakulte.objects.get(
                    fakulte_kisaltma=silinecek_fakulte)
                fakulte.delete()
            except Fakulte.DoesNotExist:
                pass

        silinecek_bolum = request.POST.get('sil2')
        if silinecek_bolum:
            try:
                bolum = Bolum.objects.get(bolum_kisaltma=silinecek_bolum)
                bolum.delete()
            except Bolum.DoesNotExist:
                pass

        silinecek_haber = request.POST.get('sil3')
        if silinecek_haber:
            try:
                haber = Haberler.objects.get(haber_kisaltma=silinecek_haber)
                haber.delete()
            except Haberler.DoesNotExist:
                pass

    veriler = {
        'fakulteliste': fakulteliste,
        'bolumliste': bolumliste,
        'haberliste': haberliste
    }

    sablon = loader.get_template('veriListe.html')
    return HttpResponse(sablon.render(veriler, request))


@csrf_exempt
def yenikayit(request):
    kampusler = Kampus.objects.all()
    hatalar = []
    bilgi = {
        'yenikayit': "False",
        'hatalistesi': hatalar,
        'kampuslistesi': kampusler
    }
    template_name = 'fakulte_ekle.html'

    if request.method == 'POST':
        kampus_adi = request.POST.get('kampus_adi')
        fakulte_no = request.POST.get('fakulte_no', '')
        fakulte_ad = request.POST.get('fakulte_ad', '')
        fakulte_kisaltma = request.POST['fakulte_kisaltma']

        if fakulte_no and fakulte_ad and fakulte_kisaltma and kampus_adi:
            if len(fakulte_no) != 3:
                hatalar.append("Fakülte Numarası 3 Haneli Olmalıdır")
            if len(fakulte_ad) < 2:
                hatalar.append("Fakülte Adı Boş Geçilemez")
            if len(fakulte_kisaltma) == 0:
                hatalar.append("Fakülte Kısaltması Boş Geçilemez")

            if not hatalar:
                kampus_adi = Kampus.objects.get(kampus_adi=kampus_adi)
                yeni = Fakulte(fakulte_no=fakulte_no,
                               fakulte_ad=fakulte_ad,
                               fakulte_kisaltma=fakulte_kisaltma)
                yeni.save()
                bilgi = {'yenikayit': "True"}
        else:
            hatalar.append(
                "Fakülte Numarası, Fakülte Adı, Fakülte Kısaltması zorunludur."
            )

    return render(request, template_name, bilgi)


@csrf_exempt
def yenikayit1(request):
    fakulteler = Fakulte.objects.all()
    hatalar = []
    bilgi = {
        'yenikayit1': "False",
        'hatalistesi': hatalar,
        'fakulteliste': fakulteler
    }
    template_name = 'bolum_ekle.html'

    if request.method == 'POST':
        fakulte_ad = request.POST['fakulte']
        bolum_no = request.POST['bolum_no']
        bolum_ad = request.POST['bolum_ad']

        bolum_kisaltma = request.POST['bolum_kisaltma']

        if bolum_no and bolum_ad and bolum_kisaltma:
            if len(bolum_no) != 3:
                hatalar.append("Bölüm Numarası 3 Haneli Olmalıdır")
            if len(bolum_ad) < 2:
                hatalar.append("Bölüm Adı Boş Geçilemez")
            if len(bolum_kisaltma) == 0:
                hatalar.append("Bölüm Kısaltması Boş Geçilemez")

            if not hatalar:
                fakulte = Fakulte.objects.get(fakulte_ad=fakulte_ad)

                yeni1 = Bolum(fakulte=fakulte,
                              bolum_no=bolum_no,
                              bolum_ad=bolum_ad,
                              bolum_kisaltma=bolum_kisaltma)
                yeni1.save()
                bilgi = {'yenikayit1': "True"}
        else:
            hatalar.append(
                "Bölüm Numarası, Bölüm Adı, Bölüm Kısaltması zorunludur.")

    return render(request, template_name, bilgi)


@csrf_exempt
def yenikayit2(request):
    hatalar = []
    bilgi = {
        'yenikayit2': "False",
        'hatalistesi': hatalar,
    }
    template_name = 'haber_ekle.html'

    if request.method == 'POST':
        haber_baslik = request.POST.get('haber_baslik', '')
        haber_kisaltma = request.POST.get('haber_kisaltma', '')
        haber = request.POST['haber']
        tarih = request.POST['tarih']
        if haber_baslik and haber_kisaltma and haber and tarih:
            if len(haber_baslik) == 0:
                hatalar.append("Haber Başlığı Boş Geçilemez.")
            if len(haber_kisaltma) > 10:
                hatalar.append("Haber Kısaltması Kısa Olmalıdır.")
            if len(haber) == 0:
                hatalar.append("Haber Metni Boş Geçilemez.")
            if len(tarih) == 0:
                hatalar.append("Haber Tarihi Boş Geçilemez.")

            if not hatalar:
                yeni2 = Haberler(haber_baslik=haber_baslik,
                                 haber_kisaltma=haber_kisaltma,
                                 haber=haber,
                                 tarih=tarih)
                yeni2.save()
                bilgi = {'yenikayit2': "True"}
        else:
            hatalar.append(
                "Haber Başlığı, Haber Kısaltması, Haber Metni ve Haber Tarihi zorunludur."
            )

    return render(request, template_name, bilgi)


def haber_detay(request, haber_kisaltma):
    haber = Haberler.objects.get(haber_kisaltma=haber_kisaltma)
    bilgi = {'haber': haber}
    sablon = loader.get_template('haber_detay.html')
    return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def haber_duzenle(request, haber_kisaltma):
    hatalar = []
    bilgi = {
        'haber': Haberler.objects.get(haber_kisaltma=haber_kisaltma),
        'yenikayit2': "False",
        'hatalistesi': hatalar
    }

    if request.method == 'POST':

        haber = Haberler.objects.get(haber_kisaltma=haber_kisaltma)

        haber.haber_baslik = request.POST['haber_baslik']
        if len(haber.haber_baslik) == 0:
            hatalar.append("Geçersiz başlık. Bir cümle ile ifade ediniz.")

        haber.haber_kisaltma = request.POST['haber_kisaltma']
        if len(haber.haber_kisaltma) > 10:
            hatalar.append(
                "Geçersiz kısaltma. Kısaltma 10 karakterden küçük olmalı.")

        haber.haber = request.POST['haber']
        if len(haber.haber) == 0:
            hatalar.append("Haber metni boş geçilemez.")

        haber.tarih = request.POST['tarih']

        if len(hatalar) == 0:
            haber.save()
            bilgi['haber'] = haber
            bilgi['yenikayit2'] = "True"
        else:
            bilgi['hatalistesi'] = hatalar

    sablon = loader.get_template('haber_duzenle.html')
    return HttpResponse(sablon.render(bilgi, request))
