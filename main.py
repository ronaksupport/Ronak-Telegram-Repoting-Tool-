import asyncio
import os
import sys
import random
from pyrogram import Client, errors, raw, types

# --- API CONFIG ---
API_ID = 26233441
API_HASH = "8095b5465e94f107f9175402476d0590"

# --- COLORS ---
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[0m'

# --- REPORT TEXTS (All Types) ---
REPORT_MESSAGES = [
    "This user is spreading spam and malicious links.",
    "Promoting violence and illegal activities.",
    "Child abuse content detected, take immediate action.",
    "Harassment and abusive behavior towards others.",
    "Inappropriate content and community guideline violation.",
    "Scamming people and financial fraud.",
    "Terrorism promotion and hate speech."
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
    print(f"{Y}        [ ALL COUNTRIES SUPPORTED | OTP LOGIN ]{W}\n")

async def main():
    banner()
    app = Client("ronak_global_session", api_id=API_ID, api_hash=API_HASH)
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
            print(f"\n{C}[*] OTP sent to {phone}. Check your Telegram app.{W}")
            otp = input(f"{G}┌─[Enter Login OTP]\n└──╼ {W}").strip()
            try:
                await app.sign_in(phone, sent_code.phone_code_hash, otp)
            except errors.SessionPasswordNeeded:
                print(f"\n{R}[!] 2FA Encryption Detected!{W}")
                pwd = input(f"{G}┌─[Enter 2FA Password]\n└──╼ {W}").strip()
                await app.check_password(pwd)
        except Exception as e:
            print(f"\n{R}❌ Login Error: {e}{W}")
            return

    banner()
    print(f"{G}✅ System Access: {app.me.first_name} (@{app.me.username}){W}\n")
    
    target = input(f"{G}┌─[Target Username or ID]\n└──╼ {W}").strip()
    
    print(f"\n{C}[ SELECT ATTACK VECTOR ]{W}")
    print(f"{R}1. Mass Spam Hit   2. Violence   3. Child Abuse   4. Illegal{W}")
    choice = input(f"\n{G}└──╼ {W}Select (1-4): ")
    
    reasons = {
        "1": types.InputReportReasonSpam(),
        "2": types.InputReportReasonViolence(),
        "3": types.InputReportReasonChildAbuse(),
        "4": types.InputReportReasonOther()
    }
    
    selected_reason = reasons.get(choice, reasons["1"])
    
    try:
        limit = int(input(f"{G}┌─[Report Count (Max 1000)]\n└──╼ {W}Count: "))
    except:
        limit = 100

    print(f"\n{R}[🔥] ATTACK STARTED BY RONAK HACKER...{W}\n")
    
    try:
        peer = await app.resolve_peer(target)
        
        for i in range(1, limit + 1):
            random_msg = random.choice(REPORT_MESSAGES)
            try:
                # Raw reporting for bypass
                await app.invoke(
                    raw.functions.account.ReportPeer(
                        peer=peer,
                        reason=selected_reason,
                        message=random_msg
                    )
                )
                sys.stdout.write(f"\r{G}[HIT-{i}] {C}Injecting Payload | {R}Status: Reported{W}")
                sys.stdout.flush()
                
                # Speed control to avoid account ban
                if i % 50 == 0:
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(0.2)
                    
            except errors.FloodWait as e:
                print(f"\n{Y}[!] FloodWait: Sleeping {e.value}s{W}")
                await asyncio.sleep(e.value)
            except Exception:
                continue

        # Final Success Message
        print(f"\n\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}✅ TASK COMPLETED SUCCESSFULLY!")
        print(f"{R}🚀 RONAK REPORT TOOL 🚀")
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
        input(f"\n{C}Press Enter to Exit...
        
