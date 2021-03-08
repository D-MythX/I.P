import os
import time
import socket
import subprocess
import signal
import sys

y = "\033[2;33m"
g = "\033[2;32m"
p = "\033[2;35m"
w = "\033[2;37m"
r = "\033[2;31m"
e = "\033[0m"
u = "\033[4m"
fr = "\033[2;41m"
B = "\033[2;01m"
a = socket.gethostname()
b = socket.gethostbyname(a)

os.system('clear')
print(g+"•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×••")
time.sleep(1.0)
print(y+"✰  Internet Protocol Address.  "+g+"|")
time.sleep(1.0)
print(g+"•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•|")
time.sleep(1.0)
print(y+"✰     Author »» D~MYTH.  "+g+"      |")
time.sleep(1.0)
print(g+"×•×•×•×•×•×•×•×•×•×•××•×•×•×•×•|")
time.sleep(1.0)
print(y+"✰ Team »» TermuxHackz Society. "+g+"|")
time.sleep(1.0)
print(g+"×•×•×•×•×•×•×•×•×•×•××•×•×•×•×••")
time.sleep(1.0)

print(" \033[2;33m           ___________   ________  \033[0m")
time.sleep(0.5)
print(" \033[2;32m          (___     ___) |    __  \ ")
time.sleep(0.5)
print("  \033[2;33m             |   |     |   (__)  )\033[0m ")
time.sleep(0.5)
print("   \033[2;32m            |   |     |   _____/\033[0m")
time.sleep(0.5)
print("\033[2;33m            ___|   |___ _|  |\033[0m ")
time.sleep(0.5)
print(" \033[2;32m          (___________(_)__| \033[2;35m(v0.1)\033[0m")
time.sleep(1.0)
print(y+" ______________________________________________")
time.sleep(0.5)
print(B+r+"\n["+w+"!"+r+"] "+u+"DISCLAIMER"+e+":"+B+r+" Developers Assume No liability And Are Not Responsible For Any Misuse And Damage Caused By This Project.\n")
time.sleep(1.0)
print(B+r+"["+w+"!"+r+"] Please Be Wise! Use It Legally and Stay safe!"+e)
time.sleep(0.5)
print(y+" ______________________________________________")
time.sleep(2.0)
while True:
    print(g+"\n--➣ Enter option:  ")
    time.sleep(0.3)
    print("["+w+"01"+g+"]"+y+" Definition of Internet Protocol(IP Address).")
    time.sleep(0.3)
    print(g+"["+w+"02"+g+"]"+y+" Introduction to DDoS and other related topics.")
    time.sleep(0.3)
    print(g+"["+w+"03"+g+"]"+y+" My Hostname.")
    time.sleep(0.3)
    print(g+"["+w+"04"+g+"]"+y+" Find my IP Address.")
    time.sleep(0.3)
    print(g+"["+w+"05"+g+"]"+y+" Find my IP Address 2.")
    time.sleep(0.3)
    print(g+"["+w+"06"+g+"]"+y+" Trace IP addresses including mine.")
    time.sleep(0.3)
    print(g+"["+w+"07"+g+"]"+y+" Find a website IP Address.")
    time.sleep(0.3)
    print(g+"["+w+"08"+g+"]"+y+" DoS/DDoS"+r+" ULTRA. "+y+"(Xerxes2)")
    time.sleep(0.3)
    print(g+"["+w+"09"+g+"]"+y+" Update.(Do this frequently!)")
    time.sleep(0.3)
    print(g+"["+w+"10"+g+"]"+y+" Quit.")
    time.sleep(0.3)
    c = input(g+"--➢ ")
    if c == "1" or c == "01" :
        os.system("figlet *I.P Intro* | lolcat")
        time.sleep(1.0)
        print(g+"\n["+w+"*"+g+"]"+y+" The Internet Protocol (IP) is the principal communications protocol in the Internet protocol suite for relaying datagrams across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet(WIKI). Brief!")
        time.sleep(1.0)
        print(g+"\n["+w+"*"+g+"]"+y+" Always keep your IP address safe, because when they get into the hands of an hacker...smfh, lots of exploits can be done.")
        time.sleep(1.0)
        print(g+"\n["+w+"*"+g+"]"+y+" I can help you discover your IP address and trace IP addresses in option "+g+"["+w+"04"+g+"]"+y+"/"+g+"["+w+"05"+g+"]"+y+" and "+g+"["+w+"06"+g+"]"+y+" respectively.....Let's get Rolling!👍")
        time.sleep(5.0)
    elif c == "2" or c == "02" :
        os.system("figlet DDoS Intro | lolcat")
        time.sleep(1.0)
        print(g+"\n["+w+"*"+g+"]"+y+" DoS: (Denial of Service attack) done with a single computer(OS) and takes time\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" DDoS: (Distributed Denial of Service attack) done with several computer(OS) for a quick and effective attack\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" In a simple definition, this attack is done to bring down a website by loading it with thousands of packets or data in seconds more than what it can compile there by weakening it till it's temporarily or permanently offline and unavailable to legitimate users.\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" If eventually you were successful DoS(ing) a weak website alone, it might still come up after few minutes and that is why it is advisable to DDoS with friends and several OS loading a single site at a time!\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" Not all sites are vulnerable to this attack, so it's also advisable to check for vulnerabilities before proceeding, there are several tools for that, go on your research......Good luck! :)\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" Also, some site are built or protected from this attack with DDoS protector like CloudFare, so you can go on your research to check if it's bypassable.....Good luck! :)\n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" Now, I can help you Find a Website IP address and run a DDoS attack on it with a very fast tool in option "+g+"["+w+"07"+g+"]"+y+" and "+g+"["+w+"08"+g+"]"+y+" respectively...Let's get Rolling! 👍")
        time.sleep(5.0)
    elif c == "3" or c == "03" :
        os.system("figlet Hostname| lolcat")
        time.sleep(1.0)
        print(r+"["+w+"•"+r+"] PROCESSING...")
        time.sleep(3.0)
        print(g+"["+w+"✓"+g+"]"+y+" FOUND IT!\n")
        time.sleep(1.0)
        if a == 'localhost' :
            print(g+"["+w+"#"+g+"]"+y+" It seems you are using default.\n")
            time.sleep(1.0)
            print(g+"["+w+"✓"+g+"]"+y+" Your OS Hostname is"+p+" '"+a+"'"+y+".\n")
            time.sleep(1.0)
            print(g+"["+w+"@"+g+"]"+y+" You can visit "+w+"https://geekflare.com/how-to-change-hostname-in-linux/amp"+y+" to learn how to change the Hostname of your terminal (Limited to only Kali windows users and other similar OS because it seems impossible to change the Hostname of Termux).")
            time.sleep(5.0)
        else:
            os.system("figlet Hostname | lolcat")
            time.sleep(1.0)
            print(g+"["+w+"✓"+g+"]"+y+" Your OS Hostname is"+p+" '"+a+"'"+y+".\n")
            timesleep(3.0)
    elif c == "4" or c == "04" :
        os.system("figlet *My I.P* | lolcat")
        time.sleep(1.0)
        input(g+"["+w+"•"+g+"]"+y+" Please switch on your hotspot. If DONE, press enter to proceed •")
        print(r+"["+w+"•"+r+"] PROCESSING...")
        time.sleep(3.0)
        print(g+"["+w+"✓"+g+"]"+y+" DONE! \n")
        time.sleep(1.0)
        print(g+"["+w+"*"+g+"]"+y+" Your IP Address is"+p+" '"+b+"'"+y+".\n")
        time.sleep(2.5)
        if b == "127.0.0.1" :
            print(g+"["+w+"#"+g+"]"+y+" NOTE: "+p+"127.0.0.1"+y+" is the general loopback internet protocol (Hostname's IP). To get your personal IP, try again while Hotspot still active and if such still repeat itself, use option "+g+"["+w+"03"+g+"]"+y+".")
            time.sleep(5.0)
    elif c == "5" or c == "05" :
        os.system("figlet *My I.P2* | lolcat")
        time.sleep(1.0)
        input(g+"\n["+w+"~"+g+"]"+y+" Please switch on your hotspot. If you are using Kali windows, its not necessary. press enter to proceed")
        print(r+"["+w+"•"+r+"] PROCESSING...")
        time.sleep(3.0)
        print(g+"["+w+"✓"+g+"]"+y+" DONE! \n")
        time.sleep(1.0)
        try:
            os.system("ifconfig lo")
            time.sleep(1.0)
            print(g+"["+w+"#"+g+"]"+y+" NOTE: to identify your IP above, its just at the top left "+p+"''inet 192...'"+y+". (e.g "+p+" inet 192.168.44.2"+y+" or"+p+" inet addr:10.44.151.227"+y+")")
            time.sleep(5.0)
        except:
            os.system("ipconfig")
            time.sleep(3.0)
            print(g+"["+w+"#"+g+"]"+y+"NOTE: To identify your IP above, it's just under "+g+"Wireless LAN adapter "+y+"»» "+g+"IPv4 address "+y+"»» "+g+" Default Gateway"+y+".")
            time.sleep(5.0)
    elif c == "06" or c == "6" :
        os.system("figlet IP Tracer | lolcat")
        time.sleep(1.0)
        while True:
            print(g+" \n»»»"+y+" Select an option:")
            time.sleep(0.25)
            print(g+"["+w+"1"+g+"]"+y+" Trace my IP Address")
            time.sleep(0.25)
            print(g+"["+w+"2"+g+"]"+y+" Trace an IP Address")
            time.sleep(0.25)
            print(g+"["+w+"3"+g+"]"+y+" Go back.")
            time.sleep(0.25)
            d = input(g+" »»»"+y+"  ")
            if d == "1" or d == "01" :
                input(p+"\nIP Tracer "+g+">> "+y+"Make sure your data connection is switched on, press enter to proceed "+e)
                time.sleep(1.0)
                os.system(" trace -m ")
                time.sleep(0.5)
            elif d == "2" or d == "02" :
                input(p+" \nIP Tracer "+g+">>"+y+" Make sure your data connection is switched on, press enter to proceed "+e)
                while True:
                    time.sleep(0.5)
                    i = input(p+" \n            IP Address "+g+">>"+y+" ")
                    time.sleep(0.25)
                    print(g+"  \n          Verify «"+y+" "+i+" "+g+"» ?? ("+y+"Y"+g+"/"+y+"N"+g+")")
                    time.sleep(0.25)
                    j = input(p+"  \n              IP Tracer"+g+" >>"+y+" ")
                    if j == "Y" or j == "y" :
                        print(y+" "+e)
                        time.sleep(0.25)
                        os.system(" trace -t "+i+" ")
                        time.sleep(0.5)
                        break
                    elif j == "n" or j == "N":
                        time.sleep(0.25)
                        print(p+"        \n            IP Tracer"+g+" >>"+y+" Oops!")
                        continue
                    else:
                        time.sleep(0.25)
                        print(p+"    \n            IP Tracer"+g+" >> "+r+"Invalid! "+e)
                        continue
            elif d == "03" or d == "3" :
                    break
            else:
                time.sleep(0.25)
                print(r+"\n["+w+"×"+r+"] Invalid input")
    elif c == "7" or c == "07" :
        os.system("figlet Web IP | lolcat ")
        time.sleep(0.5)
        while True:
            print(g+"\n["+w+"1"+g+"]"+y+" Website IP Address.")
            time.sleep(0.3)
            print(g+"["+w+"2"+g+"]"+y+" Go back.")
            time.sleep(0.3)
            wo = input(g+"["+w+"+"+g+"]"+y+" Select option : ")
            if wo == "1" or wo == "01" :
                time.sleep(0.3)
                print(g+"\n["+w+"+"+g+"]"+y+" Name of website to find it's IP Address (host up), don't not include '"+p+"https://"+y+"'.")
                time.sleep(0.3)
                wi = input(g+" >>>"+y+" ")
                time.sleep(0.3)
                os.system(" nmap -v "+wi+" ")
                time.sleep(0.3)
                print(g+"\n["+w+"#"+g+"]"+y+" NOTE: To identify it's IP Address, check '"+p+"Discovered Open Port"+y+"'.")
            elif wo == "2" or wo == "02" :
                break
            else:
                time.sleep(0.3)
                print(r+"\n["+w+"×"+r+"] Invalid option.")
    elif c == "08" or c == "8" :
        os.system("figlet *DDoS* |lolcat ")
        time.sleep(0.3)
        while True:
            print(g+"["+w+"1"+g+"]"+y+" Launch an attack.")
            time.sleep(0.3)
            print(g+"["+w+"2"+g+"]"+y+" Go back to main menu.")
            time.sleep(0.3)
            wa = input(g+"["+w+"+"+g+"]"+y+" Select an option :")
            while True:
                if wa == "1" or wa == "01" :
                    time.sleep(0.3)
                    ai = input("\n       "+r+"      XERXES "+g+">>> "+y+"IPAddress :")
                    time.sleep(0.3)
                    va = input("\n      "+g+"       Verify «"+y+""+ai+""+g+"»?? ("+y+"Y"+g+"/"+y+"N"+g+"): ")
                    time.sleep(0.3)
                    if va == "y" or va == "Y" :
                        print("\n    "+r+"STAND BY!"+y+"...To break, press Ctrl C and manually launch tool"+r)
                        time.sleep(1.0)
                        os.system(" cd XERXES ")
                        os.sysyem(" ./xerxes "+ai+" 80")
                        input()
                        os.kill(signal.SIGNIT)
                    elif va == "n" or va == "N" :
                        print(" \n          "+r+"       XERXES "+g+">>> "+r+"Oops!")
                        continue
                    else:
                        print("\n      "+r+"         XERXES "+g+">>> "+r+"Invalid input.")
                elif wa == "2" or wa == "02":
                    break
                else:
                    print("\n      "+r+"         XERXES "+g+">>> "+r+"Invalid input.")
    elif c == "09" :
        os.system("clear")
        print(g+"UPDATING!!!..."+e)
        time.sleep(0.5)
        os.system(" cd $home ")
        os.system(" rm -rf I.P ")
        os.system(" git clone https://github.com/D-MythX/I.P ")
        os.system(" cd I.P ")
        os.system(" git clone https://github.com/XCHADXFAQ77X/XERXES ")
        os.system(" git clone https://github.com/rajkumardusad/IP-Tracer ")
        os.system("cd XERXES")
        os.system(" gcc -o xerxes xerxes.c ")
        os.system(" cd .. ")
        os.system(" cd IP-Tracer ")
        os.system(" chmod +x install ")
        os.system(" sh install ")
        os.system(" clear " )
        os.system(" cd .. ")
        time.sleep(1.0)
        os.system(" chmod +x * ")
        os.system(" python ip.py ")
        break
    elif c == "10" :
        print(g+"\n["+w+"~"+g+"]"+y+" Don't forget to update when next you launch this tool!")
        time.sleep(0.5)
        os.system("figlet *Bye* | lolcat")
        time.sleep(0.5) 
        print(g+"              •×•×•×•×•×•×•×•×•×•×•")
        time.sleep(1.0)
        print(y+"                   Credits to:      ")
        time.sleep(1.0)
        print(g+"          •×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•")
        time.sleep(1.0)
        print(y+"✰ AnonymousHack5 ✰ AnonymousX11-debug ✰ Ghost ✰")
        time.sleep(1.0)
        print(g+"•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•×•\n"+e)
        time.sleep(2.0)
        break
    else:
        print(r+"\n["+w+"×"+r+"] Invalid input!\n")
        time.sleep(1.0)
        
