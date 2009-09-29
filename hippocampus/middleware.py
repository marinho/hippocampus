from hippocampus.models import *

class HippocampusMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        model = view_kwargs.pop('hippocampus', None)
        if model is None:
            return None
        slug = view_kwargs.get('slug', None)
        slug_field = view_kwargs.get('slug_field', None)
        object_id = view_kwargs.get('object_id', None)
        if not (model and ((slug and slug_field) or object_id)):
            return None
        ip_address = request.META['REMOTE_ADDR']
        if ip_address in [filter.ip_address for filter in IPFilter.objects.all()]:
            return None
        if object_id is not None:
            object = model.objects.get(id=object_id)
        else:
            object = model.objects.get(**{slug_field: slug})
        # Record vist
        return None
