from django.urls import path
from rest_framework.routers import DefaultRouter
import Studio.views as svi

router = DefaultRouter()
router.register(r'', svi.StudioGetAV, basename="studio")


urlpatterns = [

    path("create/", svi.StudioCreateAV.as_view(), name="create-studio"),
    path("update_delete/<pk>", svi.StudioUpdateDeleteAV.as_view(), name="update-delete-studio")

]

urlpatterns += router.urls