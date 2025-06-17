from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from call.views import ChamadaUsuarioViewSet, ChamadaTecnicoViewSet, ChamadosFinalizadosViewSet, ChamadosUsuarioFinalizadosViewSet
from usuario.views import UsuarioViewSet

# Roteadores separados
router_usuario = DefaultRouter()
router_usuario.register(r'chamadas-usuario', ChamadaUsuarioViewSet, basename='chamada-usuario')
router_usuario.register(r'chamados-usuario-finalizados', ChamadosUsuarioFinalizadosViewSet, basename='chamados-usuario-finalizados'
)

router_tecnico = DefaultRouter()
router_tecnico.register(r'chamadas-tecnico', ChamadaTecnicoViewSet, basename='chamada-tecnico')
router_tecnico.register(r'chamados-finalizados', ChamadosFinalizadosViewSet, basename='chamados-finalizados')

router_usuario.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('call.urls', namespace='call')),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('api/', include(router_usuario.urls)),
    path('api/', include(router_tecnico.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
