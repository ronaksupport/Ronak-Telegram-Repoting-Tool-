import asyncio
import os
import sys
import random
from pyrogram import Client, errors, raw, types

# --- COLORS ---
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[0m'

# --- OFFICIAL API ---
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

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
    print(f"{Y}        [ FIX: AUTH_KEY_UNREGISTERED RESOLVED ]{W}\n")

async def main():
    banner()
    session_name = "ronak_v4_final"
    app = Client(session_name, api_id=API_ID, api_hash=API_HASH)
    
    try:
        await app.connect()
    except errors.AuthKeyUnregistered:
        print(f"{R}[!] Session Expired. Deleting old session and restarting...{W}")
        if os.path.exists(f"{session_name}.session"):
            os.remove(f"{session_name}.session")
        app = Client(session_name, api_id=API_ID, api_hash=API_HASH)
        await app.connect()

    try:
        user_me = await app.get_me()
    except Exception:
        user_me = None

    if not user_me:
        print(f"{Y}[!] New Login Required...{W}")
        phone = input(f"{G}┌─[Enter Phone Number (+91xxxx)]\n└──╼ {W}").strip()
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

    banner()
    name = user_me.first_name if user_me else "User"
    print(f"{G}✅ ACCESS GRANTED: {name}{W}\n")
    
    target = input(f"{G}┌─[Target Username or ID]\n└──╼ {W}").strip()
    count = int(input(f"{G}Report Intensity (1-1000): {W}"))

    print(f"\n{R}[🔥] ATTACK STARTED BY RONAK HACKER...{W}\n")
    try:
        peer = await app.resolve_peer(target)
        for i in range(1, count + 1):
            try:
                await app.invoke(raw.functions.account.ReportPeer(
                    peer=peer, 
                    reason=types.InputReportReasonSpam(), 
                    message="Community Guideline Violation Report."))
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
        print(f"{R}❌ Error: {str(e)}{W}")
    finally:
        await app.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
