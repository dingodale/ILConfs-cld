from django.conf.urls import patterns, include, url
#from event.views import HelloTemplate#agregar el class view! desde nuestras vistas
urlpatterns= patterns('djangoapps.userp.views',
	url(r'^login/$','login'),
	url(r'^petic/$','peticion'),
	url(r'^logprev/$','previo_login'),
	url(r'^events/$','eventos_user'),
	url(r'^newtic/$','nuevo_evento_user'),
	url(r'^enviatic/$','send_new_ticke'),


	url(r'^validtick/$','valid_ticke'),
	
	


	#url(r'^language/(?P<language>[a-z\-]+)/$','event.views.language'),
)
