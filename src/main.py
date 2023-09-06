from colorama import Fore
from requests import get
from random import randint
import os, time, signal, readchar, sys
from sys import exit

# TITLE_LOLCAT=f"{os.system('lolcat ./title.txt')}\n".replace('0', '')
COUNTRIES = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina faso', 'Burundi', 'Cabo verde', 'Cambodia', 'Cameroon', 'Canada', 'Central african republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Democratic republic of the congo', 'Republic of the congo', 'Costa rica', 'Ivory Coast', 'Croatia', 'Cuba', 'Cyprus', 'Czech republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan']

INFO_C = f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]"
QUESTION_C = f"[{Fore.LIGHTBLUE_EX}?{Fore.RESET}]"
WIN_C = f"[{Fore.LIGHTGREEN_EX}${Fore.RESET}]"
CTRL_C = "\u0003"

user_points = 0

# api get
def get_country(query):
    curUrl = f'https://restcountries.com/v3.1/name/{str(query).lower()}?fields=name,flags'
    response = get(curUrl).json()[0]
    if (response == "404"):
        return 0

    curFlag = response["flags"]["png"]
    curName = response["name"]["common"]

    return [curName, curFlag]

# quit
def handler_quit(signum, frame):
    print(Fore.RESET)

    os.system("clear")
    exit(1)

# list command
def show_list():
    os.system("clear")
    for cc in COUNTRIES:
        signal.signal(signal.SIGINT, handler_quit)
        curC = get_country(cc.lower())
        
        print(f"{os.system(f'jp2a --height=20 --colors {curC[1]}')}".replace("0", ""))
        print(f"{INFO_C} Name: {curC[0]}\t")
        
        print(f"< {str(COUNTRIES.index(cc.capitalize()))}/{str(len(COUNTRIES))} > (Q/E) ", end="", flush=True)
        res = readchar.readchar()

        while res != "q" and res != "e" and res != CTRL_C:
            res = readchar.readchar()
        
        # quit list
        if res == CTRL_C:
            os.system("clear")
            exit(1)

        os.system("clear")

# help command
def help_cmd():
    msg = f"""Usage: wfg.sh [options]
{WIN_C} Options:

-l, --list \t\tEnter list mode, displaying each one of all countries in the world, with their names. 
           \t\tGood for knowlege.
-h, --help \t\tDisplays this message.

For more information, access https://github.com/nandooxzz/world-flags-guesser
"""

    print(msg, end="")
    exit(1)

# check console line arguments
if len(sys.argv) > 1:
    cmd = str(sys.argv[1]).lower()
    if cmd == "--list" or cmd == "-l":
        show_list()
    elif cmd == "--help" or cmd == "-h":
        help_cmd()

# randomCountryIndex = randint(0, len(countries))
TITLE_LOLCAT=f"{os.system('lolcat /usr/share/world-flags-guesser/title.txt')}\n".replace('0', '')
signal.signal(signal.SIGINT, handler_quit)
print(TITLE_LOLCAT)
print(f'{INFO_C} Welcome to World Flags guesser!'+Fore.RESET)
print(f"{INFO_C} Game starting in 5 seconds! Be ready"+Fore.RESET)
time.sleep(5)

os.system("clear")

while user_points < 100:
    signal.signal(signal.SIGINT, handler_quit)
    randomCountry = randint(0, len(COUNTRIES)-1)
    curCountry = get_country(COUNTRIES[randomCountry])
    if(curCountry == 0): pass
    curFlag = f"{os.system(f'jp2a --colors {curCountry[1]}')}".replace("0", "")

    print(curFlag+"\n")
    user_guess = str(input(Fore.RESET+f"{QUESTION_C} What's the country?: "))

    while len(user_guess) <= 0:
        user_guess = str(input(Fore.RESET+f"{QUESTION_C} What's the country?: "))

    while not (user_guess.lower() == str(curCountry[0]).lower()):
        time.sleep(1)
        user_points -= 5
        if user_points <= 0: break # loose 

        print(Fore.LIGHTRED_EX+"Incorrect Guess! -5 \t\tPoints: "+str(user_points)+Fore.RESET)
        time.sleep(1.15)
        
        os.system("clear")
        curFlag = f"{os.system(f'jp2a --colors {curCountry[1]}')}".replace("0", "")
        print(curFlag+"\n")
        user_guess = str(input(Fore.RESET+f"{QUESTION_C} What's the country?: "))
    else:
        time.sleep(1)
        user_points += 10
        print(Fore.LIGHTGREEN_EX+"Nice try! +10\t\tPoints: "+str(user_points)+Fore.RESET)
        time.sleep(1.15)
        pass

    if (user_points >= 100) or (user_points <= 0):
        msg = ""
        if user_points >= 100:
            msg = Fore.RESET+f"{WIN_C} Yay! You won! Wanna try again? (y/n): "
        elif user_points <= 0 :
            msg = Fore.RESET+f"{INFO_C} You've lost! Wanna try again? (y/n): "

        print(msg, end="", flush=True)
        res = readchar.readchar()
        if res == "y": 
            user_points = 0
            os.system("clear")
            pass
        else: 
            os.system("clear")
            print(Fore.RESET+f"{INFO_C} Bye bye!")
            exit(1)