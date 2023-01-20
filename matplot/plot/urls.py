from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('barchart',views.barchart,name='barchart'),
    path('',views.piechart,name='piechart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)