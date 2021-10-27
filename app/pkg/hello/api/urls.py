from rest_framework.routers import SimpleRouter

from app.pkg.hello.api.views import HelloView

router = SimpleRouter(trailing_slash=False)
router.register(r'hello', HelloView, basename='hello')

urlpatterns = router.urls