from django.conf.urls import url

from . import views

app_name = "clinic"

urlpatterns = [
      url(r'^$', views.login, name='login')
    , url(r'^login/', views.login, name='login')
    , url(r'^logout/', views.logout, name='logout')

    , url(r'^CRM-DentalClinic-Overview',views.crm_dentalclinic_overview, name='CRM-DentalClinic-Overview')
    , url(r'^CRM-ContactCenter-Overview',views.crm_contactcenter_overview, name='CRM-ContactCenter-Overview')
    , url(r'^CRM-OpenChannel-Overview',views.crm_openchannel_overview, name='CRM-OpenChannel-Overview')
    , url(r'^CRM-OrderManagement-Overview',views.crm_ordermanagement_overview, name='CRM-OrderManagement-Overview')

    , url(r'^calendar-index',views.calendar_index, name='calendar-index')
    , url(r'^inventory-index',views.inventory_index, name='inventory-index')
    , url(r'^hr-index',views.hr_index, name='hr-index')


# For AJAX
    , url(r'^get_appointment_schedule',views.get_appointment_schedule, name='get_appointment_schedule')

]
