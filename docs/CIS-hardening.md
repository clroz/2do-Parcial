# Evaluación CIS del router

## Propósito
Evaluar controles seleccionados, alineados con recomendaciones CIS para Cisco IOS, antes y después del hardening del C7200. El auditor verifica presencia en el running-config; no modifica equipos.

## Hallazgos y cambios aplicados

| Control | Motivo y prueba |
|---|---|
| `enable secret`, cuenta local con `secret` y `service password-encryption` | Protegen el acceso privilegiado y las credenciales locales; verificados en la configuración. |
| SSHv2, VTY solo SSH y tiempo de sesión limitado | Reduce exposición de administración remota; login SSH comprobado desde la LAN. |
| ACL de administración en VTY | Limita la administración a `192.168.45.0/24`. |
| `login on-failure log` y `login on-success log` | Registra intentos de acceso; NPS mostró eventos 6272 y 6273. |
| Buffer syslog | Conserva eventos locales para revisión. |
| HTTP/HTTPS deshabilitados en IOS | Reduce servicios de administración no usados. |
| SNMP RO con ACL | Permite monitoreo sin escritura y limita el origen al segmento de administración. Zabbix recibió datos de ambos equipos. |
| OSPF message-digest | Protege la formación del vecino entre C7200 y FortiGate; estado observado `FULL`. |
| `no ip source-route` | Deshabilita source routing no requerido. |

## Resultados
- Inicial: `2/18` controles presentes, en `evidencias/CIS-inicial.txt`.
- Posterior: `18/18`, en `evidencias/CIS-posterior.txt`, generado con el auditor sobre la captura de configuración completa.
- Credenciales, community SNMP y claves OSPF se redactan en los archivos publicados; la sintaxis y el tipo de control permanecen visibles para auditoría.

## Reproducir auditoría

```bash
python3 scripts/audit_cis_ios.py configs/C7200-running-config.txt
```
