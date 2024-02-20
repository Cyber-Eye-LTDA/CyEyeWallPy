import os

home_directory = os.getcwd()


def scriptOVPN():
    bash_script_lines = [
        "#!/bin/bash",
        "",
        "# 1 argument = Client_identifier",
        "cat <(echo -e 'client') \\",
        "    <(echo -e 'proto udp') \\",
        "    <(echo -e 'dev tun0') \\",
        "    <(echo -e 'remote 127.0.0.1 1194') \\",
        "    <(echo -e 'resolv-retry infinite') \\",
        "    <(echo -e 'nobind') \\",
        "    <(echo -e 'persist-key') \\",
        "    <(echo -e 'persist-tun') \\",
        "    <(echo -e 'remote-cert-tls server') \\",
        "    <(echo -e 'cipher AES-256-GCM') \\",
        "    <(echo -e '#user nobody') \\",
        "    <(echo -e '#group nobody') \\",
        "    <(echo -e 'verb 3') \\",
        "       <(echo -e '<ca>') \\",
        "       ca.crt \\",
        "       <(echo -e '</ca>\\n<cert>') \\",
        "       ${1}.crt \\",
        "       <(echo -e '</cert>\\n<key>') \\",
        "       ${1}.key \\",
        "       <(echo -e '</key>\\n<tls-crypt-v2>') \\",
        "       ${1}.pem \\",
        "       <(echo -e '</tls-crypt-v2>') \\",
        "       > ${1}.ovpn"
    ]

    os.system(f'mkdir {home_directory}/openvpn/scripts/')
    caminho_script = f'{home_directory}/openvpn/scripts/ovpn_creator.sh'

    if not os.path.exists(caminho_script):
        with open(caminho_script, "w") as script_file:
            for line in bash_script_lines:
                script_file.write(line + "\n")
            os.chmod(caminho_script, 0o755)


def configClient():
    os.system('clear')
    print('''
     ██████╗██╗   ██╗██████╗ ███████╗██████╗    ███████╗██╗   ██╗███████╗
    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██╔════╝╚██╗ ██╔╝██╔════╝
    ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   █████╗   ╚████╔╝ █████╗  
    ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██╔══╝    ╚██╔╝  ██╔══╝  
    ╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ███████╗   ██║   ███████╗
     ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚══════╝   ╚═╝   ╚══════╝
      (Automatic OPENVPN Client Creator)             written by: martiaga                                                 
    ''')
    main_question = input('Did you run the script in SUDO mode? (y/n): ')
    if main_question == 'y':
        nome_cliente = input('Digite o nome do cliente: ')
        diretorio_pki = f'{home_directory}/openvpn/easy-rsa/pki/'
        diretorio_private = f'{home_directory}/openvpn/easy-rsa/pki/private/'
        diretorio_issued = f'{home_directory}/openvpn/easy-rsa/pki/issued/'
        os.chown(diretorio_pki, 1000, 1000)
        os.chown(diretorio_private, 1000, 1000)
        os.chown(diretorio_issued, 1000, 1000)
        os.chdir(f'{home_directory}/openvpn/easy-rsa/')
        os.system(f'sudo sh easyrsa gen-req {nome_cliente} nopass')
        os.system(f'sudo sh easyrsa sign-req client {nome_cliente}')
        os.chdir(f'{home_directory}/openvpn/easy-rsa/pki/')
        os.system(f'openvpn --tls-crypt-v2 private/vpn_server.pem --genkey tls-crypt-v2-client private/{nome_cliente}.pem')
        os.system(f'mkdir {home_directory}/openvpn/vpn_clients')
        os.system(f'mkdir {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/ca.crt {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/issued/{nome_cliente}.crt {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/private/{nome_cliente}.key {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.system(f'sudo cp {home_directory}/openvpn/easy-rsa/pki/private/{nome_cliente}.pem {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.chown(diretorio_pki, 0, 0)
        os.chown(diretorio_private, 0, 0)
        os.chown(diretorio_issued, 0, 0)
        scriptOVPN()
        os.system(f'sudo cp {home_directory}/openvpn/scripts/ovpn_creator.sh {home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.chdir(f'{home_directory}/openvpn/vpn_clients/{nome_cliente}')
        os.system(f'sudo ./ovpn_creator.sh {nome_cliente}')
    else:
        exit()


if __name__ == '__main__':
    configClient()