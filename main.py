import asyncio
import os
import sys
import random
from pyrogram import Client, errors, raw, types

# --- COLORS ---
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[0m'

# --- API CONFIG (Official Desktop) ---
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

REPORT_MESSAGES = [
    "This user is spreading malicious content and spam.",
    "Harassment and community guideline violation.",
    "Promoting illegal activities and scams.",
    "Inappropriate behavior and abusive language.",
    "Spreading fake news and impersonating others."
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
    print(f"{Y}        [ STATUS: SECURE | BUG FIXED: ATTRIBUTE ]{W}\n")

async def main():
    banner()
    # Session file locally store hogi
    app = Client("ronak_final_v4", api_id=API_ID, api_hash=API_HASH)
    
    await app.connect()
    
    # User data fetch karne ka try karein
    user_me = await app.get_me()

    if not user_me:
        print(f"{Y}[!] Login Protocol Initiated...{W}")
        phone = input(f"{G}┌─[Enter Phone Number (with + Country Code)]\n└──╼ {W}").strip()
        try:
            sent_code = await app.send_code(phone)
            print(f"\n{C}[*] OTP Sent! Check your Telegram App.{W}")
            otp = input(f"{G}┌─[Enter OTP Code]\n└──╼ {W}").strip()
            try:
                user_me = await app.sign_in(phone, sent_code.phone_code_hash, otp)
            except errors.SessionPasswordNeeded:
                pwd = input(f"{G}┌─[Enter 2FA Password]\n└──╼ {W}").strip()
                user_me = await app.check_password(pwd)
        except Exception as e:
            print(f"\n{R}❌ Login Error: {e}{W}")
            await app.disconnect()
            return

    # Double check agar login abhi bhi None hai
    if not user_me:
        user_me = await app.get_me()

    banner()
    # Ab 'user_me' use karein 'app.me' ki jagah
    print(f"{G}✅ ACCESS GRANTED: {user_me.first_name if user_me else 'User'}{W}\n")
    
    target = input(f"{G}┌─[Target Username or ID]\n└──╼ {W}").strip()
    
    print(f"\n{C}[ SELECT ATTACK REASON ]{W}")
    print(f"{R}1. Spam   2. Violence   3. Child Abuse   4. Other{W}")
    choice = input(f"{G}└──╼ {W}Select: ")
    
    reasons = {"1": types.InputReportReasonSpam(), "2": types.InputReportReasonViolence(), 
               "3": types.InputReportReasonChildAbuse(), "4": types.InputReportReasonOther()}
    
    selected_reason = reasons.get(choice, reasons["1"])
    
    try:
        count = int(input(f"{G}┌─[Intensity (1-1000)]\n└──╼ {W}Count: "))
    except:
        count = 100

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
            except:
                continue

        print(f"\n\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}✅ REPORT COMPLETED SUCCESSFULLY!")
        print(f"{R}🚀 RONAK REPORT TOOL 🚀")
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
        input(f"\n{C}Press Enter to Exit...{W}")
        
    except Exception as e:
        print(f"{R}❌ Target Error: {str(e)}{W}")
    finally:
        await app.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    
