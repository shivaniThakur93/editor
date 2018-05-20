from django.conf.urls import url
from .views import (
    edit_page,
    edit_page_bonus,
	)

urlpatterns = [
    url(r'^$', edit_page, name='edit'),
    url(r'^materialize/$', edit_page_bonus, name='edit_bonus'),
]