from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Artikel, Lowongan
# Create your views here.
def beranda(request):
    artikel = Artikel.objects.all().order_by('-id')[0]
    lowongan = Lowongan.objects.all()
    info = {
        'flag':1,
        'lowongan':lowongan[::-1],
        'artikel':artikel,
    }
    return render(request, 'jobsdbApp/beranda.html', info)

def event(request):
    info = {
        'flag':3
    }
    return render(request, 'jobsdbApp/event.html', info)

def artikel(request, artikel_id):
    artikel = Artikel.objects.get(pk=artikel_id)
    articles = Artikel.objects.all().exclude(pk=artikel_id)
    info = {
        'artikel':artikel,
        'articles':articles
    }
    return render(request, 'jobsdbApp/artikel.html', info)

def resource(request):
    artikel = Artikel.objects.all().order_by('-id')[1::]
    newest_artikel = Artikel.objects.all().order_by('-id')[0]
    info = {
        'artikel':artikel[::-1],
        'newest_artikel':newest_artikel
    }
    return render(request, 'jobsdbApp/resource.html', info)

def searchResult(request):
    lowongan = Lowongan.objects.all()
    gaji_filter = Lowongan.objects.filter(gaji_max__gte=request.POST['gaji'], gaji_min__lte=request.POST['gaji']) | Lowongan.objects.filter(gaji_max__gte=request.POST['gaji'], gaji_min__gte=request.POST['gaji'])
    pengalaman_filter = Lowongan.objects.filter(pengalaman__lte=request.POST['pengalaman'])
    lokasi_filter = Lowongan.objects.filter(lokasi=request.POST['lokasi'])
    info = {
        'lowongan':lowongan,
        # 'gaji_filter':gaji,
        # 'pengalaman_filter':pengalaman,
        # 'lokasi_filter':lokasi
    }
    return render(request, 'jobsdbApp/search-result.html', info)

def detailLowongan(request, lowongan_id):
    lowongan = Lowongan.objects.get(pk=lowongan_id)
    info = {
        'lowongan':lowongan
    }
    return render(request, 'jobsdbApp/detail-lowongan.html', info)

def download(request):
    return render(request, 'jobsdbApp/download.html')