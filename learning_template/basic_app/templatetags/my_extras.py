from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,args):
    """
    Cuts out the value with arg
    :param value:
    :param args:
    :return:
    """
    return value.replace(args,'*')