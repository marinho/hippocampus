from hippocampus.models import *

class HippocampusMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        track = view_kwargs.pop('track', None)
        if track is None:
            return None
        model = view_kwargs.pop('hippo_model', None)
        slug = view_kwargs.pop('slug', None)
        slug_field = view_kwargs.pop('slug_field', None)
        object_id = view_kwargs.pop('object_id', None)
        if not (model and ((slug and slug_field) or object_id)):
            return None
        ip_address = request.META['REMOTE_ADDR']
        if ip_address not in [filter.ip_address for filter in IPFilter.objects.all()]:
            return None
        if object_id is not None:
            object = model.objects.get(id=object_id)
        else:
            object = model.objects.get(**{slug_field: slug})
