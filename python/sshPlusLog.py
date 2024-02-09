import os
import zoneSetFirewalld


def ssh_log():
    nova_zona = zoneSetFirewalld.set_zone()
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-service=ssh')
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-rich-rule=\'rule family=ipv4 service name=ssh log prefix="SSH Connection: " level="notice" limit value="10/m" drop\'')
    
    print('Status do reload:')
    os.system('sudo firewall-cmd --reload')
    
    #Habilita o crontab para salvar o log periodicamente no arquivo ssh_connections.log
    os.system('(echo "*/10 * * * * journalctl -xe | grep \\"SSH Connection\\" >> /var/log/ssh_connections.log") | sudo crontab -')