from django.conf.urls import url

from users.views import CreateUser, CreateContact, CheckImage

urlpatterns = [
    url(r'^create/', CreateUser.as_view()),
    url(r'^check-image/', CheckImage.as_view()),
    url(r'^all/', CreateContact.as_view())
    ]