from pysnmp.hlapi import *
import json

def snmp_get(community, ip, port, oid):
    get_respond = getCmd(SnmpEngine(),
                         CommunityData(community),
                         UdpTransportTarget((ip, port)),
                         ContextData(),
                         ObjectType(ObjectIdentity(oid)))
    for (error_indication, error_status, error_index, var_binds) in get_respond:
        if error_indication:
            self.Main.error(f"Snmp error {error_indication}")
        elif error_status:
            self.Main.error(f"Snmp error {error_status}")
        else:
            value = var_binds[0][1]
            return value

with open('config.json') as config_file:
    get_config = json.load(config_file)

config_community = get_config['community']
config_ip = get_config['ip']
config_port = get_config['port']
config_oid = get_config['oid']
result = snmp_get(config_community, config_ip, config_port, config_oid)
print(result)