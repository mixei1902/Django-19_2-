from django import template

register = template.Library()


@register.filter(name='mymedia')
def mymedia(value):
    if value:
        return f'/media/{value}'
    return '#'
