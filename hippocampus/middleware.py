from django.conf import settings
from django.utils.translation import get_language_from_request

from hippocampus import HIPPOCAMPUS_COOKIE_NAME
from hippocampus.models import *

try:
    import GeoIP
except ImportError:
    GeoIP = None

class HippocampusMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        model = view_kwargs.pop('hippocampus', None)
        if model is None:
            return None
        cookie_id = request.COOKIES.get(HIPPOCAMPUS_COOKIE_NAME)
        if cookie_id is None:
            return None
        slug = view_kwargs.get('slug', None)
        slug_field = view_kwargs.get('slug_field', None)
        object_id = view_kwargs.get('object_id', None)
        if not (model and ((slug and slug_field) or object_id)):
            return None
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address in [filter.ip_address for filter in IPFilter.objects.all()]:
            return None
        if object_id is not None:
            object = model.objects.get(id=object_id)
        else:
            object = model.objects.get(**{slug_field: slug})
        referer = request.META.get('HTTP_REFERER', '')
        visit = Visit(cookie_id=cookie_id, ip_address=ip_address, referer=referer)
        visit.content_object = object
        visit.language = get_language_from_request(request)
        visit.url = request.path
        if GeoIP:
            gi = GeoIP.open(settings.GEOIP_DATABASE_FILE, GeoIP.GEOIP_STANDARD)
            visit.country = gi.country_code_by_addr(ip_address) or ''
        visit.save()
        return None
