import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile


class ResizeImageMixin:
    def resize(self, imageField, ancho, alto, format='JPEG', marca=()):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert('RGBA')
        source_image=source_image.resize((ancho,alto))  # Resize to size

        if marca:
            path=os.path.join(BASE_DIR, 'static/xurimotos.png')
            imgAgua=Image.open(path)
            source_image.paste(imgAgua,marca,imgAgua)
        output = BytesIO()
        source_image.save(output, format=format, optimize=True, quality=90) # Save resize image to bytes
        output.seek(0)
        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)
        random_name = f'{uuid.uuid4()}.jpeg'
        imageField.save(random_name, file, save=False)