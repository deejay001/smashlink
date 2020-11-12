from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('home', views.uhome, name='uhome'),
    path('explore', views.explore, name='explore'),
    path('add_post', views.add_post, name='add_post'),
    path('<title>', views.post_detail, name='udetail'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
