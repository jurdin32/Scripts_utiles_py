#ResizeImageMixin: es un modulo que sirve para redimensionar imagenes e incluir imagen como marca de agua directamente desde el modelo.


Ejemplo:
```
class Imagenes(models.Model):
    ......
    foto=models.ImagenField(upload="fotos")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
             
        self.resize(
            imageField=self.foto, 
            ancho=600, alto=600, 
            format='png', 
            marca=(350, 530)) # la marca es opcional

        super(Imagenes,self).save()
```

Es importante que se agregue las dimensiones, y el formato, la marca de agua es opcional