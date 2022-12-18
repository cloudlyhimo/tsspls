from rich.console import Console
from rich.table import Table
import os

def main():
    appleid = input(str("[*] Enter Apple Id: "))
    passforappleid = input(str("[*] Enter Password for apple Id: "))
    udid = input(str("[*] Input UDID your Device\n(to view udid use ./usbmuxd.sh, example: with serial number c9a6be55a912): "))
    os.system("clear")
    info = Table(title="Inputed Information")
    info.add_column("Info", justify="center", style="cyan", no_wrap=True)
    info.add_column("Inputed", justify="center")
    info.add_row("Apple Id", appleid)
    info.add_row("Password for Apple Id", passforappleid)
    info.add_row("UDID", udid)
    console = Console()
    console.print(info)
    with open("arch.txt") as txt:
        if "x86_64" in txt.read():
            try:
                os.system(f"sudo ./AltServer-x86_64 -u {udid} -a {appleid} -p {passforappleid}")
            except:
                print("[*] Error Occured")
        elif "armv7" in txt.read():
            try:
                os.system(f"sudo ./AltServer-armv7 -u {udid} -a {appleid} -p {passforappleid}")
            except:
                print("[*] Error Occured")
        elif "aarch64" in txt.read():
            try:
                os.system(f"sudo ./AltServer-aarch64 -u {udid} -a {appleid} -p {passforappleid}")
            except:
                print("[*] Error Occured")
        elif "i586" in txt.read():
            try:
                os.system(f"sudo ./AltServer-i586-u {udid} -a {appleid} -p {passforappleid}")
            except:
                print("[*] Error Occured")

if __name__ == "__main__":
    main()
