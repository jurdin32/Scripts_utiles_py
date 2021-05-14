
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag()
def paginacion(actual, fin,total = 12):
    grupo = 4
    if fin > total:
        if actual - grupo > 1:
            if actual + grupo >= fin:
                pag = orden_paginacion(fin - total, total, fin)
            else:
                pag = orden_paginacion(actual - grupo, total, fin)
        else:
            pag = orden_paginacion(1, total, fin)
    else:
        pag = orden_paginacion(1, fin, fin)
    pag=set(pag)
    pag=sorted(pag)
    lista=""
    for x in pag:
        if x == actual:
            lista += """<li class="page-item active"><a class="page-link" onclick="?page=%s" style="cursor: pointer; text-decoration:none">%s</a></li>""" % (x, x)
        else:
            lista+="""<li class="page-item"><a class="page-link" onclick="?page=%s" style="cursor: pointer; text-decoration:none">%s</a></li>"""%(x,x)
    return mark_safe(lista)

    

def orden_paginacion(inicio, total, ultimo):
    valores = []
    x = range(total)
    for n in x:
        valores.append(inicio + n)
    # Si contiene más de 9
    if ultimo > 9:
        decenas = int(ultimo/10)
        for n in range(decenas):
            valores.append((n+1)*10)
    return valores