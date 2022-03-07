from dhooks import Webhook
from colorama import Fore

hook = Webhook("https://discord.com/api/webhooks/950213714311786536/bn32vlQE8NSlPiJowi1-q1xgASNFcRWY7l--uP1R3DUfhEGllEI2HlxBejmx3oCricc3")

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

name = input(Fore.CYAN + "1. Introduce tu nombre: ")

data = input(Fore.CYAN + "2. Introduce el mensaje: ")

hook.send(name + "   `>>`   " + data)
