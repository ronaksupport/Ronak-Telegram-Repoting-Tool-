import asyncio
import os
import sys
import time
from pyrogram import Client, filters, errors
from pyrogram.raw import functions, types

# --- CONFIG ---
API_ID = 32567928
API_HASH = "1ccc36ef5a82df3bba346bf9af66c143"

# --- COLORS ---
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{C}
    ██████╗  ██████╗ ███╗   ██╗  █████╗ ██╗  ██╗
    ██╔══██╗██╔═══██╗████╗  ██║ ██╔══██╗██║ ██╔╝
    ██████╔╝██║   ██║██╔██╗ ██║ ███████║█████╔╝ 
    ██╔══██╗██║   ██║██║╚██╗██║ ██╔══██║██╔═██╗ 
    ██║  ██║╚██████╔╝██║ ╚████║ ██║  ██║██║  ██╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    {Y}      >>> RONAK REPORT TOOL V1.0 <<<
    {G}   [+] POWERED BY: RONAK REPORT SYSTEM [+]
    {W}""")

async def main():
    banner()
    print(f"{C}[#] Ronak Report Tool - System Initialization...{W}")
    
    session = input(f"{Y}Enter Your String Session: {W}").strip()
    target = input(f"{Y}Enter Target (@username or ID): {W}").strip()
    
    print(f"\n{G}1. Spam\n2. Violence\n3. Child Abuse\n4. Other{W}")
    choice = input(f"{C}Select Reason (1-4): {W}")

    async with Client("ronak_session", api_id=API_ID, api_hash=API_HASH, session_string=session, in_memory=True) as app:
        try:
            peer = await app.resolve_peer(target)
            reasons = {"1": types.InputReportReasonSpam(), "2": types.InputReportReasonViolence(), 
                       "3": types.InputReportReasonChildAbuse(), "4": types.InputReportReasonOther()}
            
            print(f"\n{R}[!] Ronak Report Tool is hitting the target...{W}")
            for i in range(1, 6):
                await app.invoke(functions.account.ReportPeer(
                    peer=peer, reason=reasons.get(choice, reasons["1"]), 
                    message="Ronak Report Tool - Heavy Violation Report"
                ))
                print(f"{G}[+] Attack {i} Sent!{W}")
                await asyncio.sleep(1)
            
            print(f"\n{G}✅ Target {target} reported successfully by Ronak Tool!{W}")
        except Exception as e:
            print(f"{R}❌ Error: {e}{W}")

if __name__ == "__main__":
    asyncio.run(main())
