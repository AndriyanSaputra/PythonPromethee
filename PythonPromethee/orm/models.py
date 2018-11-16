from django.db import models
from django.contrib.auth.models import User
import time
import os

class Pekerja(models.Model):
    nip = models.IntegerField()
    nama_ptp = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False)
    alamat = models.TextField(blank=True, null=True)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    agama = models.CharField(max_length=20, blank=True, null=True)
    KAWIN = 'KW'
    BELUM = 'BK'
    ST_CHOICES  = (
        (KAWIN, 'Kawin'),
        (BELUM, 'Belum Kawin'),

    )
    status = models.CharField(
        max_length=2,
        choices=ST_CHOICES,
        default=KAWIN,
    )

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Pekerja'
        ordering = ['id']

class Pko(models.Model):
    jabatan = models.CharField(max_length=100)
    nilai = models.IntegerField(default=0)
    pekerja = models.OneToOneField(Pekerja, 
                                    on_delete=models.CASCADE, 
                                        related_name='Pkos', blank=True, null=True) 

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'pko'
        ordering = ['id']

class Disiplin(models.Model):
    kehadiran = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)
    pelanggaran = models.IntegerField(default=0)
    pekerja = models.OneToOneField(Pekerja, 
                                on_delete=models.CASCADE, 
                                    related_name='Displins', blank=True, null=True)  

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'Disiplin'
        ordering = ['id']

class Kesehatan(models.Model):
    SEHAT = 'SH'
    TIDAK = 'TS'
    JS_CHOICES  = (
        (SEHAT, 'Sehat'),
        (TIDAK, 'Tidak Sehat'),

    )
    status = models.CharField(
        max_length=2,
        choices=JS_CHOICES,
        default=SEHAT,
    )
    nilai = models.IntegerField(default=0)
    pekerja = models.OneToOneField(Pekerja, 
                                on_delete=models.CASCADE, 
                                    related_name='Kesehatans', blank=True, null=True) 
    

    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'jasmani'
        ordering = ['id']

class Psikotes(models.Model):
    intelegensi = models.CharField(max_length=100)
    kepribadian = models.CharField(max_length=50)
    nilai = models.IntegerField(default=0)
    pekerja = models.OneToOneField(Pekerja, 
                                on_delete=models.CASCADE, 
                                    related_name='Psikotess', blank=True, null=True) 

    def __str__(self):
        return self.pekerja.nama

    class Meta:
        db_table = 'intelegensi'
        ordering = ['id']
    
class Petadua(models.Model):
    teori = models.CharField(max_length=50)
    praktek = models.CharField(max_length=50)
    nilai = models.IntegerField(default=0)
    pekerja = models.OneToOneField(Pekerja, 
                                on_delete=models.CASCADE, 
                                    related_name='Petaduas', blank=True, null=True) 
    def __str__(self):
        return self.pekerja.nama

    class Meta :
        db_table = 'teori'
        ordering = ['id']
    



