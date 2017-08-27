from django.http import HttpResponse
import os

def run_backup(request):
    os.system("sh /home/inventsis/www/copydb.sh")
    return HttpResponse("Backup job done!")


