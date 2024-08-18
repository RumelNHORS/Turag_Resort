from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is(value, arg):
    return len(value) == int(arg)
