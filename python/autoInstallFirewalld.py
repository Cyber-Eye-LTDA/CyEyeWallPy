import os
import sys

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def auto_install():
    print('INICIANDO AUTO INSTALL')
    os.system('sudo apt update && sudo apt upgrade -y')
    packages = ['python3', 'python3-dbus', 'python3-gobject', 'python3-nftables',
                'ipset', 'iptables', 'polkitd', 'python3-cap-ng', 'firewalld']
    
    print("\nInstalling dependencies:")
    for _ in progressbar(range(len(packages)), prefix='Progress:', size=40):
        package = packages[_]
        os.system(f'sudo apt install {package} -qq -y 2>/dev/null')
    
    os.system('sudo systemctl enable firewalld 2>/dev/null && sudo systemctl start firewalld 2>/dev/null')

    print("\nINSTALL COMPLETO.")
