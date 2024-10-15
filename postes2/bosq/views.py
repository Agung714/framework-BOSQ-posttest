from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Karyawan

from django.contrib import messages
from .forms import KaryawanForm , UpdateForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')
def login(request):
    return render(request, 'homepage/login.html')
def dashboard(request):
    return render(request, 'homepage/dashboard.html') 

def karyawan_index(request):
    karyawans = Karyawan.objects.all()
    return render(request, 'karyawan/index.html', {'karyawan': karyawans})


def karyawan_create(request):
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        if form.is_valid():
            form.save() # Simpan data mahasiswa ke database
            messages.success(request, 'Karyawan berhasil dibuat!') # Pesan sukses
            return redirect('karyawan_index') # Redirect ke halaman index mahasiswa
    else:
        form = KaryawanForm()
    return render(request, 'karyawan/create.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Karyawan

# UPDATE Mahasiswa
def karyawan_update(request, karyawan_id):
    karyawan = get_object_or_404(Karyawan, karyawan_id=karyawan_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=karyawan)
        # form = KaryawanForm(request.POST, instance=karyawan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data karyawan berhasil diubah!')
            return redirect('karyawan_index')
    else:
        # form = KaryawanForm(instance=karyawan)
        form = UpdateForm(instance=karyawan)
    return render(request, 'karyawan/update.html', {'form': form, 'karyawan': karyawan})
from django.http import JsonResponse

# DELETE Mahasiswa
def karyawan_delete(request, karyawan_id):
    karyawan = get_object_or_404(Karyawan, karyawan_id=karyawan_id)
    karyawan.delete()
    messages.success(request, 'Data karyawan berhasil dihapus')
    return JsonResponse({'success': True})



from django.db.models import Q
def karyawan_index(request):
    query = request.GET.get('q')
    karyawan = Karyawan.objects.all()
    if query:
        karyawan = Karyawan.objects.filter(
            Q(nama__icontains=query) |
            Q(jabatan__icontains=query) |
            Q(email__icontains=query) |
            Q(gaji__icontains=query)
    )
    else:
        karyawan = Karyawan.objects.all()
    return render(request, 'karyawan/index.html', {'karyawan': karyawan, 'query': query})