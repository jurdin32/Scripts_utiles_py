#ImportExportModelAdmin: Es una libreria que permite generar importacion y exportacion:


Uso: En el Settings de la App
```
1. Instalar la libreria con: pip install django-import-export

```

```
2. Agregar al Setting en INSTALLED_APPS la libreria instalada: 'import_export'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
]
```

```
3. Crear una clase manejadora que tendra la siguiente estructura:

from import_export import resources

class ObjetoResource(resources.ModelResource):
    class Meta:
        model=Objeto
```

```
4. en el admin de la aplicacion:

@admin.register(Objeto)
class CatalogoAdmin(ImportExportModelAdmin):
    resource_class =CatalogoResource
    list_display = Attr(Objeto)

```

Objeto es el modelo que deseamos aplicar la propiedad.
