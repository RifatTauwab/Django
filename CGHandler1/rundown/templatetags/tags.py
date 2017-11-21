#https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value, arg):
    return value.split(arg)