from rest_framework.fields import Field

class ImageSerializedField(Field):
    def to_representation(self, value):
        return {
            "img_src": value.file.url,
            "height": value.height,
            "width": value.width,
        }