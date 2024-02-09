import os
import zoneSetFirewalld


def add_service():
	nova_zona = zoneSetFirewalld.set_zone()
	quantidade_services = int(input('Quantos servicos voce ira adicionar ao firewall: '))
	if quantidade_services == 1:
		service = input('Digite o servico que deseja adicionar: ')
		os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-service={service}')
	elif quantidade_services > 1:
		for _ in range(quantidade_services):
			services = input('Qual o nome do servico que deseja adicionar: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-service={services}')
	else:
		quest_confirmation = input('Era apenas esta quantidade de servicos que deseja adicionar(y/n): ')
		if quest_confirmation == 'y':
			print('Okay, os servicos foram adicionados.')
		elif quest_confirmation == 'n':
			more_services = input('Qual o outro servico que deseja adicionar: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-service={more_services}')
	print('Status do reload:')
	os.system('sudo firewall-cmd --reload')
