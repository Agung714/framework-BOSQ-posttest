from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from bosq.models.users import Users

class Karyawan(models.Model):
    # karyawan_id = models.CharField(primary_key=True,unique=True,max_length=4)
    karyawan_id = models.AutoField(primary_key=True,unique=True)
    nama = models.CharField(max_length=30)
    jabatan = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique=True) #unique klo sama ditolak
    gaji = models.PositiveIntegerField()
    username = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=13)

    
    # akun = models.ForeignKey(Users,on_delete=models.CASCADE)
    def __str__(self):
        return self.nama