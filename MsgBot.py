from dhooks_lite import Webhook
import re
from colorama import Fore


hook = Webhook("https://discord.com/api/webhooks/954460003618668586/QDbQw0x8ASww16gwczrxup1p2B261lQZW57s-EXwEpESFsooxMt5XYyDywKsfvJU84cu")


print(Fore.CYAN + """
█████████████████████████████████████▀██████████████████████████
█▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█─▄▄▄▄██▀▄─██─▄▄▄▄█▄─▄▄─███▄─▄─▀█─▄▄─█─▄─▄─█
██─█▄█─███─▄█▀█▄▄▄▄─█▄▄▄▄─██─▀─██─██▄─██─▄█▀████─▄─▀█─██─███─███
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀
""")


print(Fore.RED + """
                                                    ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                    ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                    ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
                                                    
                                                    
""")

name = input(Fore.LIGHTCYAN_EX + "1. Introduce tu nombre: ")

mensaje = input(Fore.LIGHTCYAN_EX + "2. Introduce el mensaje: ")

censura = ("http")


if re.search(censura, name) is not None:
    print(Fore.RED + "No puedes colocar links en tu nombre")
    exit()

if re.search(censura, mensaje) is not None:
    print(Fore.RED + "No puedes colocar links en tu mensaje")
    exit()

else:
    hook.execute(name + ' **>>** ' + mensaje)
    print(Fore.LIGHTWHITE_EX + "Listo! Mensaje enviado... Revisa el discord!")
