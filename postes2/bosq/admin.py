from django.contrib import admin
from .models.absensi import Absensi
from .models.karyawan import Karyawan
from .models.users import Users
from .models.overseer import Overseer
from django.contrib.auth.hashers import make_password # Untuk hashing password

# class KaryawanAdmin(admin.ModelAdmin):
#     # list_display = ('karyawan_id', 'nama', 'jabatan', 'email')
#     # exclude = ['karyawan_id',]  
#     # exclude = ('karyawan_id',)  
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)

#         user, created = Users.objects.get_or_create(username=obj.email, defaults={ # Pastikan ini model Users kustom
#         'password': make_password('default_password'),
#         })

#         if not created: 
#             user.save()

class OverseerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'password')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        user, created = Users.objects.get_or_create(username=obj.username, defaults= {
            'password': make_password('default_password'),
            'role':Users.OVERSEER
        })
        
        if not created:
            user.role = Users.OVERSEER 
            user.save()

class KaryawanAkun(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'email')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        user, created = Users.objects.get_or_create(username=obj.username, defaults= {
            'password': make_password('default_password'),
            'role':Users.OVERSEER
        })
        
        if not created:
            user.role = Users.KARYAWAN 
            user.save()

admin.site.register(Overseer, OverseerAdmin)

admin.site.register(Karyawan,KaryawanAkun)
# admin.site.register(Karyawan)
admin.site.register(Absensi)
admin.site.register(Users)