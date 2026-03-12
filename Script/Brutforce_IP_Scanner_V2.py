ip_counts = {} 

# Start des ersten Try Blocks für den Dateizugriff
try:
    with open("/var/log/auth.log", "r") as file: 
        for line in file: 
            if "Failed password" in line: 
                # Start des zweiten Try Blocks für das String Parsing
                try:
                    ip_address = line.split(" from ")[1].split(" port")[0]
                    
                    if ip_address in ip_counts:
                        ip_counts[ip_address] = ip_counts[ip_address] + 1 
                    else:
                        ip_counts[ip_address] = 1
                        
                except IndexError:
                    # Wenn das Logformat abweicht, überspringen wir diese defekte Zeile, 
                    # anstatt das ganze Script abstürzen zu lassen.
                    pass 

except FileNotFoundError:
    print("Kritischer Fehler: Die Logdatei /var/log/auth.log existiert nicht.")
except PermissionError:
    print("Kritischer Fehler: Keine Berechtigung. Führe das Script mit Root Rechten aus.")
except Exception as e:
    # Fängt alle anderen, unvorhergesehenen Systemfehler ab
    print(f"Unbekannter Systemfehler beim Lesen der Datei: {e}")

# Auswertung der aggregierten Daten
print("--- Verdächtige IP Adressen (Fehlversuche > 10) ---")
for ip, count in ip_counts.items():
    if count > 10:
        print(f"IP Adresse: {ip} | Anzahl: {count}")