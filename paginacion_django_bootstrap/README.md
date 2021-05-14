#PAGINACION CON DJANGO Y BOOTSTRAP

Ejemplo de uso:

Desde la vista:

```
def objectsPaginado(request,objects,cantidad):
    paginator = Paginator(objects, cantidad)
    page = request.GET.get('page')
    return paginator.get_page(page)

```

En el Template:
```
{%load paginator_template_tags } # carga la libreria

{% if objects.paginator.num_pages > 1 %}
    <div class="row">
        <div class="col">
            <ul class="pagination float-right" style="overflow-x: auto">
                {% if objects.has_previous %}
                    <li class="page-item"><a class="page-link" onclick="?page={{ objects.previous_page_number }}" style="cursor: pointer">
                        <i class="fas fa-angle-left"></i></a>
                    </li>
                {% endif %}
                {% paginacion objects.number objects.paginator.num_pages %}
                {% if objects.has_next %}
                    <a class="page-link" onclick="?page={{ objects.next_page_number }}"
                        style="cursor: pointer"><i class="fas fa-angle-right"></i></a>
                {% endif %}
            </ul>
        </div>
    </div>
{% endif %}

```

Donde objects es el objeto que viene paginado.
