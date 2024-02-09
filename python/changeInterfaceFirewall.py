import os


def change_interface():
    print('\nEssas sao as interfaces disponiveis:\n')
    os.system('ip link show')
    print('\nEssas sao as zonas disponiveis:\n')
    os.system('sudo firewall-cmd --get-zones')
    check_interface = input('\nDigite a interface para verificar a zona utilizada por ela: ')
    os.system(f'sudo firewall-cmd --get-zone-of-interface={check_interface}')
    resposta_interface = input('\nA interface esta conectada a alguma zona? (y/n): ')
    if resposta_interface == 'y':
        check_change = input('\nDeseja alterar a zona da interface? (y/n): ')
        if check_change == 'y':
            nova_zona = input('\nDigite a nova zona da interface: ')
            os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --change-interface={check_interface}')
    elif resposta_interface == 'n':
        nova_zona = input('\nDigite a zona para habilitar a interface: ')
        os.system(f'sudo firewall-cmd --permanent --zone={nova_zona} --add-interface={check_interface}')

    reload_firewall = os.system('sudo firewall-cmd --reload')
    if reload_firewall == 0:
        print('Status do reload: success')