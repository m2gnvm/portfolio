from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Split a string by delimiter and return a list"""
    if not value:
        return []
    return [item.strip() for item in str(value).split(delimiter)]

@register.filter
def status_label(value):
    """
    Format a status string like 'in_progress' as 'In Progress'.
    """
    if not value:
        return ''
    return str(value).replace('_', ' ').title()

