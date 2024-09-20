from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from bosq.models.users import Users

class Karyawan(models.Model):
    # id = models.IntegerField(primary_key=True)
    karyawanId = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=30)
    jabatan = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique=True) #unique klo sama ditolak
    gaji = models.CharField(max_length=9, unique=True)
    # user = models.OneToOneField(Users,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nama