from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from candidates.models import Faculty,Committee,CabinetPosition,PresidentialCabinet,Batch,SJBCandidate,SenateCandidate,ScCandidate,AcCandidate,PresidentialCabinetMember



admin.autodiscover()
admin.site.register(Faculty)
admin.site.register(Committee)
admin.site.register(CabinetPosition)
admin.site.register(PresidentialCabinet)
admin.site.register(SJBCandidate)
admin.site.register(Batch)
admin.site.register(SenateCandidate)
admin.site.register(ScCandidate)
admin.site.register(AcCandidate)
admin.site.register(PresidentialCabinetMember)






urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'election.views.home', name='home'),
    # url(r'^election/', include('election.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
     url(r'', include('django.contrib.staticfiles.urls')),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT } ),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'candidates.views.index'), 
    url(r'^nominate$', 'candidates.views.nominateindex'), 
    url(r'^nominate/sjb$', 'candidates.views.sjbindex'), 
    url(r'^nominate/sc$', 'candidates.views.scindex'), 
    url(r'^nominate/senate$', 'candidates.views.senateindex'), 
    url(r'^nominate/prc$', 'candidates.views.prindex'), 
    url(r'^view$', 'candidates.views.viewindex'), 
    url(r'^nominatesjb/$', 'candidates.views.nominateSJB'), 
    url(r'^nominatesenate/$', 'candidates.views.nominateSenate'), 
    url(r'^nominatesc/$', 'candidates.views.nominateSC'), 
    url(r'^newpc/$', 'candidates.views.newpc'), 
    url(r'^join/$', 'candidates.views.join'), 
    url(r'^show/$', 'candidates.views.show'), 


)
urlpatterns += staticfiles_urlpatterns()
