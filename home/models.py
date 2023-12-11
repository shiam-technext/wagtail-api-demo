from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.api import APIField

from home.serializers import ImageSerializedField


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    api_fields = [
        
    ]

class BlogPage(Page):
    blog_title = models.CharField(max_length=255)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True)
    content = RichTextField()

    @property
    def cover_image(self):
        return self.image
    
    @property
    def h1_text(self):
        return self.blog_title

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('image'),
        FieldPanel('content'),
    ]

    # Export fields over the API
    api_fields = [
        APIField('h1_text'),
        APIField('cover_image', serializer=ImageSerializedField()),
        APIField('content'),
    ]
