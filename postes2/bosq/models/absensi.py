from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from bosq.models.karyawan import Karyawan

class Absensi(models.Model):
    HADIR = 1
    SAKIT = 2
    IZIN = 3
    ROLE_CHOICES = (
        #  'Hadir',
        #  'Sakit',
        # 'Izin',
        (HADIR, 'Hadir'),
        (SAKIT, 'Sakit'),
        (IZIN, 'Izin'),
    )
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    tanggal = models.DateTimeField(default=timezone.now) # Absen 1x 1 hari
    # statusKehadiran = models.CharField(max_length=13, )
    statusKehadiran = models.IntegerField(choices=ROLE_CHOICES) # 1 = Karyawan, 2 = Admin

    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.karyawan}-{self.tanggal.strftime('%Y-%m-%d')}"
        # return self.id
