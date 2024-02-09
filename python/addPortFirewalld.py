import os
import zoneSetFirewalld

def add_port_firewall():
	nova_zona=zoneSetFirewalld.set_zone()
	quantidade_ports = int(input('Quantas portas deseja abrir/adicionar no firewall: '))
	if quantidade_ports == 1:
		port = input(' Digite a porta que deseja abrir/adicionar no firewall: ')
		os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-port={port}/tcp')
	elif quantidade_ports > 1:
		for _ in range (quantidade_ports):
			ports = input('Qual porta deseja abrir: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-port={ports}/tcp')
	else:
		quest_confirmation = input('Era somente esta quantidade de portas que deseja adicionar(y/n): ')
		if quest_confirmation == 'y':
			print('Okay, as portas foram adicionadas corretamente.')
		elif quest_confirmation == 'n':
			more_ports = input('Qual outra porta gostaria de adicionar: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-port={more_ports}')
	reload_firewall = os.system('sudo firewall-cmd --reload')
	if reload_firewall == 0:
		print('Status do reload: success')

