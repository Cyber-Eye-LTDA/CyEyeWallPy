import os


def set_zone():
	zone_list = 'sudo firewall-cmd --get-zones'
	os.system(zone_list)
	view_active_zones_confirmation = input('Deseja visualizar quais zonas estao ativas(y/n): ')
	if view_active_zones_confirmation == 'y':
		os.system('sudo firewall-cmd --get-active-zones')
	nova_zona = input('Qual zona deseja selecionar: ')
	return nova_zona
