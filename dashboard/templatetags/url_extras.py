from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def is_active(request, viewname):
    return request.path == reverse(viewname)
