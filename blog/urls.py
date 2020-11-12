from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('category/<name>', views.cat_view, name='cat'),
    path('blog/<title>', views.blog_detail, name='detail'),
]


urlpatterns += [
                   # ... the rest of your URLconf goes here ...
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
