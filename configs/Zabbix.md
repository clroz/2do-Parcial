# Servidor Zabbix

- Appliance Rocky Linux 8.10 con Zabbix 7.0.32.
- Interfaz `eth0`: `192.168.45.50/24` mediante DHCP; gateway `192.168.45.1`.
- Host SNMP `R1-CISCO`: `192.168.45.1`.
- Host SNMP `SW1`: `192.168.45.2`.
- Los dos hosts reportaron interfaz SNMP disponible y valores `System description` en la consulta registrada.
- Comunidad de solo lectura redactada en los artefactos públicos.

La captura de consola evidencia la dirección marcada `dynamic` y la ruta por el router.
