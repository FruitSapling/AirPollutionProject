from django.views.decorators.csrf import csrf_exempt
from djgeojson.fields import PointField
from django.shortcuts import render
from .models import Post, Monitor
from datetime import datetime
from copy import deepcopy
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

# Create your views here.

def IndexView(request):
    template_name = 'airmap/index.html'
    return render(request, template_name)

@csrf_exempt
def update_reading(request):
    posts = Post.objects.all()
    response_data = {}

    if request.method == 'POST':
        print (request.POST)
        if request.POST.get('monitor_id'): # If we received post data from a known existing monitor
            monitor_id = request.POST['monitor_id']
            latest_reading = request.POST['latest_reading']
            latest_reading_datetime = datetime.now()

            # Get the monitor object from models which corresponds to the received JSON
            monitor = Monitor.objects.get(id=monitor_id)

            # Update the name value
            monitor.latest_reading = latest_reading
            monitor.latest_reading_datetime = latest_reading_datetime

            # Call save() with the update_fields arg and a list of record fields to update selectively
            monitor.save(update_fields=['latest_reading', 'latest_reading_datetime'])

        elif request.POST.get('latitude'): # If we received post data with 'latitude' indicating a new monitor
            longitude = request.POST.get('longitude')
            latitude = request.POST.get('latitude')

            # Make a deep copy so as to not change an existing monitor
            new_geom = deepcopy(Monitor.objects.all().last().geom)

            new_geom['coordinates'][0] = longitude
            new_geom['coordinates'][1] = latitude

            Monitor.objects.create(
                latest_reading=0,
                latest_reading_datetime=datetime.now(),
                geom=new_geom
                # geom=PointField(default=default_geom)
            )

        else: # Not a recognised request
            return HttpResponseBadRequest

    return HttpResponse(None) # Return an empty HttpResponse.
    # return render(request, 'airmap/update_reading.html', {'posts':posts})






















