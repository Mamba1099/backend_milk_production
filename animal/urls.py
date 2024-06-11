"""urls for animal app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnimalViewSet,
    PurchasedViewSet,
    LocallyServicedViewSet,
    AIPredeterminedServicedViewSet,
    AInotPredeterminedServicedViewSet,
)

router = DefaultRouter()
router.register(r"animals", AnimalViewSet)
router.register(r"purchased", PurchasedViewSet)
router.register(r"locally_serviced", LocallyServicedViewSet)
router.register(r"ai_predetermined_serviced", AIPredeterminedServicedViewSet)
router.register(r"ai_not_predetermined_serviced", AInotPredeterminedServicedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
