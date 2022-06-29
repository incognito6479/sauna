from .models import SaunaPriceTypes
from client.models import Client
from sauna.models import Sauna


def count_sauna_price(self, form, action):
    if action == 'add':
        form.instance.client = Client.objects.get(id=int(self.request.POST.get('client_id')))
        form.instance.people_count = int(self.request.POST.get('people_count'))
        form.instance.sauna = Sauna.objects.get(id=int(self.request.POST.get('sauna')))
    form.instance.start_time = str(self.request.POST.get('start'))
    form.instance.end_time = str(self.request.POST.get('end'))
    form.instance.user = self.request.user
    sauna = form.instance.sauna
    sauna_price_type = SaunaPriceTypes.objects.filter(sauna=sauna)
    sauna_hour_price = 0
    for j in sauna_price_type:
        if j.min_people <= form.instance.people_count <= j.max_people:
            sauna_hour_price += j.price
    form.instance.sauna_hour_price = sauna_hour_price
    return form
