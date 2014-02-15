from django import template

register = template.Library()


@register.filter
def value(value, key):
    return value[key]
