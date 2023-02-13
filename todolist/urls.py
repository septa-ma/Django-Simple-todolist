from django.urls import path
from . import views

# 1- make this file manually.
# 2- add apps in initial-apps of setting.
# write app's url here.
urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('moreInfo/<int:todoId>', views.moreInfo, name="moreInfo"),
    path('delete/<int:todoId>', views.delete, name="delete"),
    path('update/<int:todoId>', views.updateTodo, name="update"),
    path('create', views.createTodo, name="create"),
]

# The path() function is passed four arguments,
# two required: route and view, 
# two optional: kwargs, and name. 

# 1- route:
# is a string that contains a URL pattern. When processing a request, 
# Django starts at the first pattern in urlpatterns and makes its way down the list,
# comparing the requested URL against each pattern until it finds one that matches.

# 2- view:
# When Django finds a matching pattern, 
# it calls the specified view function with an HttpRequest object
# as the first argument and any “captured” values 
# from the route as keyword arguments.

# 3- kwargs:
# Arbitrary keyword arguments can be passed in a dictionary to the target view.

# 4- name:
# Naming your URL lets you refer to it unambiguously from elsewhere 
# in Django, especially from within templates. 
# This powerful feature allows you to make global changes 
# to the URL patterns of your project while only touching a single file.