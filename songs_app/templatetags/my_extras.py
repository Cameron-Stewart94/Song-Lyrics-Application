from django import template
register = template.Library()

@register.filter
def index(List, i):
    # Custom filter allows lists to be indexed in html files
    return List[int(i)]
