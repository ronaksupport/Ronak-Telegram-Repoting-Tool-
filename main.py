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

REPORT_MESSAGES = [
    "Spamming prohibited content.",
    "Violence and community guideline breach.",
    "Harassment and abusive behavior.",
    "Illegal activities and scamming users."
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
    print(f"{G}        [ RONAK HACKER - LIVE REPORT COUNTER ]{W}\n")

async def main():
    banner()
    session_name = "ronak_final_v4"
    app = Client(session_name, api_id=API_ID, api_hash=API_HASH)
    
    await app.connect()
    
    # Session Validation
    try:
        user_me = await app.get_me()
    except Exception:
        user_me = None

    if not user_me:
        print(f"{Y}[!] Login Required...{W}")
        phone = input(f"{G}┌─[Enter Phone (+ Country Code)]\n└──╼ {W}").strip()
        sent_code = await app.send_code(phone)
        otp = input(f"{G}┌─[Enter OTP]\n└──╼ {W}").strip()
        try:
            user_me = await app.sign_in(phone, sent_code.phone_code_hash, otp)
        except errors.SessionPasswordNeeded:
            pwd = input(f"{G}┌─[Enter 2FA Password]\n└──╼ {W}").strip()
            user_me = await app.check_password(pwd)

    banner()
    print(f"{G}✅ ACCESS GRANTED: {user_me.first_name}{W}\n")
    
    target = input(f"{G}┌─[Target Username/ID]\n└──╼ {W}").strip()
    try:
        limit = int(input(f"{G}┌─[How many reports (Digit)]\n└──╼ {W}Count: "))
    except:
        limit = 10

    print(f"\n{R}[🔥] ATTACK IN PROGRESS...{W}\n")
    
    try:
        peer = await app.resolve_peer(target)
        for i in range(1, limit + 1):
            try:
                msg = random.choice(REPORT_MESSAGES)
                await app.invoke(raw.functions.account.ReportPeer(
                    peer=peer, 
                    reason=types.InputReportReasonSpam(), 
                    message=msg))
                
                # Yeh hai aapka manga hua Live Counter
                print(f"{G}{i} report sent ✅{W}")
                
                await asyncio.sleep(0.3) # Fast speed
            except errors.FloodWait as e:
                print(f"{Y}Waiting {e.value}s due to flood...{W}")
                await asyncio.sleep(e.value)
            except Exception:
                continue

        # Final Success Message
        print(f"\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{R}🚀 Ronak Report Tool SUCCESSFUL 🚀")
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
        input(f"\n{C}Press Enter to Exit...{W}")
        
    except Exception as e:
        print(f"{R}❌ Error: {str(e)}{W}")
    finally:
        await app.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
