from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

#   url(r'^$', hello.views.index, name='index'),
 #   url(r'^db', hello.views.db, name='db'),
  #  path('admin/', admin.site.urls),
 


urlpatterns = [
    url(r'^port/', include('port.urls')),

]

