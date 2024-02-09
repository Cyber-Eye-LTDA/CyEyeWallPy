import os


def remove_zone_firewall():
    print('Antes de prosseguir, aqui esta a lista de zonas')
    os.system('sudo firewall-cmd --get-zones')
    print('\n*ZONAS PRE-EXISTENTES NAO SAO POSSIVEIS DE REMOVER*\n')
    quantidade_zonas = input(int('\nDigite quantas zonas deseja remover: '))
    if quantidade_zonas == 1:
        nova_zona = input('\nDigite o nome da zona: ')
        os.system(f'sudo firewall-cmd --permanent --delete-zone={nova_zona} 2>/dev/null')
    elif quantidade_zonas > 1:
        for _ in range (quantidade_zonas):
            nova_zona = input('\nDigite o nome da zona: ')
            os.system(f'sudo firewall-cmd --permanent --delete-zone={nova_zona} 2>/dev/null')
    else:
        print ('Quantidade invalida.')
        input()
    reload_firewall = os.system('sudo firewall-cmd --reload')
    if reload_firewall == 0:
        print('Status do reload: success')