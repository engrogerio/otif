from django.conf import settings

def server_url(request):
    """Just to have the /sgp or /sgp_test from settings.py"""
    return {'SERVER_URL':settings.SERVER_URL}