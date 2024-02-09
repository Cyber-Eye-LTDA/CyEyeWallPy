import os
import zoneSetFirewalld

def remove_port_firewall():
	nova_zona=zoneSetFirewalld.set_zone()
	quantidade_ports = int(input('Quantas portas deseja fechar/encerrar: '))
	if quantidade_ports == 1:
		port= input('Digite a porta que deseja fechar/encerrar: ')
		os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-port={port}/tcp')
	elif quantidade_ports > 1:
		for _ in range (quantidade_ports):
			ports = input('Qual porta deseja fechar: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-port={ports}/tcp')
	else:
		quest_confirmation = input('Era somente esta quantidade de portas que deseja fechar(y/n): ')
		if quest_confirmation == 'y':
			print('Okay, as portas foram fechadas')
		elif quest_confirmation == 'n':
			more_ports = input('Qual outra porta deseja remover: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-port={more_ports}')
	print('Status do reload:')
	os.system('sudo firewall-cmd --reload')
