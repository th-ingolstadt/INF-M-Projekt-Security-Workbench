#!/bin/bash
# Script to install secWorkstation Service Providing Server
# !!!! Keine Überprüfung ob schon konfiguriert durch mehrfaches ausführen geht die configuration kaputt !!!!

##Help Functions
#
#check if dpkg is locked
checkAPT() {
	while fuser /var/lib/dpkg/lock >/dev/null 2>&1 ; do
    		echo -en "\r Waiting for other software managers to finish..."
    		sleep 0.5
	done 
}
##
### Main 
#
## Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
##

echo "Start Installation of Gateway PI"
## Update System
apt-get update && apt-get full-upgrade -y;

## Install, Config, Build of Docker
# Install Docker
apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
	gnupg2 \
	software-properties-common
# Add GPG Key 
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
# Add Source
echo "deb [arch=armhf] https://download.docker.com/linux/debian stretch stable" | sudo tee /etc/apt/sources.list.d/docker.list
# Update and install Docker-Comunitey Edition
apt-get update
apt-get install -y docker-ce
# Enable Docker on System Start
systemctl enable docker
service docker start 
# groupadd docker;
# Add user pi to docker group
usermod -aG docker pi;
## Build Docker container
# 
## 
echo "Installation of docker finished"

##########################
# Create Docker container#
##########################
# Linux Keylogger Container
export LINUX_KEYLOGGER_WEB_RES_PATH=$project_path/Keylogger/wifi_snatcher_DigiSpark/linux/html
../Keylogger/wifi_snatcher_DigiSpark/linux/keyloggerLinuxDockerControl.sh start
# Windows Keylogger container
export WINDOS_KEYLOGGER_WEB_RES_PATH=$project_path/Keylogger/wifi_snatcher_DigiSpark/windows/html
../Keylogger/wifi_snatcher_DigiSpark/windows/keyloggerDockerControl.sh start




## Network Configuration
#
#
##
echo "Start Configuration of Network"

## Check WLAN Modul
checkAPT;
apt-get install iw -y;
## Check WLAN Module
iw list | grep AP ## Check if not NULL

## Configure WLAN-Interfaces
# IP-Range:
##
echo "# WLAN-Interface 0
#allow-hotplug wlan0
#iface wlan0 inet static
#address 192.168.1.1
#netmask 255.255.255.0

# WLAN-Interface 1
allow-hotplug wlan1
iface wlan1 inet static
address 172.26.63.253
netmask 255.255.240.0
up service isc-dhcp-server restart

# WLAN-Interface 2
allow-hotplug wlan2
iface wlan2 inet static
address 172.26.79.253
netmask 255.255.240.0
up service isc-dhcp-server restart

# WLAN-Interface 3
allow-hotplug wlan3
iface wlan3 inet static
address 172.26.95.253
netmask 255.255.240.0
up service isc-dhcp-server restart

# WLAN-Interface 4
allow-hotplug wlan4
iface wlan4 inet static
address 172.26.111.253
netmask 255.255.240.0
up service isc-dhcp-server restart

# WLAN-Interface 5
allow-hotplug wlan5
iface wlan5 inet static
address 172.26.111.253
netmask 255.255.240.0
up service isc-dhcp-server restart
up ip addr add 172.26.112.1 dev wlan5
" > /etc/network/interfaces.d/wlan

## Configure eth Interfaces
# IP-Range: 172.26.32.0/XX1
# IP:172.26.32.5 -> news.local
##
echo "# ETH1-Interface
allow-hotplug eth1
iface eth1 inet static
address 172.26.47.253
netmask 255.255.240.0
up ip addr add 172.26.32.5 dev eth1
up ip addr add 172.26.32.6 dev eth1
up ip addr add 172.26.32.7 dev eth1
up ip addr add 172.26.32.8 dev eth1
" > /etc/network/interfaces.d/eth1

## Configuration of Firewall and Routing
# TODO some infos about
##
checkAPT;
## Install tool for iptable persistent
apt-get install iptables-persistent -y; ## TODO Hier muss noch die User eingabe auforderung unterdrückt werden TODO
# Clean Firewall Rules
iptables -F
iptables -X
iptables -t nat -F

# Loopback zulassen
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# NAT und Masquerading aktivieren
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth0 -o wlan1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth1 -j ACCEPT

# IP-Forwarding aktivieren
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1;

#Save IPTables
iptables-save > /etc/iptables/rules.v4
echo "# Generated by iptables-save v1.6.0
*filter
:INPUT ACCEPT [975:114165]
:FORWARD ACCEPT [4:160]
:OUTPUT ACCEPT [532:81632]
-A FORWARD -i eth0 -o wlan1 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i wlan1 -o eth0 -j ACCEPT
-A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i eth1 -o eth0 -j ACCEPT
-A OUTPUT -i wlan1-o eth0 -s 10.0.0.0/8 -j DROP
-A OUTPUT -i wlan1 -o eth0 -s 172.16.0.0/12 -j DROP
-A OUTPUT -i wlan1-o eth0 -s 192.168.0.0/16 -j DROP
-A OUTPUT -i wlan2-o eth0 -s 10.0.0.0/8 -j DROP
-A OUTPUT -i wlan2 -o eth0 -s 172.16.0.0/12 -j DROP
-A OUTPUT -i wlan2-o eth0 -s 192.168.0.0/16 -j DROP
-A OUTPUT -i wlan3-o eth0 -s 10.0.0.0/8 -j DROP
-A OUTPUT -i wlan3 -o eth0 -s 172.16.0.0/12 -j DROP
-A OUTPUT -i wlan3-o eth0 -s 192.168.0.0/16 -j DROP
-A OUTPUT -i wlan4-o eth0 -s 10.0.0.0/8 -j DROP
-A OUTPUT -i wlan4 -o eth0 -s 172.16.0.0/12 -j DROP
-A OUTPUT -i wlan4-o eth0 -s 192.168.0.0/16 -j DROP
-A OUTPUT -i eth1-o eth0 -s 10.0.0.0/8 -j DROP
-A OUTPUT -i eth1 -o eth0 -s 172.16.0.0/12 -j DROP
-A OUTPUT -i eth1-o eth0 -s 192.168.0.0/16 -j DROP
-A OUTPUT -i wlan5 DROP
-A OUTPUT -i wlan5 172.26.127.253 -j ACCEPT
COMMIT
# Completed on Sun Nov  5 07:45:11 2017
# Generated by iptables-save v1.6.0 on Sun Nov  5 07:45:11 2017
*nat
:PREROUTING ACCEPT [175:13840]
:INPUT ACCEPT [128:10448]
:OUTPUT ACCEPT [289:17433]
:POSTROUTING ACCEPT [1:48]
-A POSTROUTING -o eth0 -j MASQUERADE
COMMIT
# Completed " > /etc/iptables/rules.v4


#sudo sh -c "iptables-save > /etc/iptables/rules.v6"
sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf

## 
# Don't request IP on interface wlanX eth1
# 
echo "denyinterfaces wlan0 wlan1 wlan2 wlan3 wlan4 wlan5 eth1"  >>/etc/dhcpcd.conf

## Install DHCP- DNS-Server
# isc-dhcp
# Bind9
##
checkAPT;

#Install isc-dhcp
apt-get install isc-dhcp-server -y;
#SET Interfaces for dhcp Server
sed -i 's/INTERFACESv4=\"\"/INTERFACESv4=\"eth1 wlan1 wlan2 wlan3 wlan4 wlan5\"/g' /etc/default/isc-dhcp-server
#Configurare
echo "# dhcpd.conf
#
# Sample configuration file for ISC dhcpd
#

authoritative;
option broadcast-address 172.26.240.0;
default-lease-time 600;
max-lease-time 7200;
subnet 172.26.32.0 netmask 255.255.240.0 {
   range 172.26.32.10 172.26.47.250;
   option routers 172.26.47.253;
   option domain-name-servers 172.26.47.253;
   interface eth1;
}
subnet 172.26.48.0 netmask 255.255.240.0 {
   range 172.26.48.10 172.26.63.250;
   option routers 172.26.63.253;
   option domain-name-servers 172.26.63.253;
   interface wlan1;
}
subnet 172.26.64.0 netmask 255.255.240.0 {
   range 172.26.64.10 172.26.79.250;
   option routers 172.26.79.253;
   option domain-name-servers 172.26.79.253;
   interface wlan2;
}
subnet 172.26.80.0 netmask 255.255.240.0 {
   range 172.26.80.10 172.26.95.250;
   option routers 172.26.95.253;
   option domain-name-servers 172.26.95.253;
   interface wlan3;
}
subnet 172.26.96.0 netmask 255.255.240.0 {
   range 172.26.96.10 172.26.111.250;
   option routers 172.26.111.253;
   option domain-name-servers 172.26.111.253;
   interface wlan4;
}
subnet 172.26.112.0 netmask 255.255.240.0 {
   range 172.26.112.10 172.26.127.250;
   option routers 172.26.127.253;
   option domain-name-servers 172.26.127.253;
   interface wlan5;
}
" > /etc/dhcp/dhcpd.conf

#Install DNS Bind9
apt-get install bind9 bind9utils dnsutils -y;
#Conf Bind9 use CCC config
cp /etc/bind/named.conf.options /etc/bind/named.conf.options.bak
echo "options {
        directory \"/var/cache/bind\";

        // If there is a firewall between you and nameservers you want
        // to talk to, you may need to fix the firewall to allow multiple
        // ports to talk.  See http://www.kb.cert.org/vuls/id/800113

        // If your ISP provided one or more IP addresses for stable
        // nameservers, you probably want to use them as forwarders.
        // Uncomment the following block, and insert the addresses replacing
        // the all-0's placeholder.

        forwarders {
        // see: http://www.ccc.de/de/censorship/dns-howto
        85.214.20.141;    // FoeBud
        204.152.184.76;   // f.6to4-servers.net, ISC, USA
        194.150.168.168;  // dns.as250.net; Berlin/Frankfurt
        213.73.91.35;     // dnscache.berlin.ccc.de
        // OpenDNS
        208.67.222.222;
        208.67.220.220;
        };


        //========================================================================
        // If BIND logs error messages about the root key being expired,
        // you will need to update your keys.  See https://www.isc.org/bind-keys
        //========================================================================
        dnssec-validation auto;

        auth-nxdomain no;    # conform to RFC1035
        listen-on-v6 { any; };
};
" > /etc/bind/named.conf.options
#resolv conf
echo nameserver 172.26.47.253 >> /etc/resolvconf.conf

##
#
#Domains for ARP-Attacks
echo "zone \"injection.local\"{
        type master;
        file \"/etc/bind/zones/db.injection.local\";
        };
zone \"bank24.local\"{
        type master;
        file \"/etc/bind/zones/db.bank24.local\";
        };
zone \"news.local\"{
        type master;
        file \"/etc/bind/zones/db.news.local\";
        };
zone \"router.local\"{
        type master;
        file \"/etc/bind/zones/db.router.local\";
        };
zone \"tutorial.local\"{
        type master;
        file \"/etc/bind/zones/db.tutorial.local\";
        };
" >> /etc/bind/named.conf.local
mkdir /etc/bind/zones
#TODO Dummy Configuration

#DNS for router
echo "\$TTL 2h
@ IN SOA ns1.router.local. admin.router.local. (
    2017112701 ;
    3600       ;
    1800       ;
    604800     ;
    120 )      ;
@ IN NS ns1.router.local
  IN A 172.26.47.253

*       IN A 172.26.47.253
" >> /etc/bind/zones/db.router.local

#DNS for Tutorial
echo "\$TTL 2h
@ IN SOA ns1.router.local. admin.router.local. (
    2017112701 ;
    3600       ;
    1800       ;
    604800     ;
    120 )      ;
@ IN NS ns1.router.local
  IN A 172.26.112.1

*       IN A 172.26.112.1
" >> /etc/bind/zones/db.tutorial.local



#DNS for Payload
echo "\$TTL 2h
@ IN SOA ns1.router.local. admin.router.local. (
    2017112701 ;
    3600       ;
    1800       ;
    604800     ;
    120 )      ;
@ IN NS ns1.router.local
  IN A 172.26.32.8

*       IN A 172.26.32.8
" >> /etc/bind/zones/db.injection.local

#DNS for Bank24
echo "\$TTL 2h
@ IN SOA ns1.router.local. admin.router.local. (
    2017112700 ; serial
    3600       ; refresh
    1800       ; retry
    604800     ; expire
    120 )      ; ttl
@ IN NS ns1.router.local
  IN A 172.26.32.6

*       IN A 172.26.32.6
htsp    IN A 172.26.32.7
" >> /etc/bind/zones/db.bank24.local

#DNS for News
#
#
echo "\$TTL 2h
@ IN SOA ns1.router.local. admin.router.local. (
    2017112701 ;
    3600       ;
    1800       ;
    604800     ;
    120 )      ;
@ IN NS ns1.router.local
  IN A 172.26.32.5

*       IN A 172.26.32.5" >> /etc/bind/zones/db.news.local

#Install freeradius Server
apt-get install freeradius -y;
#Change Clients Password
sed -i 's/secret = testing123/secret = radius/g' /etc/freeradius/3.0/clients.conf

# Change eap default Type
sed -i 's/default_eap_type = md5/default_eap_type = peap/g' /etc/freeradius/3.0/mods-enabled/eap
# Add Users
echo "TestUser Cleartext-Password := \"HackMeHackMe\"" | sudo tee -a /etc/freeradius/3.0/users
# Add Hostapd Client to radius
echo "client 172.26.63.253 {
        secret = radius
        shortname = hostapd
}
" >> /etc/freeradius/3.0/clients.conf

## WLAN-AP-Host Einrichten
checkAPT;
apt-get install hostapd -y;

## Configure HOST-AP
# Configure new mac

# Get WLAN mac address and change to local administated
echo "# WLAN-Router-Betrieb

# Schnittstelle und Treiber
interface=wlan1
driver=nl80211

# FIRST AP WPA2
ssid=THISecWorkbenchWPA2
channel=1
hw_mode=g
#hw_mode=ag
ieee80211n=1
ieee80211d=1
country_code=DE
wmm_enabled=1

#
auth_algs=1
wpa=2
wpa_psk_file=/etc/hostapd-psk
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP TKIP
rsn_pairwise=CCMP
##WPS Config
# WPS state
# 0 = WPS disabled (default)
# 1 = WPS enabled, not configured
# 2 = WPS enabled, configured
wps_state=2
ap_setup_locked=0

# Enable control interface for PBC/PIN entry
ctrl_interface=/var/run/hostapd

# Enable internal EAP server for EAP-WSC (part of Wi-Fi Protected Setup)
eap_server=1

# When an Enrollee requests access to the network with PIN method, the Enrollee
# PIN will need to be entered for the Registrar. PIN request notifications are
# sent to hostapd ctrl_iface monitor. In addition, they can be written to a
# text file that could be used, e.g., to populate the AP administration UI with
# pending PIN requests. If the following variable is set, the PIN requests will
# be written to the configured file.
wps_pin_requests=/var/run/hostapd.pin-req

# Config Methods
# List of the supported configuration methods
# Available methods: usba ethernet label display ext_nfc_token int_nfc_token
#	nfc_interface push_button keypad virtual_display physical_display
#	virtual_push_button physical_push_button
config_methods=label virtual_display virtual_push_button keypad

device_name=USB2.0 WLAN
manufacturer=ATHEROS
model_name=WAP
model_number=123
serial_number=12345
device_type=6-0050F204-1
os_version=01020300

# Static access point PIN for initial configuration and adding Registrars
# If not set, hostapd will not allow external WPS Registrars to control the
# access point. The AP PIN can also be set at runtime with hostapd_cli
# wps_ap_pin command. Use of temporary (enabled by user action) and random
# AP PIN is much more secure than configuring a static AP PIN here. As such,
# use of the ap_pin parameter is not recommended if the AP device has means for
# displaying a random PIN.
ap_pin=12345670


# NFC password token for WPS
# These parameters can be used to configure a fixed NFC password token for the
# AP. This can be generated, e.g., with nfc_pw_token from wpa_supplicant. When
# these parameters are used, the AP is assumed to be deployed with a NFC tag
# that includes the matching NFC password token (e.g., written based on the
# NDEF record from nfc_pw_token).
#
#wps_nfc_dev_pw_id: Device Password ID (16..65535)
#wps_nfc_dh_pubkey: Hexdump of DH Public Key
#wps_nfc_dh_privkey: Hexdump of DH Private Key
#wps_nfc_dev_pw: Hexdump of Device Password

# Seconf AP WEP
# IEEE 802.11 specifies two authentication algorithms. hostapd can be
# configured to allow both of these or only one. Open system authentication
# should be used with IEEE 802.1X.
# Bit fields of allowed authentication algorithms:
# bit 0 = Open System Authentication
# bit 1 = Shared Key Authentication (requires WEP)

bss=wlan2
ssid=THISecWorkbenchWEPOpen
auth_algs=1
ignore_broadcast_ssid=0
wep_default_key=0
wep_key0=BC6AFE583E


# Seconf AP WEP
bss=wlan3
ssid=THISecWorkbenchWPA2-E
ieee8021x=1
wpa=2
wpa_key_mgmt=WPA-EAP
rsn_pairwise=CCMP
auth_algs=1
auth_server_addr=127.0.0.1
auth_server_port=1812
auth_server_shared_secret=radius


# AP WEP Open
bss=wlan4
ssid=THISecurityWorkbenchWEPShare
auth_algs=2
ignore_broadcast_ssid=0
wep_default_key=0
wep_key0=BC6AFE583E
# IEEE 802.11 specifies two authentication algorithms. hostapd can be
# configured to allow both of these or only one. Open system authentication
# should be used with IEEE 802.1X.
# Bit fields of allowed authentication algorithms:
# bit 0 = Open System Authentication
# bit 1 = Shared Key Authentication (requires WEP)

#AP for Security Workbench Website
bss=wlan5
ssid=THI Security Workbench


" > /etc/hostapd/hostapd.conf

echo "00:00:00:00:00:00 HackMeHackMe" | sudo tee -a /etc/hostapd-psk
chmod 600 /etc/hostapd/hostapd.conf
chmod 600 /etc/hostapd-psk
sed -i 's/#DAEMON_CONF=""/DAEMON_CONF=\"\/etc\/hostapd\/hostapd.conf\"/g' /etc/default/hostapd
systemctl enable hostapd
systemctl enable freeradius.service

# Build Docker Container
# ARP-Spoofing Container NEWS
export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/http/html'
chmod +x ../ARPspoofing/server/http/arphttpDockerControl.sh
../ARPspoofing/server/http/arphttpDockerControl.sh start

# ARP-Spoofing Container HTTPS NO-HSTS
#export export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/https/html'
#chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
#../ARPspoofing/server/https/arphttpsDockerControl.sh start

# ARP-Spoofing Container HTTPS HSTS
#export export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/https/html'
#chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
#../ARPspoofing/server/https/arphttpsDockerControl.sh start

# Tutorial Container 
#export export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/XYZ/server/html'
#chmod +x ../XYZ/server/XYZDockerControl.sh
#../XYZ/server/XYZDockerControl.sh start

echo "############################################################"
echo "Installion Complete Reboot needed."
echo "Info über WLAN-AP: NAME:PW"
echo "THISecurityWorkbenchWEPOpen/Share: BC6AFE583E"
echo "THISecurityWorkbenchWPA2: HackMeHackMe"
echo "THI SecurityWorkbenchWPA2-E: User: TestUser PW: HackMeHackMe"
echo "Genauere Informationen findet man in der Dokumentation"
echo "RPI wird in 30 Sekunden Automatisch neu-gestartet mit ctrl +c Abbrechen"
echo "############################################################"
sleep 30
sudo reboot
