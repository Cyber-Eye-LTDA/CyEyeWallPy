import os
import zoneSetFirewalld

def remove_service():
	nova_zona = zoneSetFirewalld.set_zone()
	quantidade_services = int(input('Quantos servicos voce ira remover do firewall: '))
	if quantidade_services == 1:
		service = input('Digite o servico que deseja remover: ')
		os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-service={service}')
	elif quantidade_services > 1:
		for _ in range(quantidade_services):
			services = input('Qual o nome do servico que deseja remover: ')
			os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --remove-service={services}')
	else:
		quest_confirmation = input('Era apenas esta quantidade de servicos que deseja remover(y/n): ')
		if quest_confirmation == 'y':
					print('Okay, os servicos foram removidos.')
		if quest_confirmation == 'n':
			more_services = input('Qual o outro servico que deseja remover: ')
			os.system(f'sudo firewall-cmd --permament --zone={nova_zona} --remove-service={more_services}')
	reload_firewall = os.system('sudo firewall-cmd --reload')
	if reload_firewall == 0:
		print('Status do reload: success')
