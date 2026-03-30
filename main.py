import asyncio
import os
import sys
import time
from pyrogram import Client, errors, types, functions
from datetime import datetime

# --- CONFIGURATION (Advanced Security) ---
API_ID = 32567928
API_HASH = "1ccc36ef5a82df3bba346bf9af66c143"

# --- PRO COLORS (CYBER THEME) ---
R = '\033[1;31m' # High Alert
G = '\033[1;32m' # Protocol Success
Y = '\033[1;33m' # System Warning
B = '\033[1;34m' # Deep Protocol
C = '\033[1;36m' # Cyber Cyan
W = '\033[0m'    # Reset

def clear():
    os.system('clear')

def pro_header(page):
    clear()
    print(f"{C}┌─────────────────────────────────────────────────────────┐")
    print(f"{C}│{R}  ██████╗  ██████╗ ███╗   ██╗ █████╗ ██╗  ██╗{C}            │")
    print(f"{C}│{R}  ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██║ ██╔╝{C}            │")
    print(f"{C}│{W}  ██████╔╝██║   ██║██╔██╗ ██║███████║█████╔╝ {C}            │")
    print(f"{C}│{W}  ██╔══██╗██║   ██║██║╚██╗██║██╔══██║██╔═██╗ {C}            │")
    print(f"{C}│{R}  ██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██╗{C}            │")
    print(f"{C}└─────────────────────────────────────────────────────────┘")
    print(f"{G}        [ PRO SYSTEM: RONAK HACKER - VERSION 4.0 ]")
    print(f"{Y}        [ STATUS: ENCRYPTED | MODULE: {page.upper()} ]")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n")

def slow_type(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

async def auth_protocol(client):
    pro_header("Auth Login")
    slow_type(f"{B}[*] Initializing Ronak Hacker Auth Protocol...{W}")
    phone = input(f"{G}┌─[Enter Phone (Ex: +9199xxxxxx)]\n└──╼ {W}").strip()
    
    try:
        code_data = await client.send_code(phone)
        hsh = code_data.phone_code_hash
        print(f"\n{Y}[!] Secure OTP sent via Telegram Cloud Service.{W}")
        
        otp = input(f"{G}┌─[Enter Binary OTP Code]\n└──╼ {W}").strip()
        
        try:
            await client.sign_in(phone, hsh, otp)
        except errors.SessionPasswordNeeded:
            print(f"\n{R}[!] 2FA Encryption Detected!{W}")
            pwd = input(f"{G}┌─[Enter 2FA Password]\n└──╼ {W}").strip()
            await client.check_password(pwd)
            
        print(f"\n{G}✅ [SUCCESS] Ronak Hacker Access Granted.{W}")
        time.sleep(1.5)
        return True
    except Exception as e:
        print(f"\n{R}❌ [FATAL ERROR] {str(e)}{W}")
        return False

async def start_attack():
    app = Client("ronak_pro_v4", api_id=API_ID, api_hash=API_HASH)
    await app.connect()
    
    # Session Persistence
    me = await app.get_me()
    if not me:
        if not await auth_protocol(app): return

    pro_header("Target Selector")
    target = input(f"{G}┌─[Enter Target ID/Username]\n└──╼ {W}").strip()
    
    print(f"\n{C}[ SELECT ATTACK VECTORS ]{W}")
    print(f"{R}1. MASS_SPAM_HIT       2. VIOLENCE_OVERRIDE")
    print(f"{R}3. CHILD_ABUSE_VEC     4. COPYRIGHT_STRIKE{W}")
    choice = input(f"\n{G}┌─[Ronak@Vector]\n└──╼ {W}Select Vector: ")
    
    try:
        intensity = int(input(f"{G}┌─[Attack Intensity (1-9999)]\n└──╼ {W}Count: "))
    except:
        intensity = 100

    pro_header("Reporting Engine")
    try:
        peer = await app.resolve_peer(target)
        reasons = {"1": types.InputReportReasonSpam(), "2": types.InputReportReasonViolence(),
                   "3": types.InputReportReasonChildAbuse(), "4": types.InputReportReasonOther()}
        
        vec = reasons.get(choice, reasons["1"])
        
        slow_type(f"{R}[!] Bypassing Telegram Trust & Safety Filters...{W}")
        slow_type(f"{B}[*] Injecting Ronak Hacker Payloads into {target}...{W}\n")
        
        for i in range(1, intensity + 1):
            try:
                # Pro Reporting Logic
                await app.invoke(
                    functions.account.ReportPeer(
                        peer=peer,
                        reason=vec,
                        message=f"Ronak Hacker System v4: Target violations detected on {datetime.now()}"
                    )
                )
                # Dynamic Logging
                sys.stdout.write(f"\r{G}[PRO-ATTACK-{i}] {C}Hit Successful | {R}Status: Bypass{W}")
                sys.stdout.flush()
                
                # Pro Speed (Adjustable)
                if i % 10 == 0: await asyncio.sleep(0.1)
                else: await asyncio.sleep(0.2)
                
            except errors.FloodWait as e:
                print(f"\n{Y}[!] Flood Detected! Waiting {e.value}s...{W}")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"\n{R}[!] Error on Hit {i}: {str(e)}{W}")

        print(f"\n\n{G}✅ [MISSION COMPLETE] Target {target} is now in Critical State.{W}")
        print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
        input(f"{Y}Press Enter to return to Command Center...{W}")

    except Exception as e:
        print(f"{R}❌ SYSTEM CRASH: {str(e)}{W}")

if __name__ == "__main__":
    try:
        asyncio.run(start_attack())
    except KeyboardInterrupt:
        print(f"\n{R}[!] Ronak Hacker System Shutdown.{W}")
