from datetime import datetime

from django.http import HttpRequest
from hippocampus import HIPPOCAMPUS_COOKIE_NAME
from hippocampus.models import Visit

def log_exit(request):
    cookie_id = request.COOKIES.get(HIPPOCAMPUS_COOKIE_NAME)
    if cookie_id is not None:
        try:
            last_visit = Visit.objects.filter(
                cookie_id=cookie_id, exit__isnull=True
            ).orderby('-enter')[0]
        except IndexError:
            pass
        else:
            last_visit.exit = datetime.now()
            last_visit.save()
    return HttpRequest('')
    
