import os
import autoInstallFirewalld
import addServiceFirewalld
import removeServiceFirewalld
import addPortFirewalld
import removePortFirewalld
import blockIncomingTrafficIp
import blockOutgoingTrafficIpUrl
import zoneSetFirewalld
import sshPlusLog
import allowIncomingTrafficIp
import addZoneFirewall
import removeZoneFirewall
import changeInterfaceFirewall

# função para limpar tela
def limpar_tela():
    os.system('clear')

# função para exibir menu
def exibir_ascii():
    print("""

   ______      __              ______
  / ____/_  __/ /_  ___  _____/ ____/_  _____
 / /   / / / / __ \/ _ \/ ___/ __/ / / / / _ \.
/ /___/ /_/ / /_/ /  __/ /  / /___/ /_/ /  __/
\____/\__, /_.___/\___/_/  /_____/\__, /\___/
     /____/                      /____/
               Written by: martiaga, gbrisolla""")

# função para exibir menu
    
def menu_config():
    while True:
        limpar_tela()
        exibir_ascii()
        print("""
    *EXECUTAR SCRIPT COM SUDO* 
            
    Config Menu:
    
    1. Auto Install Firewall
    2. Adicionar Zona
    3. Remover Zona
    4. Adicionar Servico
    5. Remover Servico
    6. Adicionar Porta
    7. Remover Porta
    8. Bloquear IP
    9. Permitir IP
    10. Bloquear acesso URL por IP
    11. Verificar Info de Zona
    12. Implementar SSH-Block + log
    13. Alterar interface de rede
    14. Sair
""")

        option = input("Escolha uma opcao: ")

        if option == '1':
            print ("\nSelecionada a opcao 1")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            autoInstallFirewalld.auto_install()

        elif option == '2':
            print ("\nSelecionada a opcao 2")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            addZoneFirewall.add_zone_firewall()

        elif option == '3':
            print ("\nSelecionada a opcao 3")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            removeZoneFirewall.remove_zone_firewall()

        elif option == '4':
            print ("\nSelecionada a opcao 4")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            addServiceFirewalld.add_service()

        elif option == '5':
            print ("\nSelecionada a opcao 5")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            removeServiceFirewalld.remove_service()

        elif option == '6':
            print ("\nSelecionada a opcao 6")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            addPortFirewalld.add_port_firewall()

        elif option == '7':
            print ("\nSelecionada a opcao 7")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            removePortFirewalld.remove_port_firewall()

        elif option == '8':
            print ("\nSelecionada a opcao 8")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            blockIncomingTrafficIp.block_incoming_traffic_ip()

        elif option == '9':
            print ("\nSelecionada a opcao 9")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            allowIncomingTrafficIp.allow_incoming_traffic_ip()

        elif option == '10':
            print ("\nSelecionada a opcao 10")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            blockOutgoingTrafficIpUrl.ip_url()
            blockOutgoingTrafficIpUrl.block_outgoing_traffic()

        elif option == '11':
            print ("\nSelecionada a opcao 11")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            nova_zona = zoneSetFirewalld.set_zone()
            print('\nInfo da Zona selecionada:\n')
            os.system(f'sudo firewall-cmd --zone={nova_zona} --list-all')
            print("\nPressione Enter para continuar.")
            input()
            
        elif option == '12':
            print ("\nSelecionada a opcao 12")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            sshPlusLog.ssh_log()
        
        elif option == '13':
            print ("\nSelecionada a opcao 13")
            continuar = input("\nDeseja continuar? (y/n): ").lower()
            if continuar == 'n':
                continue
            changeInterfaceFirewall.change_interface()

        elif option == '14':
            limpar_tela()
            print("See you farewell, my friend...\n")
            break
        else:
            print("Opcao invalida.")
            input()
def main():
    menu_config()

if __name__ == "__main__":
    main()