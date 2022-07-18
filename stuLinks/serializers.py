##data sjango to js

from rest_framework import serializers
from .models import StuLinks

class StuLinksSerializers(serializers.ModelSerializer):
    class Meta:
        model=StuLinks
        fields=['link_name', 'link']
