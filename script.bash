docker run -p 8082:8088 -e DEBUG="True" -e DATABASE="Hospital-django" -e USER_DB="postgres" -e PASS_DB="12345" -e HOST_DB="192.168.13.53" -e PORT_DB="15432" --name finanzas diplomado-finanzas:1.4