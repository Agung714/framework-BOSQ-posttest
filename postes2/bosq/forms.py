from django import forms
from .models import Karyawan
class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        # fields = ['__all__']
        fields = ['nama', 'jabatan', 'email', 'gaji', 'username','password']
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        # fields = ['__all__']
        fields = ['nama', 'jabatan', 'email', 'gaji']
