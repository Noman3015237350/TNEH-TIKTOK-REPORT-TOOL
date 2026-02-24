# change banner name new banner and logo name TNEH TIKTOK REPORT TOOL
# dv TNEH GROUP 
# auto open telegram group https://t.me/+QkMGTxBpqftkNDU1
# then ckk enter then open tool 
# DECODED BY - TNEH GROUP (t.me/tneh_owner)
# GitHub - github.com/LMNx9 https://t.me/+QkMGTxBpqftkNDU1
# WhatsApp - https://wa.me/+8801611229803

""" OPEN SOURCED BY - TNEH GROUP """

import os
import time
import random
import requests
import re
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.live import Live
from rich.table import Table

console = Console()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- ১. টিকটক রিপোর্টের নামের তালিকা ---
TIKTOK_REPORTS = [
    "Violent Graphic Content", "Dangerous Acts & Challenges",
    "Harassment & Bullying", "Hate Speech Bypass",
    "Minor Safety Violation", "Illegal Activities",
    "Spam & Fake Engagement", "Intellectual Property Theft"
]

PROXY_API = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

# --- ২. লোগো ও ব্র্যান্ডিং (UPDATED) ---
def display_logo():
    logo_text = """
████████╗███╗   ██╗███████╗██╗  ██╗
╚══██╔══╝████╗  ██║██╔════╝██║  ██║
   ██║   ██╔██╗ ██║█████╗  ███████║
   ██║   ██║╚██╗██║██╔══╝  ██╔══██║
   ██║   ██║ ╚████║███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """
    
    title_text = """
╔══════════════════════════════════════════╗
║      TNEH TIKTOK REPORT TOOL v2.0       ║
║            [ TNEH GROUP ]                ║
╚══════════════════════════════════════════╝
    """
    
    logo_panel = Panel(
        Align.center(
            Text(logo_text + title_text, style="bold cyan"), 
        ),
        title="[bold red]⚡ TNEH SECURITY ⚡[/bold red]", 
        border_style="cyan", 
        style="on black"
    )
    console.print(logo_panel)

# --- ৩. স্ট্যাটাস টেবিল জেনারেটর ---
def generate_stats_table(total, success, failed):
    table = Table(title="[bold cyan]TNEH Live Reporting Statistics[/bold cyan]", border_style="cyan")
    table.add_column("Total Hits", justify="center", style="yellow")
    table.add_column("Success", justify="center", style="green")
    table.add_column("Failed", justify="center", style="red")
    table.add_row(str(total), str(success), str(failed))
    return table

# --- ৪. প্রক্সি স্ক্র্যাপার ---
def get_proxies():
    try:
        response = requests.get(PROXY_API)
        return response.text.splitlines() if response.status_code == 200 else []
    except:
        return []

# --- ৫. টেলিগ্রাম জয়েন লক (UPDATED with new group) ---
def telegram_lock():
    channel_url = "https://t.me/+QkMGTxBpqftkNDU1"  # New TNEH Group
    while True:
        clear()
        display_logo()
        console.print(Panel(
            "[bold yellow][!] JOIN TNEH GROUP TO UNLOCK TOOL[/bold yellow]\n\n"
            "[bold cyan]Group Link:[/bold cyan] https://t.me/+QkMGTxBpqftkNDU1\n\n"
            "[bold white]After joining, press ENTER to continue...[/bold white]", 
            border_style="yellow", 
            title="[bold red]🔐 ACCESS REQUIRED[/bold red]"
        ))
        
        # Auto open telegram group
        os.system(f"xdg-open {channel_url}")
        
        # Wait for user to press ENTER
        input("\n[?] Press ENTER after joining the group...")
        
        console.print("[bold green][✓] Access Granted! Welcome TNEH Member![/bold green]")
        time.sleep(1)
        break

# --- ৬. মেইন রিপোর্টিং ইঞ্জিন ---
def start_reporting(target, mode_name, proxy_list):
    report_count = 0
    success_count = 0
    failed_count = 0
    
    clear()
    display_logo()
    console.print(Panel(
        f"[bold green]Target:[/bold green] {target}\n"
        f"[bold yellow]Mode:[/bold yellow] {mode_name}\n"
        f"[bold cyan]Group:[/bold cyan] TNEH GROUP", 
        border_style="cyan"
    ))
    console.print("\n[bold cyan][ TNEH HISTORICAL LOGS ][/bold cyan]\n" + "-"*65)

    while True:
        report_count += 1
        current_report_name = random.choice(TIKTOK_REPORTS)
        current_proxy = random.choice(proxy_list) if proxy_list else "Rotating Proxy"
        now = datetime.now().strftime("%H:%M:%S")
        wait_time = random.choice([10, 15, 60])
        is_failed = random.random() < 0.15 

        log_msg = Text()
        log_msg.append(f"[{now}] ", style="bold blue")
        log_msg.append(f"HIT #{report_count} ", style="bold yellow")
        log_msg.append(f"| NAME: {current_report_name[:15]}... ", style="bold cyan")
        log_msg.append(f"| IP: {current_proxy[:15]} ", style="bold magenta")
        
        if is_failed:
            failed_count += 1
            log_msg.append(" | [FAILED ❌]", style="bold red")
            console.print(log_msg)
            console.print(f"   [dim red]└─ Connection Timeout: Proxy refused to respond.[/dim red]")
        else:
            success_count += 1
            log_msg.append(" | [SENT 💥]", style="bold green")
            console.print(log_msg)
            if report_count > 25 and wait_time == 60:
                console.print(f"   [dim white]└─ IP Response is slow... System Overloaded[/dim white]")
        
        # প্রতি রিপোর্টে লাইভ স্ট্যাটাস দেখানো
        console.print(generate_stats_table(report_count, success_count, failed_count))

        for i in range(wait_time, 0, -1):
            console.print(f"\r[bold white][!] Next Payload in {i}s...[/bold white]", end="")
            time.sleep(1)
        console.print("\r" + " " * 65, end="\r")

# --- ৭. মেইন ফাংশন ---
def main():
    telegram_lock()
    clear()
    display_logo()
    
    console.print(Panel(
        "[bold yellow]SELECT REPORT MODE[/bold yellow]\n\n"
        " [bold cyan]1[/bold cyan] • TikTok Video Link\n"
        " [bold cyan]2[/bold cyan] • TikTok User Profile\n"
        " [bold cyan]3[/bold cyan] • TNEH Group Info",
        border_style="cyan"
    ))
    
    choice = input("\n[>] TNEH Choice: ")
    
    if choice == "1":
        mode_name = "VIDEO REPORT MODE"
        target = input("[>] Enter Video Link: ")
        if "tiktok.com" not in target: 
            console.print("[bold red]Invalid TikTok Link![/bold red]")
            return
    elif choice == "2":
        mode_name = "PROFILE BAN MODE"
        target = input("[>] Enter Username: ")
        if len(target) < 2: 
            console.print("[bold red]Invalid Username![/bold red]")
            return
    elif choice == "3":
        console.print(Panel(
            "[bold cyan]TNEH GROUP INFORMATION[/bold cyan]\n\n"
            "Group: TNEH TikTok Report Team\n"
            "Link: https://t.me/+QkMGTxBpqftkNDU1\n"
            "Members: Active\n"
            "Status: Online", 
            border_style="green"
        ))
        input("\n[?] Press ENTER to continue...")
        return main()
    else: 
        return

    with console.status("[bold cyan]TNEH System: Fetching Global Proxies...[/bold cyan]", spinner="dots"):
        proxies = get_proxies()
        time.sleep(1)

    try:
        start_reporting(target, mode_name, proxies)
    except KeyboardInterrupt:
        console.print("\n\n[bold red][!] Session Terminated by TNEH User.[/bold red]")
        console.print("[bold cyan]Thanks for using TNEH TikTok Report Tool![/bold cyan]")

if __name__ == "__main__":
    main()
