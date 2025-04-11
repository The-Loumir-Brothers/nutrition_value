from django.urls import path, include  # include() will include another url pattern

from . import views
from. import foods

urlpatterns = [
    # path is empty to connect it to the base URL of the website, calling views function
    path("", views.home, name='home'),
    # Link to another set of URLs (nutrition_value urls)
    path("foods.html", foods.food, name='foods'),
]