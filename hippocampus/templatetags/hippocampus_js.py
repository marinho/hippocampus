import hashlib
from datetime import datetime

from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
#from django.utils.safestring import mark_safe

from hippocampus import HIPPOCAMPUS_COOKIE_NAME

register = template.Library()

@register.inclusion_tag('hippocampus/script_tag.html')
def hippocampus_script():
    script_context = {
        'cookie_name': HIPPOCAMPUS_COOKIE_NAME,
        'cookie_val': hashlib.md5(datetime.now().isoformat()).hexdigest(),
        'log_exit_url': reverse('hippocampus_log_exit')
    }
    script = render_to_string('hippocampus/track.js', script_context)
    return {'script': script}
