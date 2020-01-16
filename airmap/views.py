from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import Post, Monitor
from django.views.decorators.csrf import csrf_exempt
from djgeojson.fields import PointField

default_geom = {
  "type":"Point",
  "coordinates":[
    -1.5058208465576172,
    48.15301133231325
  ]
}

# Create your views here.

def IndexView(request):
    template_name = 'airmap/index.html'
    return render(request, template_name)

@csrf_exempt
def update_reading(request):
    posts = Post.objects.all()
    response_data = {}

    # print(Monitor.objects.all().last().id)

    if request.method == 'POST':
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
            Monitor.objects.create(
                geom=PointField(default=default_geom),
                latest_reading=20,
                latest_reading_datetime=datetime.now()
            )

    return render(request, 'airmap/update_reading.html', {'posts':posts})
