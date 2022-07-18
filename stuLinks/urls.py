from rest_framework_nested import routers
from stuLinks.views import StuLinksViewSet

router=routers.DefaultRouter()
router.register('stuLinks',viewset=StuLinksViewSet)
urlpatterns=router.urls

from  django.urls import include,path
from . import views
from . import api
app_name='stuLinks'


##api
path('api/list',api.stulinksapi,name='add_link'),