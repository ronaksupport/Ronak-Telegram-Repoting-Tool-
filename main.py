import asyncio
import os
import sys
from pyrogram import Client, errors, raw, types

# --- API CONFIG ---
# Aap apni API_ID aur API_HASH bhi use kar sakte hain
API_ID = 32567928
API_HASH = "1ccc36ef5a82df3bba346bf9af66c143"

# --- COLORS ---
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
W = '\033[0m'    

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"{R}██████╗  ██████╗ ███╗   ██╗ █████╗ ██╗  ██╗")
    print(f"{R}██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██║ ██╔╝")
    print(f"{W}██████╔╝██║   ██║██╔██╗ ██║███████║█████╔╝ ")
    print(f"{W}██╔══██╗██║   ██║██║╚██╗██║██╔══██║██╔═██╗ ")
    print(f"{R}██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██╗")
    print(f"{G}       [ RONAK HACKER - OTP LOGIN SYSTEM ]{W}\n")

async def main():
    banner()
    # Session file locally save hogi
    app = Client("ronak_session", api_id=API_ID, api_hash=API_HASH)
    
    await app.connect()
    
    try:
        me = await app.get_me()
    except:
        me = None

    if not me:
        print(f"{Y}[!] Login Required...{W}")
        phone = input(f"{G}Enter Phone Number (with +91): {W}")
        try:
            sent_code = await app.send_code(phone)
            otp = input(f"{G}Enter OTP sent on Telegram: {W}")
            try:
                await app.sign_in(phone, sent_code.phone_code_hash, otp)
            except errors.SessionPasswordNeeded:
                pwd = input(f"{G}2FA Password Required: {W}")
                await app.check_password(pwd)
        except Exception as e:
            print(f"{R}Login Error: {e}{W}")
            return

    banner()
    print(f"{G}Login Successful as: {app.me.first_name}{W}\n")
    
    target = input(f"{C}Target Username/ID: {W}")
    print(f"\n{Y}1. Spam  2. Violence  3. Child Abuse  4. Copyright  5. Other{W}")
    choice = input(f"{G}Select Reason: {W}")
    
    reasons = {
        "1": types.InputReportReasonSpam(),
        "2": types.InputReportReasonViolence(),
        "3": types.InputReportReasonChildAbuse(),
        "4": types.InputReportReasonCopyright(),
        "5": types.InputReportReasonOther()
    }
    
    reason = reasons.get(choice, types.InputReportReasonSpam())
    msg_text = "Violation of Telegram terms. Please take action."

    try:
        peer = await app.resolve_peer(target)
        count = int(input(f"{G}Report Count: {W}"))
        
        print(f"\n{R}[!] Attack Started on {target}...{W}\n")
        
        for i in range(1, count + 1):
            try:
                await app.invoke(
                    raw.functions.account.ReportPeer(
                        peer=peer,
                        reason=reason,
                        message=msg_text
                    )
                )
                print(f"{G}[SUCCESS] Report {i} Sent!{W}")
                await asyncio.sleep(0.5) # Avoid flood
            except errors.FloodWait as e:
                print(f"{Y}FloodWait: Sleeping {e.value}s{W}")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"{R}Error: {e}{W}")
                
    except Exception as e:
        print(f"{R}Could not find target: {e}{W}")

if __name__ == "__main__":
    asyncio.run(main())
    
