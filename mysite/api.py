# api.py

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter

from rest_framework.renderers import JSONRenderer

from home.models import BlogPage

api_router = WagtailAPIRouter('wagtailapi')

class PostPagesAPIViewSet(PagesAPIViewSet):
    model = BlogPage


api_router.register_endpoint("posts", PostPagesAPIViewSet)

api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)