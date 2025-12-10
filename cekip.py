import requests
from colorama import Fore
import time

login_usr = input("masukan password: ")
if login_usr == "agusganteng":
  pilih = input(Fore.BLUE + "1. lihat ip orang lain \n2. lihat ip sendiri \n pilih 1/2 : ")
  if pilih == "1":
    ip = input("MASUKAN IP TARGET: ")
    link = f"https://ifconfig.co/json?ip={ip}"
  
    data = requests.get(link, headers={"User-Agent": "curl"}).json()
  
    print(Fore.RED + """==========================
 HASIL DATA IP TARGET
==========================
  """)
    time.sleep(3)
    print(Fore.GREEN + "IP:", data.get("ip"))
    time.sleep(1)
    print("negara: ", data.get("country"))
    time.sleep(1)
    print("wilayah: ", data.get("region_name"))
    time.sleep(1)
    print("kota :", data.get("city"))
    time.sleep(1)
    print("zona waktu: ", data.get("time_zone"))
    time.sleep(1)
    print("penyedia jaringan: ", data.get("asn_org"))
  
  if pilih == "2":
    ceklink = f"https://ifconfig.co/json"
    data = requests.get(ceklink, headers={"User-Agent": "curl"}).json()
  
    print(Fore.RED + """==========================
HASIL DATA PERANGKAT
==========================
  """)
    time.sleep(3)
    print(Fore.GREEN + "IP:", data.get("ip"))
    time.sleep(1)
    print("negara: ", data.get("country"))
    time.sleep(1)
    print("wilayah: ", data.get("region_name"))
    time.sleep(1)
    print("kota :", data.get("city"))
    time.sleep(1)
    print("zona waktu: ", data.get("time_zone"))
    time.sleep(1)
    print("penyedia jaringan: ", data.get("asn_org"))
if login_usr != "agusganteng":
  print("passwordsalah")