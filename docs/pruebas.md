# Pruebas de aceptación

## Router
```text
show ip dhcp binding
show ip ospf neighbor
show ip route ospf
show ip ssh
show aaa servers
```

## RADIUS/NPS
```text
test aaa group radius radiusadmin <clave-valida> legacy
test aaa group radius radiusadmin <clave-incorrecta> legacy
```

La prueba observada fue aceptada con la credencial válida y rechazada con la incorrecta. En Windows se verificaron los eventos 6272 y 6273. No se publica ninguna contraseña.

## Switch y conectividad
```text
show ip ssh
ping 192.168.45.1 repeat 3 timeout 1
ping 192.168.45.10 repeat 3 timeout 1
ping 192.168.45.50 repeat 3 timeout 1
```

Los tres destinos respondieron 3/3.

## Zabbix
La consola mostró `192.168.45.50/24 dynamic` y ruta por `192.168.45.1`. En Latest data se verificaron los hosts `R1-CISCO` y `SW1` mediante SNMP.
