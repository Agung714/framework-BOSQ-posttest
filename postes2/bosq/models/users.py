from django.db import models
# from bosq.models.karyawan import Karyawan

class Users(models.Model):
    # KARYAWAN = 1
    # ADMIN = 2
    # ROLE_CHOICES = (
    #     (KARYAWAN, 'Karyawan'),
    #     (ADMIN, 'Admin'),
    # )
    # username = models.CharField(max_length=150, unique=True)
    # password = models.CharField(max_length=128) # Panjang standar untuk password hash di Django


    OVERSEER = 1
    KARYAWAN = 2
    ROLE_CHOICES = (
        (OVERSEER, 'Overseer'),
        (KARYAWAN, 'Karyawan'),
    )

    username = models.CharField(max_length=150, unique=True)
    # Panjang standar untuk password hash di Django
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_CHOICES)

    def __str__(self):
        return self.username 