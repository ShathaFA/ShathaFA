
from django.shortcuts import render

# Create your views (function) here.
#request handller
#request--responce


#class or fun
from rest_framework.viewsets import ModelViewSet
from stuLinks.models import StuLinks
from  stuLinks.serializers import StuLinksSerializers

class StuLinksViewSet(ModelViewSet):
    serializer_class = StuLinksSerializers
    queryset = StuLinks.objects.all()
    http_method_names = ['get','post','patch','delete']