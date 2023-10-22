from decimal import Decimal, InvalidOperation

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Persona, Cuenta, CuentaCorriente, CajaAhorro, Movimiento
from .serializer import (PersonaSerializer, CuentaSerializer, CuentaCorrienteSerializer,
                          CajaAhorroSerializer, MovimientoSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class CuentaCorrienteViewSet(viewsets.ModelViewSet):
    queryset = CuentaCorriente.objects.all()
    serializer_class = CuentaCorrienteSerializer

class CajaAhorroViewSet(viewsets.ModelViewSet):
    queryset = CajaAhorro.objects.all()
    serializer_class = CajaAhorroSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class TransferenciaView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        cuenta_origen_id = request.data.get('cuenta_origen_id')
        cuenta_destino_id = request.data.get('cuenta_destino_id')
        monto = request.data.get('monto')

        # Validaciones
        if not all([cuenta_origen_id, cuenta_destino_id, monto]):
            return Response({'error': 'Faltan datos necesarios'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            monto = Decimal(monto)
        except InvalidOperation:
            return Response({'error': 'Monto inválido'}, status=status.HTTP_400_BAD_REQUEST)

        cuenta_origen = Cuenta.objects.get(id=cuenta_origen_id)
        cuenta_destino = Cuenta.objects.get(id=cuenta_destino_id)

        if cuenta_origen.saldo < monto:
            return Response({'error': 'Saldo insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

        # Realizar la transferencia
        cuenta_origen.saldo -= monto
        cuenta_destino.saldo += monto

        cuenta_origen.save()
        cuenta_destino.save()

        # Registrar el movimiento
        Movimiento.objects.create(cuenta=cuenta_origen, tipo_movimiento='T', monto=monto,
                                  descripcion=f'Transferencia a cuenta {cuenta_destino_id}')
        Movimiento.objects.create(cuenta=cuenta_destino, tipo_movimiento='D', monto=monto,
                                  descripcion=f'Transferencia desde cuenta {cuenta_origen_id}')

        return Response({'message': 'Transferencia realizada con éxito'}, status=status.HTTP_200_OK)