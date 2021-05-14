#Navegacion: Permite mantener el link activo, este modulo se debe incluir directamente en la plantilla principal.

```
Los enlaces deben tener como class='url' solo de esta manera el script sabra a cual tiene 
que apuntar cuando la url cambie.

<a class='url' href='xxxxxx/xxxx'>

```

#GeneradorUrlsParametrosGet: Permite obtener los parametros get de la url.

Ejemplo:
```
<a class="page-link" onclick="url('page',1)

Esto deberia redireccionarlo a => www.pagina.com/?page=1

```