from django.urls import path,include
from . import views
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('',views.getnotes,name='getnotes'),
    path('note/create',views.createnote, name='create_new_note'),
    path('note/<int:pk>',views.note,name='single_note'),
    path('note/<int:pk>/update',views.noteupdate,name='update_note'),
    path('note/<int:pk>/delete',views.deletenote,name='delete_note'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# router = DefaultRouter()
# router.register('construction',views.constructionviewset, basename='construct')
# router.register('feature',views.featureviewset,basename='featur')
# router.register('contact',views.contactviewset,basename='contacts')
# urlpatterns += router.urls
