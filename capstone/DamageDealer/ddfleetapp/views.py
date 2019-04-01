from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Card, Fleet, CardAmount
from .forms import CardNumber

class DmgDealerHome(TemplateView):
    template_name = "ddfleetapp/home.html"

class DmgDealerCreateFleet(CreateView):
    model = Fleet
    template_name = 'ddfleetapp/newfleet.html'
    fields = ['admiral_name', 'list_name', 'faction']

class DmgDealerFleetDetails(DetailView):
    model = CardAmount
    template_name = 'ddfleetapp/fleetdetails.html'

    def get_context_data(self, **kwargs):
        thisfleet = CardAmount.objects.filter(fleet=self.kwargs['pk'])
        fleet = get_object_or_404(Fleet, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['fleet'] = fleet
        context['card_ship'] = thisfleet.filter(card__card_type='ship')
        context['card_squadron'] = thisfleet.filter(card__card_type='squadron')
        context['card_upgrade'] = thisfleet.filter(card__card_type='upgrade')
        context['card_objective'] = thisfleet.filter(card__card_type='objective')
        return context

class DmgDealerPrintDetails(DetailView):
    model = CardAmount
    template_name = 'ddfleetapp/print.html'

    def get_context_data(self, **kwargs):
        thisfleet = CardAmount.objects.filter(fleet=self.kwargs['pk'])
        fleet = get_object_or_404(Fleet, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['fleet'] = fleet
        context['card_ship'] = thisfleet.filter(card__card_type='ship')
        context['card_squadron'] = thisfleet.filter(card__card_type='squadron')
        context['card_upgrade'] = thisfleet.filter(card__card_type='upgrade')
        context['card_objective'] = thisfleet.filter(card__card_type='objective')
        return context

class DmgDealerFleetList(ListView):
    model = Fleet
    template_name = 'ddfleetapp/listOfFleets.html'

    def get_queryset(self):
        return Fleet.objects.order_by('list_name')
    
class DmgDealerDeleteFleet(DeleteView):
    model = Fleet
    template_name = 'ddfleetapp/deletefleet.html'
    success_url = reverse_lazy('dd_list')

class DmgDealerEditFleet(UpdateView):
    model = Fleet
    template_name = 'ddfleetapp/editfleet.html'
    fields = ['admiral_name', 'list_name']


def add_cards(request, pk):
    thisfleet = get_object_or_404(Fleet, pk=pk)
    if thisfleet.faction == 'Rebel':
        shipslist = Card.objects.filter(card_type="ship").exclude(faction='Imperial').order_by('name')
        squadslist = Card.objects.filter(card_type="squadron").exclude(faction='Imperial').order_by('name')
        commanderlist = Card.objects.filter(upgrade_type="commander").exclude(faction='Imperial').order_by('name')
        defenselist = Card.objects.filter(upgrade_type="defensive retrofit").exclude(faction='Imperial').order_by('name')
        experimentlist = Card.objects.filter(upgrade_type="experimental retrofit").exclude(faction='Imperial').order_by('name')
        fleetcommlist = Card.objects.filter(upgrade_type="fleet command").exclude(faction='Imperial').order_by('name')
        fleetsupplist = Card.objects.filter(upgrade_type="fleet support").exclude(faction='Imperial').order_by('name')
        ionlist = Card.objects.filter(upgrade_type="ion cannon").exclude(faction='Imperial').order_by('name')
        offenselist = Card.objects.filter(upgrade_type="offensive retrofit").exclude(faction='Imperial').order_by('name')
        officerlist = Card.objects.filter(upgrade_type="officer").exclude(faction='Imperial').order_by('name')
        ordnancelist = Card.objects.filter(upgrade_type="ordnance").exclude(faction='Imperial').order_by('name')
        supportlist = Card.objects.filter(upgrade_type="support team").exclude(faction='Imperial').order_by('name')
        titlelist = Card.objects.filter(upgrade_type__endswith="title").exclude(faction='Imperial').order_by('name')
        turbolist = Card.objects.filter(upgrade_type__endswith="turbolaser").exclude(faction='Imperial').order_by('name')
        weapteamlist = Card.objects.filter(upgrade_type__endswith="weapons team").exclude(faction='Imperial').order_by('name')
        boardlist = Card.objects.filter(upgrade_type__endswith="boarding team").exclude(faction='Imperial').order_by('name')
        objectiveslist = Card.objects.filter(card_type="objective").exclude(faction='Imperial').order_by('name')
    else:
        shipslist = Card.objects.filter(card_type="ship").exclude(faction='Rebel').order_by('name')
        squadslist = Card.objects.filter(card_type="squadron").exclude(faction='Rebel').order_by('name')
        commanderlist = Card.objects.filter(upgrade_type="commander").exclude(faction='Rebel').order_by('name')
        defenselist = Card.objects.filter(upgrade_type="defensive retrofit").exclude(faction='Rebel').order_by('name')
        experimentlist = Card.objects.filter(upgrade_type="experimental retrofit").exclude(faction='Rebel').order_by('name')
        fleetcommlist = Card.objects.filter(upgrade_type="fleet command").exclude(faction='Rebel').order_by('name')
        fleetsupplist = Card.objects.filter(upgrade_type="fleet support").exclude(faction='Rebel').order_by('name')
        ionlist = Card.objects.filter(upgrade_type="ion cannon").exclude(faction='Rebel').order_by('name')
        offenselist = Card.objects.filter(upgrade_type="offensive retrofit").exclude(faction='Rebel').order_by('name')
        officerlist = Card.objects.filter(upgrade_type="officer").exclude(faction='Rebel').order_by('name')
        ordnancelist = Card.objects.filter(upgrade_type="ordnance").exclude(faction='Rebel').order_by('name')
        supportlist = Card.objects.filter(upgrade_type="support team").exclude(faction='Rebel').order_by('name')
        titlelist = Card.objects.filter(upgrade_type__endswith="title").exclude(faction='Rebel').order_by('name')
        turbolist = Card.objects.filter(upgrade_type__endswith="turbolaser").exclude(faction='Rebel').order_by('name')
        weapteamlist = Card.objects.filter(upgrade_type__endswith="weapons team").exclude(faction='Rebel').order_by('name')
        boardlist = Card.objects.filter(upgrade_type__endswith="boarding team").exclude(faction='Rebel').order_by('name')
        objectiveslist = Card.objects.filter(card_type="objective").exclude(faction='Rebel').order_by('name')
    context = {'thisfleet': thisfleet, 
               'shipslist': shipslist, 
               'squadslist': squadslist, 
               'commanderlist': commanderlist, 
               'defenselist': defenselist, 
               'experimentlist': experimentlist, 
               'fleetcommlist': fleetcommlist, 
               'fleetsupplist': fleetsupplist, 
               'ionlist': ionlist, 
               'offenselist': offenselist, 
               'officerlist': officerlist, 
               'ordnancelist': ordnancelist, 
               'supportlist': supportlist, 
               'titlelist': titlelist, 
               'turbolist': turbolist, 
               'weapteamlist': weapteamlist, 
               'boardlist': boardlist, 
               'objectiveslist': objectiveslist}
    return render(request, 'ddfleetapp/addcard.html' , context)

@csrf_exempt
def postdata(request, pk):
    received_json_data = json.loads(request.body)
    print(received_json_data)
    fleet = received_json_data['fleet']
    card = received_json_data['card']
    amount = received_json_data['amount']
    newcard = CardAmount(
        fleet_id = fleet,
        card_id = card,
        amount = amount,
    )
    newcard.save()
    return HttpResponse('OK')


class DmgDealerCardAmount(UpdateView):
    model = CardAmount
    template_name = 'ddfleetapp/cardnum.html'
    fields = ['amount']
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dd_detail', args=(self.object.fleet.id,))

    # def get_context_data(self, **kwargs):
    #     thisfleet = CardAmount.objects.filter(fleet=self.kwargs['pk'])
    #     fleet = get_object_or_404(Fleet, pk=self.kwargs['pk'])
    #     context = super().get_context_data(**kwargs)
    #     context['fleet'] = fleet
    #     return context


class DmgDealerDeleteCard(DeleteView):
    model = CardAmount
    template_name = 'ddfleetapp/deletecard.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dd_detail', args=(self.object.fleet.id,))

