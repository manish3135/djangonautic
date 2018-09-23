from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/',views.about,name='about'),
    url(r'^$',views.homepage,name='homepage'),
    url(r'^accounts/',include('accounts.urls',namespace="login")),
    url(r'^articles/',include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
