from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from donatory.models import DonorInformation
from donatory.forms import DonorInformationForm
from .filters import DonorInformationFilter


def donatory_home(request):
    template = 'donatory/donatory_home.html'
    donatory_qs = DonorInformation.objects.all()
    filter = DonorInformationFilter(request.GET, queryset=donatory_qs)
    return render(request, template, {'filter': filter,})

def donor_blood_form_edit(request,id):
    template = 'donatory/edit.html'
    qs = get_object_or_404(DonorInformation, id=id)
    if request.method == 'POST':
        form = DonorInformationForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = DonorInformationForm(instance=qs)
    return render(request, template, {'form': form, 'qs':qs })

def donor_blood_form_delete(request,id):
    template = 'donatory/confirm_delete.html'
    qs = get_object_or_404(DonorInformation, id=id)
    if request.method == "POST":
        qs.delete()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    return render(request, template, {'qs': qs})

def blood_form(request):
    template = 'donatory/blood_form.html'

    if request.method == 'POST':
        form = DonorInformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('donatory:home')
    else:
        form = DonorInformationForm()

    context = {'form': form,}
    return render(request, template, context)
