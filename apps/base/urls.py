from django.urls import path
from apps.base.views import index, contact_form




urlpatterns = [
    path('', index, name = "index-page"),
    path('contact-form/', contact_form, name="contact_form"),

]