from django.db import models
from django.contrib.auth.models import User
import time
import os
from orm import FileUploader

class Pekerja(models.Model):
    nip = models.IntegerField(default=0)
    nama_ptp = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False)
    alamat = models.TextField(blank=True, null=True)
    PRIA = 'Pria'
    WANITA = 'Wanita'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=8,
        choices=JK_CHOICES,
        default=PRIA,
    )
    agama = models.CharField(max_length=20, blank=True, null=True)
    KAWIN = 'Kawin'
    BELUM = 'Belum Kawin'
    ST_CHOICES  = (
        (KAWIN, 'Kawin'),
        (BELUM, 'Belum Kawin'),

    )
    status = models.CharField(
        max_length=15,
        choices=ST_CHOICES,
        default=KAWIN,
    )
    picture = models.ImageField(upload_to=FileUploader.file_profile,
                            null=True,
                            blank=True,
                            help_text="Upload Fotomu sebagai gambar profile",
                            default='pekerja/icon.png'
                            )


    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Pekerja'
        ordering = ['id']

class Pko(models.Model):
    pekerja = models.OneToOneField(Pekerja, on_delete=models.CASCADE,related_name='Pkos', blank=True, null=True) 
    jabatan = models.CharField(max_length=100)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'Pko'
        ordering = ['id']

class Disiplin(models.Model):
    pekerja = models.OneToOneField(Pekerja, on_delete=models.CASCADE, related_name='Disiplins', blank=True, null=True)  
    kehadiran = models.IntegerField(default=0)
    pelanggaran = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'Disiplin'
        ordering = ['id']

class Kesehatan(models.Model):
    pekerja = models.OneToOneField(Pekerja, on_delete=models.CASCADE, related_name='Kesehatans', blank=True, null=True) 
    SEHAT = 'Sehat'
    TIDAK = 'Tidak Sehat'
    JS_CHOICES  = (
        (SEHAT, 'Sehat'),
        (TIDAK, 'Tidak Sehat'),

    )
    status_kes = models.CharField(
        max_length=15,
        choices=JS_CHOICES,
        default=SEHAT,
    )
    nilai = models.IntegerField(default=0)
    

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'Kesehatan'
        ordering = ['id']

class Psikotes(models.Model):
    pekerja = models.OneToOneField(Pekerja, on_delete=models.CASCADE, related_name='Psikotess', blank=True, null=True) 
    intelegensi = models.IntegerField(default=0)
    kepribadian = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.pekerja.nama

    class Meta:
        db_table = 'Psikotes'
        ordering = ['id']
    
class Petadua(models.Model):
    pekerja = models.OneToOneField(Pekerja, on_delete=models.CASCADE, related_name='Petaduas', blank=True, null=True) 
    teori = models.IntegerField(default=0)
    praktek = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)
    
    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'Petadua'
        ordering = ['id']

class Pemilih(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nip = models.IntegerField(default=0)
    nama = models.CharField(max_length=100, blank=True, null=True)
    nama_ptp = models.CharField(max_length=100, blank=True, null=True)
    PRIA = 'Pria'
    WANITA = 'Wanita'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=8,
        choices=JK_CHOICES,
        default=PRIA,
    )
    picture = models.ImageField(upload_to=FileUploader.file_pemilih,
                        null=True,
                        blank=True,
                        help_text="Upload Fotomu sebagai gambar profile",
                        default='pemilih/icon.png'
                        )

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Pemilih'
        ordering = ['id']

class HakAkses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Login'
        ordering = ['id']

class Calon(models.Model):
    nama_calon = models.CharField(max_length=100, blank=True, null=True)
    visi = models.CharField(max_length=100, blank=True, null=True)
    misi = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to=FileUploader.file_calon,
                        null=True,
                        blank=True,
                        help_text="Upload Fotomu sebagai gambar profile",
                        default='calon/icon.png'
                        )
    
    score = models.IntegerField(default=0)


    def __str__(self):
        return self.nama_ketua

    class Meta:
        db_table = 'Calon'
        ordering = ['id']
