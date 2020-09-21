from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from mainpage import views


urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^news/', include("news.urls", namespace='news')),

    url(r'^solutions/scna/', views.scna, name='scna'),
    url(r'^solutions/cna/', views.cna, name='cna'),
    url(r'^solutions/d-key/', views.dkey, name='dkey'),
    url(r'^solutions/d-keysd/', views.dkeysd, name='dkeysd'),
    url(r'^solutions/itvpn/', views.itvpn, name='itvpn'),

    url(r'^laboratory/attestation/', views.attestation, name='attestation'),
    url(r'^laboratory/sertification/', views.sertification, name='sertification'),
    url(r'^laboratory/ekspertiza/', views.ekspertiza, name='ekspertiza'),
    url(r'^laboratory/oblast-akkreditacii/', views.oblast, name='oblast-akkreditacii'),

    url(r'^company/audit-ib/', views.audit, name='audit-ib'),
    url(r'^company/soprovozhdenie-po/', views.soprovozhdenie, name='soprovozhdenie-po'),
    url(r'^company/razrabotka-programmnogo-obespecheniya/', views.razrabotka, name='razrabotka-programmnogo-obespecheniya'),
    url(r'^company/o-kompanii/', views.company, name='o-kompanii'),

    url(r'^ru/company/', views.company, name='o-kompanii'),

    url(r'^vacancies/', views.vacancies, name='vacancies'),
    url(r'^sitemap.xml', views.sitemap, name='sitemap'),
    url(r'^robots.txt', views.robots, name='robots'),
    url(r'^turbo.rss', views.turbo, name='turbo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)