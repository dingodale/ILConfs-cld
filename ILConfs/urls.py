﻿#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djangoapps.inev.api import QuestionResource
from djangoapps.moderat.api import QuestResource, ChoiceResource

question_resource = QuestionResource()
quest_resource = QuestResource()
choice_resource = ChoiceResource()
 

urlpatterns = patterns('',
	(r'^$', TemplateView.as_view(template_name="home.html")),
	#(r'^/$', include('djangoapps.event.urls')),
	(r'^events/$', include('djangoapps.event.urls')),
    (r'^home/', include('djangoapps.cms.urls')),
    (r'^json/', include('djangoapps.event.urls')),
    (r'^adm/', include('djangoapps.admn.urls')),
    (r'^moder/', include('djangoapps.moderat.urls')),
    (r'^interactiv/', include('djangoapps.inev.urls')),
    (r'^api/', include(question_resource.urls)),
    (r'^jsoncho/', include(choice_resource.urls)),
    (r'^user/', include('djangoapps.userp.urls')),
    #url(r'', include('gcm.urls'),
    # Examples:
    # url(r'^$', 'ILConfs.views.home', name='home'),
    # url(r'^ILConfs/', include('ILConfs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^secret/admin/', include(admin.site.urls)),
    # basic resources without authentication
    url(r'', include('gcm.urls')),
)
