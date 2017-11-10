from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('clinic.urls')),]
