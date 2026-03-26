### **Two Systems (Dell + Asus)**

- **Networking** : Requires Bridged (Exposes VMs to your home Wi-Fi)
- **Complexity** : High (Walking between laptops, physical wires)
- **Speed** : Limited by your Wi-Fi/Ethernet speed
- **Safety** : High risk if you run malware (Bridged)

### **One System (Single Host)**

- **Networking**: Can use Internal Network (Total isolation)
- **Complexity** : Low (Switching windows on one screen)
- **Speed** : Limited only by your computer’s RAM/CPU
- **Safety** : Zero risk to your home network if using Internal mode

<table>
    <tr>
        <th>Network Mode</th>
        <th>Use Case</th>
        <th>Why?</th>
    </tr>
    <tr>
        <td>Bridged Network</td>
        <td>Multi-Device Lab</td>
        <td>Best for your current Dell + Asus setup</td>
    </tr>
    <tr>
        <td>NAT Network</td>
        <td>Single-Device Lab</td>
        <td>If you had both Kali and Metasploitable on only the Dell, this keeps them in a private "bubble" hidden from your router.</td>
    </tr>
    <tr>
        <td>Host-Only Adaptor</td>
        <td>High Security</td>
        <td>Use this if you are analyzing "Live Malware." It prevents the virus from escaping the VMs and reaching the internet or your physical home network.</td>
    </tr>
</table>


**Basic penetration testing** (scanning, exploiting services) : Bridged (Both VMs appear on same network, easy communication)

**Web app testing** (SQLi, XSS via browser)	: Bridged (Need to access web interface from Kali browser)

**Malware/backdoor testing** : Host-Only (Isolated, malware can't escape to your real network)

**Complete APT simulation** : Host-Only (Safe for persistent backdoors and malware)

**Pentesting** : Hybrid (NAT + Bridged) : Needs internet for tools; needs Bridged to see the second laptop.
Malware Analysis : Host-Only / Isolated : Must prevent the virus from spreading to your home network.

---

**Private Network (Home)** : Bridged : Safe. Your router is your own.

**Public Network (University)** : NAT Network : Switch to this! Public networks often block "Bridged" devices for security, or worse, other students might see your vulnerable Metasploitable VM.

**No Wi-Fi** : Host-Only : If you have no internet, Bridged won't work. Use Host-Only to let the two laptops talk via a LAN cable.

---

**Setup & Update** : UP NAT (eth0), DOWN Bridged (eth1) : "To download nmap, metasploit, or updates safely."

**Active Pentesting** : UP NAT (eth0), UP Bridged (eth1) : NAT for looking up exploits; Bridged to hit the Asus laptop.

**Safe Lab Mode** : DOWN NAT (eth0), UP Bridged (eth1) : Keeps your hacking activity isolated from the internet.

**Malware Test** : DOWN NAT (eth0), DOWN Bridged (eth1) : "STOP! Switch to ""Host-Only"" in VirtualBox before proceeding."

---

**NAT (Standard)** : Browsing the web safely (VMs are isolated from each other).

**NAT Network** : The perfect hacking lab setup.

**Host-only** : Maximum security (if you don't want any traffic leaving your PC), No Internet Access

---

1. **Downloading (NAT Network)** — Good
   
    **Why:** Both VMs can reach the internet to grab tools or samples, and they can talk to each other to move those files around.

2. **Malware Analysis (Host-only)** — Perfect
   
    **Why:** This is the safest way to "detonate" malware. If the malware tries to "phone home" or spread, it is physically trapped inside your computer's RAM and cannot touch your router or the internet.

3. **Pentesting Same System (NAT Network)** — Good
   
    **Why:** It keeps your lab isolated from your family/roommates on the same Wi-Fi while letting your Kali machine still look up tutorials or documentation online.

4. **Pentesting Different Systems (Bridged)** — High Risk
   
    **Why:** Putting Metasploitable 2 in Bridged mode is like putting a "HACK ME" sign on your front lawn. It becomes visible to every device on your Wi-Fi. If your router has a weak firewall, it might even be visible to the public internet.

    **The Fix:** If you must use two different physical computers, connect them with a physical Ethernet cable or use a VPN (like OpenVPN) to create a private tunnel between them. Avoid your main home Wi-Fi for this.

    **Alternate Fix:** Mobile Hotspot Method, where this creates a separate, private wireless network that acts as a "virtual bridge" between your two laptops. On both laptops, set your VM network adapter to Bridged Adapter and select the Wireless/Wi-Fi interface that is connected to the hotspot.

---

- A Static IP address is a permanent, unchanging numerical identifier manually assigned to a device on a network. Unlike standard Dynamic ip addresses (DHCP) that change periodically, a static IP remains the same every time the device connects
- In a penetration testing lab, it ensures your Victim (Target) remains at a known, reachable address, preventing your automation scripts and exploit payloads from failing due to an IP change.
- It allows for communication in "Air-Gapped" or "Host-Only" environments where a DHCP Server is absent or intentionally disabled for security.

**Your Workflow Breakdown**

- Preparation (NAT Network):
    - Switch both VMs to NAT Network on their respective hosts.
    - Connect your laptops to your home Wi-Fi.
    - Download your tools on Kali (e.g., sudo apt update, searchsploit, etc.).
- The Attack Lab (Bridged + Hotspot):
    - Turn off your home Wi-Fi on both laptops.
    - Turn on the Mobile Hotspot on your SIM-less phone (it doesn't need data; it just needs to broadcast a signal).
    - Connect both the Dell and Asus to that phone's Wi-Fi.
    - Change both VM settings in VirtualBox to Bridged Adapter (select the Wi-Fi card).
- Execution:
    - Your VMs will now be "bridged" onto the phone's network.
    - Since the phone has no SIM/Internet, your lab is 100% isolated.

**One Small Detail to Watch**

- Since your phone has no internet and no SIM, it might not have a DHCP server running to give your VMs IP addresses automatically.
- The Fix: You will likely need to set Static IPs inside your VMs so they can talk to each other:

    - On Kali (Dell): sudo ifconfig eth0 192.168.43.10 netmask 255.255.255.0
    - On Metasploitable (Asus): sudo ifconfig eth0 192.168.43.20 netmask 255.255.255.0
    (Note: Android hotspots usually use the 192.168.43.x range).


---

1. **On Metasploitable (The Victim)**
   
    Since Metasploitable 2 is purely command-line, you’ll type this directly into the terminal:

    - Login with msfadmin / msfadmin.
    - Type:
    `sudo ifconfig eth0 192.168.43.20 netmask 255.255.255.0`
    - Verify it by typing:
    `ifconfig`
    (Look for the inet addr: 192.168.43.20 line).

2. **On Kali Linux (The Attacker)**
    You can do this via the terminal for speed:

    - Open a terminal.
    - Type:
    `sudo ifconfig eth0 192.168.43.10 netmask 255.255.255.0`
    (Note: If you are using Wi-Fi, the interface name might be wlan0 instead of eth0).
    - Verify it worked:
    `ip a`

---

### **How to Take a Snapshot (Before the Attack)**

- Shut Down the VM: While you can take snapshots while it's running, it is much cleaner and faster to do it while the VM is Powered Off.
- Select the VM: Click on your Metasploitable (victim) VM in the VirtualBox list.
- Go to Snapshots: Click the small Menu icon (three lines/dots) next to the VM name and select Snapshots.
- Click Take: Hit the Take button (camera icon).
- Name It: Give it a clear name like "Clean Install - Before Malware" and click OK.


**How to "Undo" Damage (Restoring)**
If the malware breaks the system:

- Shut Down the broken VM.
- Go back to the Snapshots tab.
- Right-click your "Clean Install" snapshot and select Restore.
- Uncheck the box that says "Create a snapshot of the current system state" (you don't want to save the broken version!).
- Click Restore. Now, when you start the VM, it will be exactly as it was when you first set it up.