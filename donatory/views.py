from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from donatory.models import DonorInformation
from donatory.forms import DonorInformationForm
from .filters import DonorInformationFilter
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> b175e0180d7a4f4ae5ff8ce856f00761d98e86c0

def donatory_home(request):
    template = 'donatory/donatory_home.html'
    donatory_qs = DonorInformation.objects.all()
    filter = DonorInformationFilter(request.GET, queryset=donatory_qs)
    return render(request, template, {'filter': filter,})

@login_required
def donor_blood_form_edit(request,id):
    template = 'donatory/edit.html'
    qs = get_object_or_404(DonorInformation, id=id, user=request.user)
    if request.method == 'POST':
        form = DonorInformationForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = DonorInformationForm(instance=qs)
    return render(request, template, {'form': form, 'qs':qs })

<<<<<<< HEAD
    
=======
>>>>>>> b175e0180d7a4f4ae5ff8ce856f00761d98e86c0
@login_required
def donor_blood_form_delete(request,id):
    template = 'donatory/confirm_delete.html'
    qs = get_object_or_404(DonorInformation, id=id, user=request.user)
    if request.method == "POST":
        qs.delete()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    return render(request, template, {'qs': qs})


@login_required
def blood_form(request):
    template = 'donatory/blood_form.html'

    if request.method == 'POST':
        form = DonorInformationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            form = form.save(commit=False) # not yet save in database
            form.user = request.user # select user
            form.save()
            return redirect('donatory:home')
    else:
        form = DonorInformationForm()
        

    context = {'form': form,}
    return render(request, template, context)
