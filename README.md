# Tarea: Desarrollo de Aplicación Backend con Django

**Objetivo:** Desarrollar una solución para gestión bancaria basada en relaciones de tablas.

## Detalles Generales

- **Modalidad**: Grupal
- **Integrantes**: Mínimo 4, Máximo 5
- **Fecha de presentación**: 26 de Octubre
- **Diagrama de referencia**: 
![Diagrama](images/tareaDiplomadoBacken-Página-2.drawio (1).png)

## Instrucciones

### 1. Configuración del Entorno

- **Requisitos**: Asegura tener instalado `Django`, `rest_framework`, y `rest_framework_simplejwt`.
  
- **Proyecto Django**: 
    ```bash
    django-admin startproject finanzas-diplomado-backend
    ```
  
- **App Cuentas**: 
    ```bash
    python manage.py startapp cuentas
    ```

### 2. Configuraciones y Desarrollo

#### Configuraciones iniciales

- **Base de datos**: En `settings.py`, configura la base de datos para usar PostgreSQL. Define usuario, contraseña, host y puerto.
  
- **Apps**: Registra tu nueva aplicación y las necesarias (`rest_framework` y `rest_framework_simplejwt`) en `INSTALLED_APPS`.
  
- **REST_FRAMEWORK**: Establece `DEFAULT_PERMISSION_CLASS` y `DEFAULT_AUTHENTICATION_CLASSES`.
  
- **Migraciones**: 
    ```bash
    python manage.py migrate
    ```

#### Desarrollo principal

- **Modelos**: Define modelos basados en el diagrama provisto.
  
- **Serializadores**: Implementa los serializadores para los modelos.
  
- **Vistas CRUD**: Desarrolla las vistas para CRUD y listados.
  
- **Operaciones específicas**: Crea vistas para Transferencia, Depósito, Retiro, Extractos, y Bloqueos.
  
- **URLs**: Define URLs para las vistas y para manejo de tokens.
  
- **Docker**:
    ```bash
    # Crea el Dockerfile
    docker build . 
    # Despliega el contenedor
    docker run [OPTIONS]
    ```

### 3. Validaciones

- Solo se permiten transferencias entre cuentas del mismo tipo (Cuenta Corriente o Caja de Ahorro).
  
- No se debe permitir una transferencia que exceda el saldo disponible.
  
- Las transferencias deben ser realizadas en la misma moneda.
  
- Asegura que las cuentas estén activas para todas las operaciones.

### 4. Entrega

Publica tu trabajo en un repositorio público, ya sea en GitHub u otra plataforma.

### 5. Presentación

La demostración del proyecto se hará desde una sola máquina.
