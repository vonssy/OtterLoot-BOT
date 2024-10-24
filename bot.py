import requests
import json
import os
import random
from colorama import *
from datetime import datetime, timedelta
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class OtterLoot:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'otter-game-service.otterloot.io',
            'Origin': 'https://assets.otterloot.io',
            'Pragma': 'no-cache',
            'Referer': 'https://assets.otterloot.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Otter Loot - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def auth_login(self, query: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/auth/login'
        data = json.dumps({"initData":query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']['accessToken']
        else:
            return None
        
    def join(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/referral/join'
        data = json.dumps({"code":"6717c6fe2dabfb7a4785bf4b", "premium":False})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return True
        else:
            return False
        
    def user_profile(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/user/profile'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def item_user(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/item/user'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def game_info(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/game/info'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def game_spin(self, token: str, count: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/game/spin'
        data = json.dumps({'x':count})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None

    def game_steal(self, token: str, position: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/game/steal'
        data = json.dumps({'position':position})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None

    def raid_info(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/game/raid-info'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None

    def game_raid(self, token: str, raid_id: str, potition: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/game/raid'
        data = json.dumps({"userId":raid_id, "part":potition, "goldenPunch":True, "type":1})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def otter_info(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/otter'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def otter_cost(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/otter/cost'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def otter_repair(self, token: str, part_type: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/otter/repair'
        data = json.dumps({"part":part_type})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def otter_upgrade(self, token: str, part_type: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/otter/upgrade'
        data = json.dumps({"part":part_type})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def basic_quests(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/quest'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def do_basic(self, token: str, quest_id: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/quest/do'
        data = json.dumps({'questID': quest_id})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def special_quests(self, token: str):
        url = 'https://otter-game-service.otterloot.io/api/v1/special-quest'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def do_special(self, token: str, quest_id: int):
        url = 'https://otter-game-service.otterloot.io/api/v1/special-quest/do'
        data = json.dumps({'questID': quest_id})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['success']:
            return status['data']
        else:
            return None
        
    def question(self):
        while True:
            spin_otter = input("Auto Play Otter Loot Game Spin? [y/n] -> ").strip().lower()
            if spin_otter in ["y", "n"]:
                spin_otter = spin_otter == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to spin or 'n' to skip.{Style.RESET_ALL}")
        count = 0
        if spin_otter:
            while True:
                try:
                    count = int(input("Enter Energy Count per Spin [1, 2, 3] -> "))
                    if count in [1, 2, 3]:
                        break
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}Please enter 1, 2, or 3.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED+Style.BRIGHT}Invalid input. Enter a number.{Style.RESET_ALL}")

        while True:
            upgrade_otter = input("Auto Upgrade Otter Level? [y/n] -> ").strip().lower()
            if upgrade_otter in ["y", "n"]:
                upgrade_otter = upgrade_otter == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        
        return spin_otter, count, upgrade_otter

    def process_query(self, query: str, spin_otter: bool, count: int, upgrade_otter: bool):

        token = self.auth_login(query)

        if not token:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if token:
            self.join(token)
            user = self.user_profile(token)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

                quests = self.basic_quests(token)
                if quests:
                    for quest in quests['quests']:
                        quest_id = quest['questID']
                        status = quest['questStatus']

                        if quest and status == 1:
                            complete = self.do_basic(token, quest_id)
                            if complete:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {quest['description']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {quest['description']} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                quests = self.special_quests(token)
                if quests:
                    for quest in quests['quests']:
                        quest_id = quest['questID']
                        status = quest['questStatus']

                        if quest and status == 1:
                            complete = self.do_special(token, quest_id)
                            if complete:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {quest['description']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {quest['description']} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                items = self.item_user(token)
                if not items:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Item Info{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return

                if items:
                    coin = sum(item['amount']['value'] // 10000 for item in items if item['type'] == 3)
                    diamond = sum(item['amount']['value'] // 10000 for item in items if item['type'] == 4)

                info = self.game_info(token)
                if info:
                    energy = info['energy']
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Coin{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {coin} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Diamond{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {diamond} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Energy{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {energy}/{info['maxEnergy']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                    if spin_otter:
                        while energy > 0:
                            spin = self.game_spin(token, count)
                            if spin:
                                slots = spin.get('slots', [])
                                rewards = spin.get('sumRewards', [])
                                if not rewards and all(slot.get('item') == 5 for slot in slots):
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}] [{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} You Got a Game Steal {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                    time.sleep(1)

                                    used_positions = set()
                                    for _ in range(3):
                                        available_positions = [pos for pos in range(1, 5) if pos not in used_positions]
                                        if not available_positions:
                                            self.log(f"{Fore.YELLOW + Style.BRIGHT}[ No More Available Positions ]{Style.RESET_ALL}")
                                            break

                                        position = random.choice(available_positions)
                                        used_positions.add(position)

                                        steal = self.game_steal(token, position)
                                        if steal:
                                            self.log(
                                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Steal{Style.RESET_ALL}"
                                                f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT}] [ Position{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} {position} {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                            )
                                        time.sleep(1)

                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Game Steal{Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )

                                elif not rewards and all(slot.get('item') == 4 for slot in slots):
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}] [{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} You Got a Game Raid {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                    time.sleep(1)

                                    raid = self.raid_info(token)
                                    if raid:
                                        position = random.randint(1, 6)
                                        raid_id = raid['user']['id']
                                        name = raid['user']['firstName']

                                        punch = self.game_raid(token, raid_id, position)
                                        if punch and punch['success']:
                                            self.log(
                                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Raid{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} {name} {Style.RESET_ALL}"
                                                f"{Fore.GREEN + Style.BRIGHT}Was Punched{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Raid{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} {name} {Style.RESET_ALL}"
                                                f"{Fore.YELLOW + Style.BRIGHT}Wasn't Punched{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} Has a Shield {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                            )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Raid{Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}] {Style.RESET_ALL}"
                                        )

                                info = self.game_info(token)
                                if info:
                                    energy = info['energy']
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Remaining Energy{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {energy} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )

                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break
                            time.sleep(1)

                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Stopped {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Energy Depleted {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Otter{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Is Skipped {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Game Info{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                otter = self.otter_info(token)
                if not otter:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Otter{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return

                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Otter{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Level {otter['level']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                if upgrade_otter:
                    coin = sum(item['amount']['value'] // 10000 for item in self.item_user(token) if item['type'] == 3)
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Checked {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {coin} Coin {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    time.sleep(1)

                    costs = self.otter_cost(token)['costs']

                    for part in otter['parts']:
                        part_type = part['type']
                        stars = part['stars']

                        if stars >= 3:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Reached Max Upgarde{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} 3 Stars {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            continue

                        while stars < 3:
                            if part['broken']:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW + Style.BRIGHT}Is Broken{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} Starting Repairs... {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                
                                repair_cost_info = next(
                                    (c for c in costs if c['part'] == part_type), None
                                )
                                
                                if repair_cost_info:

                                    repair_amount = repair_cost_info['repair']['amount']['value'] // 10000

                                    if coin >= repair_amount:
                                        repair = self.otter_repair(token, part_type)
                                        if repair:
                                            self.log(
                                                f"{Fore.MAGENTA + Style.BRIGHT}[ Repair Otter{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                                f"{Fore.GREEN + Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Cost{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} {repair_amount} Coin {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                            )
                                            coin -= repair_amount

                                            otter = self.otter_info(token)
                                            part = next((p for p in otter['parts'] if p['type'] == part_type), None)
                                            if part:
                                                stars = part['stars']
                                            else:
                                                self.log(
                                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Repair Otter{Style.RESET_ALL}"
                                                    f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                                    f"{Fore.RED + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                                    f"{Fore.WHITE + Style.BRIGHT} Type {part_type} Not Found {Style.RESET_ALL}"
                                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                                )
                                                break
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA + Style.BRIGHT}[ Repair Otter{Style.RESET_ALL}"
                                                f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                                f"{Fore.RED + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                            break

                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Repair Otter{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                            f"{Fore.YELLOW + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                        break
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Repair Otter{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Can't Find Repair Cost {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                    break

                                time.sleep(1)

                            next_star = stars + 1
                            cost_info = next(
                                (c for c in costs if c['part'] == part_type and c['star'] == next_star), None
                            )
                            if not cost_info:
                                self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Can't Find Upgrade Cost {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                break

                            upgrade_amount = cost_info['upgrade']['amount']['value'] // 10000

                            if coin >= upgrade_amount:
                                upgarde = self.otter_upgrade(token, part_type)
                                if upgarde:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Cost{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {upgrade_amount} Coin {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )

                                    if upgarde['levelUp']:
                                        otter['level'] += 1
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT} Otter Level Up! {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Otter{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} Level {otter['level']} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                        break

                                    otter = self.otter_info(token)
                                    part = next((p for p in otter['parts'] if p['type'] == part_type), None)
                                    if part:
                                        stars = part['stars']
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} Type {part_type} Not Found {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                        break

                                    coin -= upgrade_amount
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                    break
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW + Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            print(
                                f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                                f"{Fore.YELLOW + Style.BRIGHT}Wait for{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} 3 Seconds to Next Upgrade {Style.RESET_ALL}",
                                end="\r",
                                flush=True
                            )
                            time.sleep(3)

                        if stars >= 3:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} Type {part_type} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Reached Max Upgarde{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {stars} Stars {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Upgrade Otter{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Is Skipped {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            spin_otter, count, upgrade_otter = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, spin_otter, count, upgrade_otter)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Otter Loot - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = OtterLoot()
    bot.main()