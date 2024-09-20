from django.db import models
from bosq.models.karyawan import Karyawan

class Users(models.Model):
    # KARYAWAN = 1
    # ADMIN = 2
    # ROLE_CHOICES = (
    #     (KARYAWAN, 'Karyawan'),
    #     (ADMIN, 'Admin'),
    # )
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10) # Panjang standar untuk password hash di Django
    karyawan = models.OneToOneField(Karyawan,on_delete=models.CASCADE)
    # role = models.IntegerField(choices=ROLE_CHOICES) # 1 = Karyawan, 2 = Admin

    def __str__(self):
        return self.username