# Diseño y configuración

El C7200 conecta la LAN `192.168.45.0/24` al switch. El mismo router presta DHCP a la LAN. NPS en Windows Server proporciona autenticación RADIUS para la administración del router. FortiGate es el par OSPF del C7200 por el tránsito `10.45.0.0/30`; no se añadieron equipos.

El switch conecta al router en Gi0/0; Windows Server en Gi0/1; el PC en Gi0/2; y Zabbix en Gi0/3. Zabbix supervisa router y switch por SNMPv2c de solo lectura, con comunidad redactada y ACL de origen LAN.

La captura del running-config del C7200 con secretos redactados y la documentación de Windows/Zabbix se encuentran en `configs/`. Los archivos del switch y FortiGate son reconstrucciones/extractos a partir de los comandos aplicados y de las verificaciones conservadas; no son exportaciones `show running-config` actuales. La VM está apagada y no fue posible obtener una captura nueva. Las evidencias disponibles están en `evidencias/` y el diagrama en `images/topologia.svg`.
