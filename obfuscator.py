#!/usr/bin/python

import argparse, sys, time
from socket import gethostbyname, gaierror


banner = '''
       __   ___                  __
 ___  / /  / _/_ _____ _______ _/ /____  ____
/ _ \/ _ \/ _/ // (_-</ __/ _ `/ __/ _ \/ __/
\___/_.__/_/ \_,_/___/\__/\_,_/\__/\___/_/

| Author : Mr. Pixelheartz
| Url/IP obfuscator
| Tool untuk meng-obfuscate ip/url
| e.g. : obfuscator.py google.com --mode=hex
'''

# -------------------- KONVERSI BILANGAN -------------------------

def int_hex(integerNum):
    ipList = [hex(int(n)) for n in integerNum]
    result = '.'.join(ipList)

    print "[+] Obfuscating",
    sys.stdout.flush()
    for i in range(3):
        print ".",
        sys.stdout.flush()
        time.sleep(1.0)

    print "\n[+] Hasil : http://" + result


def int_oct(integerNum):
    ipList = [oct(int(n)) for n in integerNum]
    result = '.'.join(ipList)

    print "[+] Obfuscating",
    sys.stdout.flush()
    for i in range(3):
        print ".",
        sys.stdout.flush()
        time.sleep(1.0)

    print "\n[+] Hasil : http://" + result


def int_undottedInt(integerNum):
    slotOne = int(integerNum[0]) * 16777216
    slotTwo = int(integerNum[1]) * 65536
    slotThree = int(integerNum[2]) * 256
    slotFour = int(integerNum[3])
    result = slotOne + slotTwo + slotThree + slotFour

    print "[+] Obfuscating",
    sys.stdout.flush()
    for i in range(3):
        print ".",
        sys.stdout.flush()
        time.sleep(1.0)

    print "\n[+] Hasil : http://" + str(result)


def int_undottedOct(integerNum):
    slotOne = int(integerNum[0]) * 16777216
    slotTwo = int(integerNum[1]) * 65536
    slotThree = int(integerNum[2]) * 256
    slotFour = int(integerNum[3])
    result = slotOne + slotTwo + slotThree + slotFour

    print "[+] Obfuscating",
    sys.stdout.flush()
    for i in range(3):
        print ".",
        sys.stdout.flush()
        time.sleep(1.0)

    print "\n[+] Hasil : http://" + str(oct(result))


def int_undottedHex(integerNum):
    slotOne = int(integerNum[0]) * 16777216
    slotTwo = int(integerNum[1]) * 65536
    slotThree = int(integerNum[2]) * 256
    slotFour = int(integerNum[3])
    result = slotOne + slotTwo + slotThree + slotFour

    print "[+] Obfuscating",
    sys.stdout.flush()
    for i in range(3):
        print ".",
        sys.stdout.flush()
        time.sleep(1.0)

    print "\n[+] Hasil : http://" + str(hex(result))


# ------------------------- SYSTEM ----------------------------

def obfuscating(num):
    try:
        if (args.mode == 'hex'):
            int_hex(num)
        elif (args.mode == 'octal'):
            int_oct(num)
        elif (args.mode == 'undottedInt'):
            int_undottedInt(num)
        elif (args.mode == 'undottedOct'):
            int_undottedOct(num)
        elif (args.mode == 'undottedHex'):
            int_undottedHex(num)
        else:
            print "[-] Nothing happened!"
    except KeyboardInterrupt:
        print "[-] Keluar",
        sys.stdout.flush()
        for i in range(3):
            print ".",
            sys.stdout.flush()
            time.sleep(1.0)
        exit()


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
    # mengecek apakah string mengandung angka


def splitIP(ip):
    splitIp = ip.split(".")
    if len(splitIp) == 4:
        for i in splitIp:
            if (int(i) >= 0 and int(i) <= 256):
                obfuscating(splitIp)
                break
            else:
                print "[!] Pastikan format ip anda benar!"
                break


def main():
    addr = args.host
    if hasNumbers(addr):
        splitIP(addr)
    else:
        try:
            addr = gethostbyname(addr)
            splitIP(addr)
        except gaierror:
            print "[!] Gagal mendapatkan IP target.\n"
        except KeyboardInterrupt:
            print "[-] Keluar",
            sys.stdout.flush()
            for i in range(3):
                print ".",
                sys.stdout.flush()
                time.sleep(1.0)
            exit()
        except ImportError:
            print "[-] Terjadi kesalahan."

if __name__ == '__main__':
    print banner

    parser = argparse.ArgumentParser(description="This tool is used for obfuscating ip/url address.")
    parser.add_argument("host", help="e.g. : google.com or 1.1.1.1", type=str)
    parser.add_argument("--mode", "-m", type=str, default="undottedInt", help="Obfuscate host into [hexa] [octal] [undottedInt] [undottedHex] [undottedOct]")
    args = parser.parse_args()

    main()
