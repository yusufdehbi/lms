from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def is_active(request, viewname):
    return request.path == reverse(viewname)


@register.filter
def department_initials(department_name):
    words = department_name.split()
    if len(words) == 1:
        return words[0][:2].upper()
    else:
        return (words[0][0] + words[1][0]).upper()
