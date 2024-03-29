import os
import zoneSetFirewalld


def allow_incoming_traffic_ip():
    nova_zona = zoneSetFirewalld.set_zone()
    source_address = input('\nDigite o ip que deseja permitir na zona: ')
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-source={source_address}')

    # reload para habilitar
    reload_firewall = os.system('sudo firewall-cmd --reload')
    if reload_firewall == 0:
        print('Status do reload: success')
