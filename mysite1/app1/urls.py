from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, tests

urlpatterns = [
    path('index/', views.index, name='index'),
    path('',views.login1, name='login1'),
    path('sign_up/',views.sign_up, name='sign_up'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('record_audio/<str:msg3>',tests.record_audio,name='record_audio'),
    path('play_audio/<int:id>',tests.play_audio,name='play_audio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)