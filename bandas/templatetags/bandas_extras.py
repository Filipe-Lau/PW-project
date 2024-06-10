from django import template

register = template.Library()

@register.filter
def albuns_ordenados(album):
    return album.objects.all()