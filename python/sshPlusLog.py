import os
import datetime
import zoneSetFirewalld


def verificar_crontab(comando):
    # Lê o crontab atual
    crontab_atual = os.popen('sudo crontab -l').read()
    # Verifica se o comando já está presente no crontab
    return comando in crontab_atual

def adicionar_tarefa_cron(comando):
    # Verifica se o comando já está no crontab
    if not verificar_crontab(comando):
        # Adiciona o comando ao crontab
        os.system(f'echo "{comando}" | sudo crontab -')
        print('Tarefa adicionada ao crontab.')
    else:
        print('A tarefa ja esta presente no crontab.')

def ssh_log():
    print('ATENCAO: AO UTILIZAR ESSA FUNCAO BLOQUEARA O SSH DA ZONA SELECIONADA\n')
    nova_zona = zoneSetFirewalld.set_zone()
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-service=ssh 2>/dev/null')
    os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-rich-rule=\'rule family=ipv4 service name=ssh log prefix="Dropped SSH: " level="notice" limit value="10/m" drop\' 2>/dev/null')
    
    reload_firewall = os.system('sudo firewall-cmd --reload')
    if reload_firewall == 0:
        print('Status do reload: success')

    escolha_log = input('\nDeseja habilitar o log? (y/n): ')

    if escolha_log == 'y':

        #Habilita o crontab para salvar o log a cada 10 minutos no arquivo ssh_dropped_connections.log
        add_cron_log = '*/10 * * * * journalctl -xe | grep "Dropped SSH" >> /var/log/ssh_dropped_connections.log 2>&1'
        adicionar_tarefa_cron(add_cron_log)

        data_atual = datetime.datetime.now()
        nome_backup = f'/var/log/ssh_dropped_connections_backup_{data_atual.strftime("%Y%m")}.log'
        
        # Habilita crontab para fazer backup do arquivo de log antes de resetá-lo mensalmente
        add_cron_backup = f"0 0 1 * * sudo cp /var/log/ssh_dropped_connections.log {nome_backup}"
        adicionar_tarefa_cron(add_cron_backup)

        # Habilita o crontab para resetar o arquivo de log mensalmente
        add_cron_reset = "0 0 1 * * sudo truncate -s 0 /var/log/ssh_dropped_connections.log"
        adicionar_tarefa_cron(add_cron_reset)