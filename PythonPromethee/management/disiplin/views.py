from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Disiplin,Pekerja
from management.disiplin.forms import DisiplinForm
# from django.contrib.auth.models import User


# Create your views here.



class ListDisiplinView(View):
	def get(self, request):

		template = 'disiplin/index.html'

		form = DisiplinForm(request.POST or None)
		disiplin = Disiplin.objects.all()
		data = {
        'form_mode' : 'add',
        'form' : form,
		'pekerja' : Pekerja.objects.all(),
		'disiplin' : disiplin,
		}
		return render(request, template, data)


class SavedisiplinView(View):
    def post(self, request):
        template = 'disiplin/index.html'
        form = DisiplinForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            Disiplin = Disiplin()
            Disiplin.pekerja = form.cleaned_data['pekerja']
            disiplin.jenjang = form.cleaned_data['jenjang']
            disiplin.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            disiplin.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            disiplin.save()
            return redirect('disiplin:view')
        else:
            disiplin = Disiplin.objects.all()
            data = {

                'form': form,
                'disiplin': disiplin,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditDisiplinView(View):
    template = 'disiplin/edit.html'

    def get(self, request, id):
        disiplin = disiplin.objects.filter(id=id)
        if not disiplin.exists():
            return redirect('disiplin:view')
        disiplin = disiplin.first()
        initial = {

            'id': disiplin.id,
            'jenjang': disiplin.jenjang,
            'mata_pelajaran': disiplin.mata_pelajaran,
            'nilai': disiplin.nilai,
            'pekerja': disiplin.pekerja,
        }

        form = DisiplinForm(initial=initial)
        disiplin = Disiplin.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'disiplin' : disiplin,
        }
        return render(request, self.template, data)



class UpdateDisiplinView(View):

    def post(self, request):
        
        template = "disiplin/index.html"
        form = DisiplinForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            disiplin = disiplin.objects.get(pk=id)
            disiplin.jenjang = form.cleaned_data['jenjang']
            disiplin.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            disiplin.nilai = form.cleaned_data['nilai']
            disiplin.pekerja = form.cleaned_data['pekerja']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            disiplin.save(force_update=True)
            return redirect('disiplin:view')
        else:
            disiplin = disiplin.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'disiplin': disiplin,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            # return render(request, template, data)
            return HttpResponse(form.errors)

class HapusDisiplinView(View):

    def get(self, request, id):
        disiplin = disiplin.objects.filter(id=id)
        if disiplin.exists():
            disiplin.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
return redirect('disiplin:view')
        else:
messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 