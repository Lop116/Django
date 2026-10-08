from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('branches/',views.branches, name = 'branches'),
    path('coaches/',views.coaches, name = 'coaches'),
    path('classes/',views.classes, name = 'classes'),
    path('membership-plans/',views.membership_plans, name = 'membership_plans'),
    path('contact/',views.contact, name = 'contact'),
    path('support/process/', views.support_process, name='support_process'),
]