#Envio de Emails

Realizar la configuración del archivo 'configuracion.py'

Ejemplo:

Con adjuntos

```
enviarEmail(
    ['urdin-23@live.com','j-h-diog@live.com.ar'],
    'saludo',
    'Hola este es un mensaje con adjuntos',
    ['archivo.txt'])
```

Sin adjuntos
```
enviarEmail(
    ['urdin-23@live.com','j-h-diog@live.com.ar'],
    'saludo',
    'Hola este es un mensaje sin archivos adjuntos')

```