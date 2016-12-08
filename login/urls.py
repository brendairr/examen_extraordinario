from django.conf.urls import url
from views import login
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    #url(r'^$', login_mentor, name="login_mentor"),
    url(r'^$', login, {'template_name':'login.html'}, name="login"),
    url(r'^cerrar/$', logout_then_login, name="logout"),

]
