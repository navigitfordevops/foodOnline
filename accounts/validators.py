from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    # will give you jpeg for example cover.jpeg -> [1]
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension. Allowed extension' + str(valid_extensions))
