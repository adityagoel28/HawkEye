from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()

def highlight_search(text, search):
    highlighted = text.replace(search, '<span class="highlight">{}</span>'.format(search))
    return mark_safe(highlighted)

register.filter('highlight', highlight_search)
# register.tag()