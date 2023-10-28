from django.urls import path
from .views import *

urlpatterns = [
    path("index/", index_view, name='index_url'),
    path("", signin_view, name='login_url'),
    path("signup/", signup_view, name='signup_url'),
    path("loguot/", logout_view, name='loguot_url'),
    path("block/", block_view, name='block_url'),
    path("portfolio/", portfolio_view, name='portfolio_url'),
    path("single/", single_view, name='single_url'),
    path("my_profile/", my_profile_view, name='my_profile_url'),
    path("create-subject/", create_subject_view, name="create_subject_url")
]