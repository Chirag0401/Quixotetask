from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1 MB")
    else:
        return value

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['jpeg', 'png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

