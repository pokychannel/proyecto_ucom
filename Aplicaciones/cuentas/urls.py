from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Aplicaciones.cuentas.views import PersonaViewSet, CuentaViewSet, CuentaCorrienteViewSet, CajaAhorroViewSet, \
    MovimientoViewSet, TransferenciaView

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'cuentas-corriente', CuentaCorrienteViewSet)
router.register(r'cajas-ahorro', CajaAhorroViewSet)
router.register(r'movimientos', MovimientoViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('transferencia/', TransferenciaView.as_view(), name='transferencia'),
]