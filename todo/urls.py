from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from todo import settings

from django.conf.urls import url, include
from notes.models import AIUser,Feeds,FeedsNlp,FeedsGroupedTopics
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AIUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AIUser
        fields = [ 'username', 'password']

# ViewSets define the view behavior.
class AIUserViewSet(viewsets.ModelViewSet):
    queryset = AIUser.objects.all()
    serializer_class = AIUserSerializer

# Serializers define the API representation.
class FeedsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feeds
        fields = [ 'feed_id', 'article_id','long_desc','short_desc','speciality','topics','title']

# ViewSets define the view behavior.
class FeedsViewSet(viewsets.ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer 
    
class FeedsNLPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedsNlp
        fields = [ 'feed_id', 'article_id','long_desc','short_desc','speciality','topics','title','simscore','queryfeedid']

# ViewSets define the view behavior.
class FeedsNLPViewSet(viewsets.ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer   
    

class FeedsGroupedTopicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedsGroupedTopics
        fields = [ 'feed_id', 'article_id_x','speciality_y','topics_y','title_y','simscore','queryfeedid']

# ViewSets define the view behavior.
class FeedsGroupedTopicsViewSet(viewsets.ModelViewSet):
    queryset = FeedsGroupedTopics.objects.all()
    serializer_class = FeedsGroupedTopicsSerializer     
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', AIUserViewSet)
router.register(r'feeds', FeedsViewSet)
router.register(r'feedsnlp', FeedsNLPViewSet)
router.register(r'feedsgrouped', FeedsGroupedTopicsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/',include('notes.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('',include(router.urls))
      # url(r'^api-auth/', include('rest_framework.urls'))
    #path('recruiter/',include('recruiter.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





