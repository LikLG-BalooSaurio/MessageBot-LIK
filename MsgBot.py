from dhooks_lite import Webhook
import re
from colorama import Fore


hook = Webhook("https://discord.com/api/webhooks/950463373554876427/faJJXfXZr1ct6-uRIjK9ao55wxG37QrXt5Iul2KlO9maTG5tO2_BruJ3hI0FLbsq1ylO")


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
