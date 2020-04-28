from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Monitor
from datetime import datetime
from copy import deepcopy
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms

def IndexView(request):
    template_name = 'airmap/index.html'
    return render(request, template_name)

@csrf_exempt
def create_monitor(request):
    print("request look;")
    print(request)
    # If request has longitude, latitude and mac_address headers, then it is a valid request
    if (request.POST.get('latitude')
            and request.POST.get('longitude')
            and request.POST.get('mac_address')):

        form = CreateRequestValidationForm(request.POST, request.FILES)
        if not form.is_valid():
            print("Rejected because invalid form")
            return HttpResponseBadRequest(None)

        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        mac_address = request.POST.get('mac_address')

        # Make a deep copy of a monitor to edit, so as to not change an existing monitor
        new_geom = deepcopy(Monitor.objects.all().last().geom)

        new_geom['coordinates'][0] = longitude
        new_geom['coordinates'][1] = latitude

        Monitor.objects.create(
            mac_address=mac_address,
            latest_reading=0,
            latest_reading_datetime=datetime.now(),
            geom=new_geom
        )
        return HttpResponse(None)
    else:
        # Invalid request
        return HttpResponseBadRequest(None)

@csrf_exempt
def update_reading(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('mac_address'): # If we received post data from a known existing monitor
            form = UpdateRequestValidationForm(request.POST, request.FILES)
            if not form.is_valid():
                print("Rejected because invalid form")
                return HttpResponseBadRequest(None)
            else: # Valid form
                mac_address = request.POST['mac_address']
                latest_reading = request.POST['latest_reading']
                latest_reading_pm = request.POST['latest_reading_pm']
                latest_reading_datetime = datetime.now()

                with open("results.txt", "a") as myfile:
                    myfile.write(latest_reading_datetime.strftime("%H:%M:%S") + "," + str(latest_reading) + "," + str(latest_reading_pm) + "\n")
                    myfile.close()

                # Get the monitor object from models which corresponds to the received JSON
                monitor = Monitor.objects.get(mac_address=mac_address)

                # Update the name value
                monitor.latest_reading = latest_reading
                monitor.latest_reading_datetime = latest_reading_datetime

                # Call save() with the update_fields arg and a list of record fields to update selectively
                monitor.save(update_fields=['latest_reading', 'latest_reading_datetime'])

        else: # Not a recognised request
            return HttpResponseBadRequest(None)

    return HttpResponse(None) # Return an empty HttpResponse.

class CreateRequestValidationForm(forms.Form):
    mac_address = forms.CharField()
    latitude = forms.FloatField()
    longitude = forms.FloatField()

class UpdateRequestValidationForm(forms.Form):
    mac_address = forms.CharField()
    latest_reading = forms.IntegerField()
    latest_reading_pm = forms.IntegerField()