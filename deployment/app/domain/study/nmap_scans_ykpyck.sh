#!/bin/bash

# target hostname or IP address
target="securityupdated.com"
ports="1-1024"

output_file="nmap_results.txt"

# nmap commands
echo "Nmap scan: TCP and UDP scan with PSH scanflags" >> $output_file
sudo nmap -v -p $ports -sX -sU $target --scanflags PSH -Pn >> $output_file

echo ""
echo "Nmap scan: Fast scan of the most common ports" >> $output_file
nmap -v -p $ports -sX -sU $target --scanflags PSH -Pn >> $output_file

echo ""
echo "Nmap scan: Aggressive scan with OS detection" >> $output_file
nmap -v -p $ports -A -T4 $target -Pn >> $output_file

echo ""
echo "Nmap scan: HTTP vulnerability script scan" >> $output_file
nmap -v -p $ports --script http-vuln* $target -Pn >> $output_file

echo ""
echo "Nmap scan: Service version detection" >> $output_file
nmap -v -p $ports -sV $target -Pn >> $output_file

echo ""
echo "Nmap scan: SSL/TLS enumeration on port 443" >> $output_file
nmap --script ssl-enum-ciphers -p 443 $target -Pn >> $output_file