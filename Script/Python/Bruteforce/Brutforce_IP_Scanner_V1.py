ip_counts={} 
with open("/var/log/auth.log", "r") as file: 
    for line in file: 
        if "Failed password" in line: 
            ip_address = line.split(" from ")[1].split(" port")[0]
            if ip_address in ip_counts:
                ip_counts[ip_address] =ip_counts[ip_address]+1 
            else:
                ip_counts[ip_address]=1
for ip, count in ip_counts.items():
    if count > 10:
        print(f"IP Adresse: {ip} | Anzahl: {count}")
