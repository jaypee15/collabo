from django import template

register = template.Library()

@register.filter
def status_color(status):
    color_mapping = {
        'Planning': 'bg-sky-400',
        'In Progress': 'bg-green-300',
        'On Hold': 'bg-yellow-300',
        'Completed': 'bg-blue-700',
        'Canceled': 'bg-red-300',
        'Archived': 'bg-gray-300',
        'Other': 'bg-purple-300',
    }
    return color_mapping.get(status, 'bg-gray-200')

@register.filter
def hover_status_color(status):
    color_mapping = {
        'Planning': 'bg-sky-600',
        'In Progress': 'bg-green-400',
        'On Hold': 'bg-yellow-600',
        'Completed': 'bg-blue-800',
        'Canceled': 'bg-red-400',
        'Archived': 'bg-gray-400',
        'Other': 'bg-purple-400',
    }
    return color_mapping.get(status, 'bg-gray-200')
