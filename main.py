import asyncio
import os
import sys
import random
from pyrogram import Client, errors, raw, types

# --- COLORS ---
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[0m'

# --- DEFAULT API (Official Telegram Desktop) ---
# Agar ye block ho jaye, toh tool user se mangega
DEFAULT_ID = 2040
DEFAULT_HASH = "b18441a1ff607e10a989891a5462e627"

REPORT_MESSAGES = [
    "Spreading prohibited content and malware.",
    "Harassment and cyber-bullying violation.",
    "Promoting illegal activities and scamming.",
    "Inappropriate profile and community guideline breach.",
    "User is impersonating others and spreading fake news."
]

def banner():
    os.system('clear')
    print(f"{C}┌─────────────────────────────────────────────────────────┐")
    print(f"{C}│{R}  ██████╗  ██████╗ ███╗   ██╗ █████╗ ██╗  ██╗{C}            │")
    print(f"{C}│{R}  ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██║ ██╔╝{C}            │")
    print(f"{C}│{W}  ██████╔╝██║   ██║██╔██╗ ██║███████║█████╔╝ {C}            │")
    print(f"{C}│{W}  ██╔══██╗██║   ██║██║╚██╗██║██╔══██║██╔═██╗ {C}            │")
    print(f"{C}│{R}  ██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██╗{C}            │")
    print(f"{C}└─────────────────────────────────────────────────────────┘")
    print(f"{G}        [ GLOBAL SYSTEM: RONAK HACKER - V4.0 ]")
    print(f"{Y}        [ ALL COUNTRIES SUPPORTED | FIXED API ]{W}\n")

async def main():
    banner()
    
    # API ID Check
    print(f"{C}[*] Initializing Secure Connection...{W}")
    api_id = DEFAULT_ID
    api_hash = DEFAULT_HASH

    app = Client("ronak_final_fix", api_id=api_id, api_hash=api_hash)
    
    try:
        await app.connect()
    except Exception:
        print(f"{R}[!] Default API Blocked. Please use your own API ID from my.telegram.org{W}")
        api_id = int(input(f"{G}Enter API ID: {W}"))
        api_hash = input(f"{G}Enter API HASH: {W}")
        app = Client("ronak_custom_session", api_id=api_id, api_hash=api_hash)
        await app.connect()

    try:
        me = await app.get_me()
    except:
        me = None

    if not me:
        print(f"{Y}[!] Login Protocol Initiated...{W}")
        phone = input(f"{G}┌─[Enter Phone Number (with + Country Code)]\n└──╼ {W}").strip()
        try:
            sent_code = await app.send_code(phone)
            print(f"\n{C}[*] OTP Sent! Check your Telegram App.{W}")
            otp = input(f"{G}┌─[Enter OTP Code]\n└──╼ {W}").strip()
            try:
                await app.sign_in(phone, sent_code.phone_code_hash, otp)
            except errors.SessionPasswordNeeded:
                pwd = input(f"{G}┌─[Enter 2FA Password]\n└──╼ {W}").strip()
                await app.check_password(pwd)
        except errors.ApiIdInvalid:
            print(f"{R}❌ Error: This API ID/HASH is invalid. Use a fresh one from my.telegram.org{W}")
            return
        except Exception as e:
            print(f"\n{R}❌ Login Error: {e}{W}")
            return

    banner()
    print(f"{G}✅ ACCESS GRANTED: {app.me.first_name}{W}\n")
    target = input(f"{G}┌─[Target Username or ID]\n└──╼ {W}").strip()
    
    print(f"\n{C}[ SELECT ATTACK REASON ]{W}")
    print(f"{R}1. Spam   2. Violence   3. Child Abuse   4. Other{W}")
    choice = input(f"{G}└──╼ {W}Select: ")
    
    reasons = {"1": types.InputReportReasonSpam(), "2": types.InputReportReasonViolence(), 
               "3": types.InputReportReasonChildAbuse(), "4": types.InputReportReasonOther()}
    
    selected_reason = reasons.get(choice, reasons["1"])
    count = int(input(f"{G}┌─[Intensity (1-1000)]\n└──╼ {W}Count: "))

    print(f"\n{R}[🔥] ATTACK INJECTED BY RONAK HACKER...{W}\n")
    try:
        peer = await app.resolve_peer(target)
        for i in range(1, count + 1):
            try:
                msg = random.choice(REPORT_MESSAGES)
                await app.invoke(raw.functions.account.ReportPeer(
                    peer=peer, reason=selected_reason, message=msg))
                sys.stdout.write(f"\r{G}[HIT-{i}] {C}Payload Sent | {R}Status: Reported{W}")
                sys.stdout.flush()
                await asyncio.sleep(0.1)
            except errors.FloodWait as e:
                await asyncio.sleep(e.value)
            except: continue

        print(f"\n\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}✅ REPORT COMPLETED SUCCESSFULLY!")
        print(f"{R}🚀 RONAK REPORT TOOL 🚀")
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
        input(f"\n{C}Press Enter to Exit...{W}")
    except Exception as e:
        print(f"{R}❌ Target Error: {str(e)}{W}")

if __name__ == "__main__":
    asyncio.run(main())
    
