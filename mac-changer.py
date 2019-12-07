#
# =======================================+SCRIPT BY Abdurrahman Faid+==============================================
#
# ====================================+github : www.github.com/abdurrhmanFaid=====================================
import sys
import os
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 400)


slowprint("[!] Starting MAC Changer : ")
os.system('clear')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)



def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)


slowprint('''\033[1;31m \033[91m    
       __  ___                 ________                               
      /  |/  /___ ______      / ____/ /_  ____ _____  ____ ____  _____
     / /|_/ / __ `/ ___/_____/ /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
    / /  / / /_/ / /__/_____/ /___/ / / / /_/ / / / / /_/ /  __/ /    
   /_/  /_/\__,_/\___/      \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                                                   /____/\033[97m             
''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 400)


slowprint("\t\t                                         \033[93mBy :A||F")
print(" ")
print("1- Show the current MAC-ADDRESS")
print("")
print("2- Change your MAC-ADDRESS Randomly")
print("")
print("3- Change your MAC-ADDRESS Customly")
print("")
print("4- Reset the original MAC-ADDRESS")
print(" ")
print("5- Why change MAC-ADDRESS")
print("")
af = input("\033[92m[?] \033[96mYour Choice ?[1:5] ==>")
if af == ('1'):
    print(" ")
    print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
    print("\033[94m2 \033[97m- \033[91meth0 \033[97m( Ethernet connection)")
    print(" ")
    lawla = input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
    if lawla == ('1'):
        slowprint("\033[97m")
        os.system('macchanger -s wlan0')
        print(" ")
        input('press any key to continue')
        os.system('clear')
        os.system('python3 mac-changer.py')
    if lawla == ('2'):
        slowprint("\033[97m")
        os.system('macchanger -s eth0')
        print(" ")
        allah = input('press any key to continue')
        os.system('clear')
        os.system('python3 mac-changer.py')

if af == ('2'):
    print(" ")
    print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
    print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
    print(" ")
    deuxs = input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
    if deuxs == ('2'):
        slowprint("")
        os.system('ifconfig eth0 down')
        os.system('macchanger -r eth0')
        os.system('ifconfig eth0 up')
        print(" ")
        hoho = input("press any key to continue")
        os.system('clear')
        os.system('python3 mac-changer.py')
    if deuxs == ('1'):
        slowprint("")
        os.system('ifconfig wlan0 down')
        os.system('macchanger -r wlan0')
        os.system('ifconfig wlan0 up')
        print(" ")
        hoho = input("press any key to continue")
        os.system('clear')
        os.system('python3 mac-changer.py')

if af == ('4'):
    print(" ")
    print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
    print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
    print(" ")
    talta = input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
    if talta == ('2'):
        print(" ")
        slowprint("\033[97m")
        os.system('macchanger -p eth0')
        print(" ")
        lopa = input("press any key to continue ")
        os.system('clear')
        os.system('python3 mac-changer.py')
    if talta == ('1'):
        print(" ")
        slowprint("\033[97m")
        os.system('ifconfig wlan0 down')
        os.system('macchanger -p wlan0')
        os.system('ifconfig wlan0 up')
        print(" ")
        lopa = input("press any key to continue ")
        os.system('clear')
        os.system('python3 mac-changer.py')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)


if af == ('5'):
    print("\033[97m")
    slowprint(''' 
Why You Need To Change MAC Address?
I have been asked many times this question, in person as well as over email. Many people are clueless that you can even change MAC address and give open challenges, so forget that they would know why there is a need to change a MAC address.

Some people think that websites on Internet can track users using MAC address and so they must change it! Well, your MAC address wont go further than the first router the IP packet gets to. Its because, MAC address is used as unique identifier at data link layer (OSI layer 2), like for example your local Ethernet, while the IP packet being forwarded over Internet is at network level (OSI layer 3) and uses IP Address as a global unique identifier (which websites can see and track). And when an Ethernet frame reaches a router, the router's MAC address is used to send the frame forward. So, clearly this is not a reason to change MAC address!

There are many reasons you would want change MAC address, some legitimate others not so. I am listing some of the legitimate reasons while you wonder what the other reasons might be!
Your ISP uses MAC address to identify or authenticate your Internet connection. So in case your network card goes boom, the new card you replace it with will have different MAC address and so the Internet wont work. So changing the MAC address to old network adapter is the quickest fix instead of telling your ISP to register your new MAC address which may take lot of time.

If you want to access a network, which limits access based on MAC address, from another machine then you can change MAC address to the one for which you have access. Note that only one computer would be able to access the same network (no two computers can have same MAC address on same network to access it without any problem)

A very important reason is privacy. Your MAC address can be seen by everyone on the local Ethernet network using many simple tools. A hacker on local network thus can track machines (and thus you) on the network. This is especially a threat when you are on a wireless network and are using a public WiFi network like in coffee shops, hotels or airports.

If your original MAC address is revealed, an hacker can use it to impersonate you! On many networks (wired or wireless) access is restricted based on MAC address to avoid access to unauthorized devices on the network. So, when you go offline, someone can use your machine's MAC address and access the network as 'you'.

You can get a new IP address lease from DHCP server by changing MAC address. On many networks, DHCP lease is set to last many days or is associated directly with a MAC address such that you get the same IP address all the time.

The reasons I listed above are just the ones that came to my mind while writing this post. There are many more reasons (sometime bizarre) to change MAC address.
               ''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)


if af == ('3'):
    print(" ")
    print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
    print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
    print(" ")
    data = input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
    if data == ('2'):
        print(" ")
        os.system('ifconfig eth0 down')
        dire = input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
        os.system('ifconfig eth0 down')
        os.system('macchanger -m' + (dire) + ' eth0')
        os.system('ifconfig eth0 up')
        print("done")
    if data == ('1'):
        os.system('ifconfig wlan0 down')
        print(" ")
        dire = input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
        os.system('ifconfig wlan0 down')
        os.system('macchanger -m' + (dire) + ' wlan0')
        os.system('ifconfig wlan0 up')
        print("done")

