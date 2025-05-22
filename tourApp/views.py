from django.shortcuts import get_object_or_404, redirect, render
from .models import TourPackage
from .forms import TourPackageForm

def home(request):
    packages = TourPackage.objects.all()
    return render(request, 'tourApp/home.html', {'packages': packages})

def tour_package_list(request):
    packages = TourPackage.objects.prefetch_related('itineraries').all()
    return render(request, 'tour_package_list.html', {'packages': packages})  # updated path

def view_packages(request):
    packages = TourPackage.objects.all()
    return render(request, 'tourApp/package_list.html', {'packages': packages})

def add_package(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = TourPackageForm()
    return render(request, 'tourApp/add_package.html', {'form': form})

def edit_package(request, id):
    package = get_object_or_404(TourPackage, id=id)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('view_packages')
    else:
        form = TourPackageForm(instance=package)
    return render(request, 'tourApp/edit_package.html', {'form': form})

def delete_package(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('package_list')
    return render(request, 'tourApp/delete_package.html', {'package': package})
