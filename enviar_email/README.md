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

Se puede enviar Contenido Html activando la bandera is_html=True, y en lugar el mensaje se pasa la pagina parseada en string.