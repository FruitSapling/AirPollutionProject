from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from . import views
from . models import Monitor
from airmap.views import update_reading, create_monitor

app_name = 'airmap'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='airmap/index.html'), name='home'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=Monitor,
                                             properties=('latest_reading', 'latitude', 'longitude')),
                                             name='data'),
    path('update', update_reading, name="update"),
    path('create', create_monitor, name="create")
    # path('', views.IndexView, name='home'),
    # url(r'^data/$', GeoJSONLayerView.as_view(model=Monitor), name='data'),
]
