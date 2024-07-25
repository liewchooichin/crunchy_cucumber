from django.apps import AppConfig

# custom admin
#from django.contrib.admin.apps import AdminConfig


#class MyAdminConfig(AdminConfig):
#    default_site = "polls.admin.MyAdminSite"


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
