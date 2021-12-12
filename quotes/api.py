from rest_framework import routers
from main import views as quote_views

router = routers.DefaultRouter()
router.register(r'quotes', quote_views.QuotesViewSet)
router.register(r'authors', quote_views.AuthorViewSet)
