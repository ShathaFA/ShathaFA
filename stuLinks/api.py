##views for api as js
from rest_framework.decorators import api_view

from .models import StuLinks
from rest_framework.response import Response
from .serializers import StuLinksSerializers


@api_view(['GET'])
def stulinksapi(request):
    all_links = StuLinks.object.all()
    data = StuLinksSerializers(all_links, many=True).data
    return Response({'data': data})
