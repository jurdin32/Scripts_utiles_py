#SnniperModelsAdmin: este modulo permite importar todos los atributos de las clases para mostrar en el admin:


Ejemplo:
```
@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = Attr(Objeto)
    list_display_links = Attr(Objeto)

```

Donde Objeto es el nombre del modelo que deseamos mostrar.

