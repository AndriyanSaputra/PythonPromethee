from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Bobot
from management.bobot.forms import BobotForm
# Create your views here.


class ListBobotView(View):
	def get(self, request):

		template = 'bobot/index.html'

		form = BobotForm(request.POST or None)
		bobot = Bobot.objects.all()
		data = {
        'form_mode' : 'add',
        'form' : form,
		'bobot' : bobot,
		}
		return render(request, template, data)

class EditBobotView(View):
    template = 'bobot/index.html'

    def get(self, request, id):
        bobot = Bobot.objects.filter(id=id)
        if not bobot.exists():
            return redirect('bobot:view')
        bobot = bobot.first()
        initial = {

            'id': bobot.id,
            'pko' : bobot.pko,
            'disiplin' : bobot.disiplin,
            'kesehatn' : bobot.kesehatan,
            'psikotes'	: bobot.plomba,
            'petadua' : bobot.petadua,
        }

        form = BobotForm(initial=initial)
        bobot = Bobot.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'bobot' : bobot,
        }
        return render(request, self.template, data)



class UpdateBobotView(View):

    def post(self, request):
        
        template = "bobot/index.html"
        form = BobotForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            bobot = Bobot.objects.get(pk=id)
            bobot.pko = form.cleaned_data['pko']
            bobot.disiplin = form.cleaned_data['disiplin']
            bobot.kesehatan = form.cleaned_data['kesehatan']
            bobot.psikotes = form.cleaned_data['psikotes']
            bobot.petadua = form.cleaned_data['petadua']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            bobot.save(force_update=True)
            return redirect('bobot:view')
        else:
            bobot = bobot.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'bobot': bobot,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)