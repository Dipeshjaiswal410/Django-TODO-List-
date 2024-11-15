from django.contrib import admin  # Add this import statement
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
]

