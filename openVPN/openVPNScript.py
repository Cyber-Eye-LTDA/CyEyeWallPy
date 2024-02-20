import os
import secrets
import string


def gerar_senha(tamanho=15):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        if (any(c.islower() for c in senha)
                and any(c.isupper() for c in senha)
                and any(c.isdigit() for c in senha)
                and any(c in string.punctuation for c in senha)):
            return senha


def salvar_senha(nome_arquivo, senha):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(senha)


def autoInstall():
    os.system('clear')
    print('''
 ██████╗██╗   ██╗██████╗ ███████╗██████╗    ███████╗██╗   ██╗███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██╔════╝╚██╗ ██╔╝██╔════╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   █████╗   ╚████╔╝ █████╗  
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██╔══╝    ╚██╔╝  ██╔══╝  
╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ███████╗   ██║   ███████╗
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚══════╝   ╚═╝   ╚══════╝
  (Automatic OPENVPN Installer)                  written by: martiaga                                                 
''')
    main_question = input('Did you run the script in SUDO mode? (y/n): ')
    if main_question == 'y':
        os.system('sudo apt update -qq 2>/dev/null && sudo apt upgrade -qq -y 2>/dev/null')
        os.system('sudo apt install -qq -y python3-pexpect 2>/dev/null')
        os.system('sudo apt install -qq -y openvpn 2>/dev/null && sudo apt install -qq -y easy-rsa 2>/dev/null')
        home_directory = os.getcwd()
        os.system(f'sed -i "$ a export PATH=$PATH:/usr/sbin" {home_directory}/.bashrc')
        os.system(f'mkdir -p {home_directory}/openvpn/easy-rsa/')
        os.system(f'ln -s /usr/share/easy-rsa/* {home_directory}/openvpn/easy-rsa/')
        os.chdir(f'{home_directory}/openvpn/easy-rsa/')
        os.system(f'sudo sh easyrsa init-pki')
        os.system(f'mkdir {home_directory}/openvpn/passwords/')

        #################################
        diretorio_senha = f"{home_directory}/openvpn/passwords/"
        nome_arquivo1 = "senha_vpn_ca.txt"
        caminho_senha = os.path.join(diretorio_senha, nome_arquivo1)
        senha_vpn_ca = gerar_senha()
        salvar_senha(caminho_senha, senha_vpn_ca)
        nome_arquivo2 = "senha_vpn_pem.txt"
        caminho_senha2 = os.path.join(diretorio_senha, nome_arquivo2)
        senha_vpn_pem = gerar_senha()
        salvar_senha(caminho_senha2, senha_vpn_pem)

        os.system('sudo sh easyrsa build-ca')

        os.system('sudo sh easyrsa build-server-full vpn_server nopass')

        os.system('sudo sh easyrsa sign-req server vpn_server')

        os.system(f'sudo sh easyrsa gen-dh')
        diretorio_pki = f'{home_directory}/openvpn/easy-rsa/pki/'
        diretorio_private = f'{home_directory}/openvpn/easy-rsa/pki/private/'
        diretorio_issued = f'{home_directory}/openvpn/easy-rsa/pki/issued/'
        os.chown(diretorio_pki, 1000, 1000)
        os.chown(diretorio_private, 1000, 1000)
        os.chown(diretorio_issued, 1000, 1000)
        os.chdir(f'{home_directory}/openvpn/easy-rsa/pki/')
        os.system('openvpn --genkey tls-crypt-v2-server private/vpn_server.pem')

        diretorio_conf = '/etc/openvpn/server/server.conf'
        with open(diretorio_conf, 'w') as f:
            f.write('#--------------------\n')
            f.write('#VPN port\n')
            f.write('port 1194\n\n')
            f.write('#VPN over UDP\n')
            f.write('proto udp\n\n')
            f.write('# "dev tun" will create a routed IP tunnel\n')
            f.write('dev tun\n\n')
            f.write('ca ca.crt\n')
            f.write('cert vpn_server.crt\n')
            f.write('key vpn_server.key\n')
            f.write('tls-crypt-v2 vpn_server.pem\n')
            f.write('dh dh.pem\n\n')
            f.write('#network for the VPN\n')
            f.write('server 10.8.0.0 255.255.255.0\n\n')
            f.write('push "redirect-gateway autolocal"\n\n')
            f.write('# Maintain a record of client <-> virtual IP address\n')
            f.write('# associations in this file.\n')
            f.write('ifconfig-pool-persist /var/log/openvpn/ipp.txt\n\n')
            f.write('# Ping every 10 seconds and assume client is down if\n')
            f.write('# it receives no response in 120 seconds.\n')
            f.write('keepalive 10 120\n\n')
            f.write('#cryptographic cipher\n')
            f.write('cipher AES-256-GCM\n\n')
            f.write('#avoid accessing certain resources on restart\n')
            f.write('persist-key\n')
            f.write('persist-tun\n\n')
            f.write('#log of current connections\n')
            f.write('status /var/log/openvpn/openvpn-status.log\n\n')
            f.write('#log verbose level (0-9)\n')
            f.write('verb 4\n\n')
            f.write('# Notify the client when the server restarts\n')
            f.write('explicit-exit-notify 1\n')
            f.write('#-----------------------------------------\n')

        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/ca.crt /etc/openvpn/server/')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/dh.pem /etc/openvpn/server/')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/private/vpn_server.key /etc/openvpn/server/')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/private/vpn_server.pem /etc/openvpn/server/')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/issued/vpn_server.crt /etc/openvpn/server/')
        ##################################################
        os.chown(diretorio_pki, 0, 0)
        os.chown(diretorio_private, 0, 0)
        os.chown(diretorio_issued, 0, 0)
        os.system('sudo sh -c \'echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf\'')
        os.system('sudo sysctl -p')
        os.system('sudo firewall-cmd --permanent --new-zone=vpn')
        os.system('sudo firewall-cmd --reload')
        os.system('sudo firewall-cmd --permanent --zone=vpn --add-interface=tun0')
        os.system('sudo firewall-cmd --permanent --zone=public --add-port=1194/udp')
        os.system('sudo firewall-cmd --permanent --zone=vpn --add-port=1194/udp')
        os.system('sudo firewall-cmd --permanent --zone=vpn --add-source=10.8.0.0/16')
        os.system('sudo firewall-cmd --permanent --zone=public --add-masquerade')
        os.system('sudo firewall-cmd --permanent --zone=vpn --set-target=ACCEPT')
        os.system('sudo firewall-cmd --permanent --zone=vpn --add-forward')
        os.system('sudo firewall-cmd --permanent --zone=public --add-service=openvpn')
        os.system('sudo firewall-cmd --reload')
        ##################################################
        os.system('sudo systemctl enable openvpn-server@server.service')
        check_service = os.system('sudo systemctl is-active openvpn-server@server.service')
        if check_service == 0:
            os.system('sudo systemctl restart openvpn-server@server.service')
        else:
            os.system('sudo systemctl start openvpn-server@server.service')
    else:
        exit()


if __name__ == '__main__':
    autoInstall()
