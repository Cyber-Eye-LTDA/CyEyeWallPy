import os
import zoneSetFirewalld


def block_incoming_traffic_ip():
    nova_zona = zoneSetFirewalld.set_zone()
    ruleFamily = input('Qual o tipo de IP que deseja banir: ')
    source_address = input('Qual o IP que deseja banir: ')
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-rich-rule=\'rule family="{ruleFamily}" source address="{source_address}" reject\'')
    print('Status do reload:')
    os.system('sudo firewall-cmd --reload')