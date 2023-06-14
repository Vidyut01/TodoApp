from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def get_value(d, key):
    return d.get(key)
