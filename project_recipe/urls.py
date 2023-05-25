from django.contrib import admin
from django.urls import path

from recipe.views import main, category_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('category/', category_list, name='category_list')

]
