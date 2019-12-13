from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Lowongan(models.Model):
    jabatan = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    gaji_min = models.BigIntegerField(default=0)
    gaji_max = models.BigIntegerField(default=0)
    pengalaman = models.IntegerField(default=0)
    deskripsi = RichTextField()
    perusahaan = models.CharField(max_length=200)
    tanggal_publikasi = models.DateField(auto_now=True)
    link_image = models.CharField(max_length=1000)

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    tanggal_publikasi = models.DateField(auto_now=True)
    thumbnail = models.CharField(max_length=200)
    isi = RichTextField()

