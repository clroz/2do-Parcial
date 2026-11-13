#!/usr/bin/env python3
"""Audita controles seleccionados alineados a las recomendaciones CIS para Cisco IOS."""
import argparse
import re
from pathlib import Path

CHECKS = [
    ("Enable secret configurado", r"(?m)^enable secret "),
    ("Usuario local admin con secret", r"(?m)^username admin privilege 15 secret "),
    ("Cifrado de contrasenas de linea habilitado", r"(?m)^service password-encryption$"),
    ("SSH version 2", r"(?m)^ip ssh version 2$"),
    ("VTY limita transporte a SSH", r"(?ms)^line vty 0 4\s+.*?^ transport input ssh$"),
    ("AAA permite respaldo local para VTY", r"(?m)^aaa authentication login VTY group NPS-GROUP local$"),
    ("VTY aplica lista AAA", r"(?ms)^line vty 0 4\s+.*?^ login authentication VTY$"),
    ("Servicio HTTP deshabilitado", r"(?m)^no ip http server$"),
    ("Servicio HTTPS deshabilitado", r"(?m)^no ip http secure-server$"),
    ("Registro de accesos fallidos habilitado", r"(?m)^login on-failure log$"),
    ("Registro de accesos exitosos habilitado", r"(?m)^login on-success log$"),
    ("Buffer de syslog configurado", r"(?m)^logging buffered \d+ informational$"),
    ("Comunidad SNMP de solo lectura", r"(?m)^snmp-server community \S+ RO \d+$"),
    ("Servidor RADIUS NPS definido", r"(?m)^ address ipv4 192\.168\.45\.10 auth-port 1812 acct-port 1813$"),
    ("Autenticacion OSPF con digest", r"(?m)^ area 0 authentication message-digest$"),
    ("Clave OSPF aplicada a interfaz", r"(?m)^ ip ospf message-digest-key 1 md5 "),
    ("Sin source routing", r"(?m)^no ip source-route$"),
    ("Lista de acceso de gestion en VTY", r"(?ms)^line vty 0 4\s+.*?^ access-class 10 in$"),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    args = parser.parse_args()
    text = args.config.read_text(encoding="utf-8", errors="replace")
    passed = 0
    for label, pattern in CHECKS:
        ok = re.search(pattern, text) is not None
        passed += int(ok)
        print(f"{'PASS' if ok else 'FAIL'} | {label}")
    print(f"Resultado: {passed}/{len(CHECKS)} controles presentes")
    return 0 if passed == len(CHECKS) else 1

if __name__ == "__main__":
    raise SystemExit(main())