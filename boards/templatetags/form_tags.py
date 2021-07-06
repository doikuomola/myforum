from django import template

register = template.Library()

@register.filter
def field_type(value):
    return value