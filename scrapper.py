# Author: Pari Malam
import requests
from colorama import Fore, Style

def banners():
    print(f"""{Style.BRIGHT + Fore.RED}
    ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
    ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
    ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
    ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                                
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.BRIGHT + Fore.YELLOW}  
    Coded By       :     Pari Malam
    Description    :     Proxy Auto Scrapper [#OpsPETIR CyberTroopers]


    Forum          :      https://dragonforce.io
    Github         :      https://github.com/Pari-Malam
    Telegram       :      https://telegram.me/DragonForceIO     I think, ur face got problemo? hehe boiss :P
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
banners()

options = {
    1: {"country": "all", "timeout": "750"},
    2: {"country": "US", "timeout": "750"},
    3: {"country": "RU", "timeout": "1000"},
    4: {"country": "UA", "timeout": "1000"},
    5: {"country": "IN", "timeout": "1000"},
    6: {"country": "IT", "timeout": "1000"},
    7: {"country": "CA", "timeout": "1000"},
    8: {"country": "FR", "timeout": "1000"},
    9: {"country": "TH", "timeout": "1000"},
    10: {"country": "PL", "timeout": "1000"},
    11: {"country": "NL", "timeout": "2100"},
    12: {"country": "MX", "timeout": "1500"},
    13: {"country": "KZ", "timeout": "1500"},
    14: {"country": "IR", "timeout": "1500"},
    15: {"country": "EG", "timeout": "1500"},
    16: {"country": "HK", "timeout": "2250"},
    17: {"country": "DE", "timeout": "1500"},
    18: {"country": "VN", "timeout": "1500"},
    19: {"country": "HU", "timeout": "1500"},
    20: {"country": "BR", "timeout": "1500"},
    21: {"country": "JP", "timeout": "1500"},
    22: {"country": "KH", "timeout": "1500"},
    23: {"country": "CN", "timeout": "1250"}
}

while True:
    country_code = input(f"{Fore.GREEN}\nEnter a country code (type 'all' for all countries): {Style.RESET_ALL}")
    if country_code == "all" or country_code.upper() in options.values():
        break
    print(f"{Fore.RED}Invalid country code, please try again.{Style.RESET_ALL}")

while True:
    try:
        print(f"{Fore.RED}{'Options:':<10}{'Country':<10}{'Timeout':<10}{Style.RESET_ALL}")
        for op, option in options.items():
            print(f"{Fore.GREEN}{op:<10}{option['country']:<10}{option['timeout']:<10}{Style.RESET_ALL}")
        op = int(input(f"{Fore.CYAN}Enter an option - [1-23]: {Style.RESET_ALL}"))
        if op in options:
            break
        print(f"{Fore.RED}Invalid option, please try again.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input, please try again.{Style.RESET_ALL}")

url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout={options[op]['timeout']}&country={options[op]['country']}"
proxies = requests.get(url).text

with open("proxy.txt", "w") as f:
    f.write(proxies)

print(f"{Fore.GREEN}Proxies saved to 'proxy.txt'.{Style.RESET_ALL}")