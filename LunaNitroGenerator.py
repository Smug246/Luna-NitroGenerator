# Coded with ❤ by Luna's Dev Team.

import ctypes
import string
import os
import time
import numpy
import requests

from discord_webhook import DiscordWebhook
from colorama import Fore

USE_WEBHOOK = True

VER = "1.0"

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')




url = "https://google.com"
try:
    response = requests.get(url)
    print(f"{Fore.MAGENTA}Internet check{Fore.RESET}")
    time.sleep(.4)
except requests.exceptions.ConnectionError:

    input(f"{Fore.MAGENTA}You are not connected to internet, check your connection and try again.\nPress enter to exit{Fore.RESET}")
    exit()


class NitroGen: 
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt": 
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator || Made by Luna Dev Team")  
        else:  
            print(f'Nitro Gen || Luna Dev Team',
                  end='', flush=True) 

        print(f"""{Fore.MAGENTA}
██╗     ██╗   ██╗███╗   ██╗ █████╗     ███╗   ██╗██╗████████╗██████╗  ██████╗        ██████╗ ███████╗███╗   ██╗
██║     ██║   ██║████╗  ██║██╔══██╗    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗      ██╔════╝ ██╔════╝████╗  ██║
██║     ██║   ██║██╔██╗ ██║███████║    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║     ██║   ██║██║╚██╗██║██╔══██║    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
███████╗╚██████╔╝██║ ╚████║██║  ██║    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝      ╚██████╔╝███████╗██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝{Fore.RESET}""")
        print(VER)
        time.sleep(2)  
        self.slowType(f"{Fore.MAGENTA}Made by Luna Dev Team{Fore.RESET}", .02)
        time.sleep(1) 
        self.slowType(
            f"{Fore.MAGENTA}\nInput How Many Codes to Generate and Check: {Fore.RESET}", .02, newLine=False)

        try:
            num = int(input('')) 
        except ValueError:
            input(f"{Fore.MAGENTA}Specified input wasn't a number.{Fore.RESET}")
            time.sleep(2)
            if not os.name == "nt":
                os.system("clear")
            else:
                os.system("cls")
            Gen.main()


        self.slowType(
            f"{Fore.MAGENTA}Please enter your webhook: {Fore.RESET}", .02, newLine=False)
        url = input('') 
        webhook = url

        if webhook == "":
            print(f"{Fore.MAGENTA}Please enter a valid webhook.{Fore.RESET}")
            time.sleep(2)
            if not os.name == "nt":
                os.system("clear")
            else:
                os.system("clr")
                Gen.main()


        if webhook is not None:
            DiscordWebhook(  
                    url=url,
                    content=f"```Started checking urls\nI will send any valid codes here```"
                ).execute()


        valid = []  
        invalid = 0 
        chars = []
        chars[:0] = string.ascii_letters + string.digits


        c = numpy.random.choice(chars, size=[num, 23])
        for s in c: 
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result: 
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
                DiscordWebhook(  
                    url=url,
                    content=f"```Stop checking, Interupted by user input```"
                ).execute()
                print(f"{Fore.MAGENTA}\nInterrupted by user{Fore.RESET}")
                break  

            except Exception as e:  
                DiscordWebhook( 
                    url=url,
                    content=f"```Stopped checking encountered an error.\nError || {e}```"
                ).execute()
                print(f"{Fore.MAGENTA} Error | {url} {Fore.RESET}")  

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Luna Dev Team") 
                print("")
            else: 
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Luna Dev Team\a', end='', flush=True)

        if len(valid) < 1:
            valid = "None"
        else:
            ', '.join(valid)

        print(f"""
Results:
 Valid: {len(valid) - 4}
 Invalid: {invalid}
 Valid Codes: {valid}""")  

        DiscordWebhook(  
                            url=url,
                            content=f"```Results:\n\nValid: {len(valid)}\nInvalid: {invalid}\nValid Codes: {valid}```"
                        ).execute()


        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]  


    def slowType(self, text: str, speed: float, newLine=True):
        for i in text: 
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200:  
            print(f"{Fore.MAGENTA} Valid | {nitro} {Fore.RESET}", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro)

            if notify is not None:
                DiscordWebhook( 
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True 

        else:
            print(f" {Fore.MAGENTA}Invalid | {nitro} {Fore.RESET}", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False 


if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main() 
