from django.contrib import admin
from django.urls import path

from task1.views import *

urlpatterns = [
        path('admin/', admin.site.urls),
        path('platform/', platform),
        path('platform/games/', games),
        path('platform/cart/', cart),
        path('platform/news/', news),
        path('', sign_up_by_django),
        path('registration_page', sign_up_by_html),
        ]
