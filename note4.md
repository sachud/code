### To gain hands-on experience

you should transform your Asus into a "Target" through Virtualization and your Dell into the "Control Center."

1. The "Sandbox" Setup (Safe Learning)
- Do not install hacking tools directly on your daily Windows/Mac OS.
- On the Dell: Install VirtualBox or VMware Player. Inside it, run a Kali Linux VM. This is your "Attacker" machine.
- On the Asus: Install VirtualBox and download Metasploitable 2 (a Linux VM designed to be hackable) or OWASP Juice Shop or Windows 10 VM
- The Experience: Try to "attack" the Asus VM from your Dell VM. This teaches you Network Scanning (Nmap) and Exploitation (Metasploit) without touching your family's files.

    Test Your Antivirus (The Purple Team Project)
    Step A: Write your "Small Attack Tool" (the one we discussed, like a harmless ransomware simulator) on the Dell.
    Step B: Move that tool to a specific "Test Folder" on the Asus.
    Step C: Install your Antivirus on the Asus and run the attack tool.
    The Experience: If the Asus alerts you, your code is working. If the tool "encrypts" the folder, you need to go back to the Dell and fix your Antivirus code.

1. Monitor the Family Network (Defense Experience)
- Use your Dell to see what’s happening on your home Wi-Fi.
- Tool: Install Wireshark on your Dell.
- The Task: Watch the traffic (packets) while someone uses the Asus. Can you see which websites they are visiting? (If they are HTTPS, you’ll only see encrypted data; if HTTP, you might see more).
- The Experience: This teaches you Packet Analysis, which is a core skill for SOC Analysts.

1. Remote Administration & Logs
- The Task: Try to "SSH" from your Dell into the Asus (you'll need to enable WSL or a Linux VM on the Asus).
- The Experience: Once connected, try to read the Asus system logs (Event Viewer on Windows or /var/log on Linux).
- Why? Real cyber jobs involve looking at logs on remote servers to find where a hacker entered.

1. Build a "Honey-Folder"
- The Task: Create a folder on the Asus named "Bank Passwords" (put fake files inside).
- The Script: Write a small Python script on the Asus that sends an email to your Dell whenever that folder is opened.
- The Experience: This is a basic EDR (Endpoint Detection and Response) concept.

Important Warning: Since the Asus is used by your family, never run tools that crash the system or change BIOS settings. Always do the "dangerous" stuff inside a Virtual Machine (VM).

Best Setup for Your Asus (Target)
Allocate Resources: Give the VM at least 4GB of RAM and 2 CPU cores so it doesn't lag.
Network Mode: Use "Bridged Adapter" in your VirtualBox or VMware settings. This gives the Asus VM its own IP address, allowing your Dell to "talk" to it over your home Wi-Fi.
Tools to Install: Once Windows is in the VM, install System Informer or Process Monitor. These will let you "see" exactly what your Python scripts are doing to the system in real-time.


Wireshark: Install this on your Dell and learn how to capture and inspect packets. Try to identify what happens "under the hood" when you visit a website or send an encrypted file.

Nmap: Use your Dell to scan your Asus (ensure your family isn't doing anything critical!) to see which ports are open and what services are running.