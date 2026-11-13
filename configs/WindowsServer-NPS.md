# Windows Server y NPS

- Host: `SADNPS` / dominio `campusano.local`.
- Dirección: `192.168.45.10/24`, gateway `192.168.45.1`.
- Roles: Active Directory Domain Services, DNS y Network Policy Server.
- Cliente RADIUS: `R1-CISCO`, `192.168.45.1`, autenticación UDP 1812 y accounting UDP 1813.
- Directiva: `CiscoAdminAccess`; usuario de prueba `radiusadmin`.
- Clave compartida omitida de este repositorio.
- Auditoría de Security: evento 6272 (acceso concedido) y 6273 (acceso rechazado).

La captura `../images/nps-6272-6273.png` evidencia ambos eventos.
