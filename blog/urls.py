from django.conf import settings
from django.conf.urls import patterns, include, url
from . import views
# make sure you add ** (r'^blog/', include('blog.urls')), ** to your project's main urls.py
urlpatterns = [
    url(r'^$', views.all_posts, name='posts'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.single_post, name='post'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.category_archive, name='category'),
]