import os
import zoneSetFirewalld

def ip_url():
    url = input('Qual o url que deseja descobrir o IP: ')
    os.system('host -t a {}'.format(url))

def block_outgoing_traffic():
    nova_zona=zoneSetFirewalld.set_zone()
    url_ip = input('Qual o IP da URL: ')
    cmd = "sudo firewall-cmd --permanent --zone={} --add-rich-rule='rule family=ipv4 source address={} drop'".format(nova_zona, url_ip)
    os.system(cmd)
    print('Status do reload:')
    os.system('sudo firewall-cmd --reload')
