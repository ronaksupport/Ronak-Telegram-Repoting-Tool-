import asyncio
import os
import sys
import time
import re
from pyrogram import Client, filters, errors
from pyrogram.raw import functions, types

# --- CONFIGURATION ---
API_ID = 32567928
API_HASH = "1ccc36ef5a82df3bba346bf9af66c143"

# --- COLORS ---
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
B = '\033[1;34m' # Blue
W = '\033[0m'    # White

def clear():
    os.system('clear')

def draw_header(page_title):
    clear()
    print(f"{R}██████╗  ██████╗ ███╗   ██╗ █████╗ ██╗  ██╗")
    print(f"{R}██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██║ ██╔╝")
    print(f"{W}██████╔╝██║   ██║██╔██╗ ██║███████║█████╔╝ ")
    print(f"{W}██╔══██╗██║   ██║██║╚██╗██║██╔══██║██╔═██╗ ")
    print(f"{R}██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██╗")
    print(f"{R}╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{G}       [ PROJECT: RONAK REPORT TOOL ]")
    print(f"{Y}       [ CURRENT PAGE: {page_title.upper()} ]")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n")

async def ronak_system():
    # --- PAGE 1: ACCOUNT ACCESS ---
    draw_header("Account Login")
    print(f"{B}[ℹ] System requires a valid String Session to bypass filters.{W}")
    session = input(f"{G}┌─[Ronak@Login]\n└──╼ {W}Paste Session: ").strip()
    
    if not session:
        print(f"\n{R}❌ Access Denied: Session cannot be empty!{W}")
        return

    # --- PAGE 2: TARGET & ATTACK VECTORS ---
    draw_header("Target Config")
    print(f"{B}[ℹ] Enter Channel ID, Group ID, or Username (Unified Mode).{W}")
    target = input(f"{G}┌─[Ronak@Target]\n└──╼ {W}Target ID/User: ").strip()
    
    print(f"\n{Y}[ SELECT ATTACK VECTOR ]{W}")
    print(f"{C}1. Spam Injection      2. Violence/Illegal")
    print(f"3. Child Abuse Hits    4. Pornography/Other{W}")
    choice = input(f"\n{G}┌─[Ronak@Vector]\n└──╼ {W}Select (1-4): ")

    try:
        limit = int(input(f"{G}┌─[Ronak@Intensity]\n└──╼ {W}Report Count (e.g. 500): "))
    except:
        limit = 100

    # --- PAGE 3: ATTACK EXECUTION ---
    draw_header("Reporting Engine")
    print(f"{R}[!] Initializing Deception Protocols...{W}")
    time.sleep(1)

    async with Client("ronak_engine", api_id=API_ID, api_hash=API_HASH, session_string=session, in_memory=True) as app:
        try:
            # Resolve Peer (Unified for all types)
            print(f"{B}[*] Resolving Target Security Layers...{W}")
            peer = await app.resolve_peer(target)
            
            reasons = {
                "1": types.InputReportReasonSpam(),
                "2": types.InputReportReasonViolence(),
                "3": types.InputReportReasonChildAbuse(),
                "4": types.InputReportReasonPornography()
            }
            vec = reasons.get(choice, reasons["1"])

            print(f"{R}[🔥] ATTACK COMMENCED BY RONAK REPORT TOOL{W}\n")
            
            for i in range(1, limit + 1):
                try:
                    await app.invoke(
                        functions.account.ReportPeer(
                            peer=peer,
                            reason=vec,
                            message="Ronak Report System: Critical Violation Detected. Termination Required."
                        )
                    )
                    sys.stdout.write(f"\r{G}[REPORT-{i}] Ronak Tool successfully bypassed filters for {target}{W}")
                    sys.stdout.flush()
                    
                    # Anti-Spam Wait
                    await asyncio.sleep(0.2)
                    
                except errors.FloodWait as e:
                    print(f"\n{Y}[!] Telegram Flood Protection Active. Waiting {e.value}s...{W}")
                    await asyncio.sleep(e.value)
                except Exception as e:
                    print(f"\n{R}[!] Hit Failed: {str(e)}{W}")

            print(f"\n\n{G}✅ [COMPLETED] Target {target} marked for termination.")
            print(f"{Y}Status: All {limit} Reports Sent By Ronak Report Tool.{W}")
            input(f"\n{C}Press Enter to return to main system...{W}")

        except errors.AuthKeyInvalid:
            print(f"{R}❌ Error: String Session Unauthorized!{W}")
        except Exception as e:
            print(f"{R}❌ System Fatal Error: {str(e)}{W}")

if __name__ == "__main__":
    try:
        asyncio.run(ronak_system())
    except KeyboardInterrupt:
        print(f"\n{R}[!] Manual Shutdown by Ronak System.{W}")
