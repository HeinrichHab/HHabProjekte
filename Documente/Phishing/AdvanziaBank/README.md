# Phishing Analyse: Advanzia Bank (März 2026)

## TL;DR
Dokumentation einer realen Phishingmail vom 10. März 2026 zum
Diebstahl von Advanzia Bank Zugangsdaten. Die Analyse belegt
praktische Fähigkeiten in der Bedrohungserkennung, OSINT Methoden
und der Umsetzung von IT-Sicherheit Standards.

## Analyseergebnisse
Die Untersuchung der E-Mail offenbart eine hochgradig gezielte
Vorgehensweise der Angreifer:

* **Angriffsvektor:** Missbrauch des Marketingdienstleisters
    Constant Contact (IP: 208[.]75[.]122[.]14), um technische
    Standardspamfilter zu umgehen.
* **Täuschung:** Einsatz von Typosquatting im Absendernamen
    (`loginADVANZIA.app`) und in der Absenderadresse.
* **Infrastruktur:** Nutzung der kompromittierten Domain
    `juanjosesese.com` (registriert 2008). Das hohe Alter der
    Domain wird gezielt genutzt, um Reputationssysteme zu täuschen.
* **Verschlüsselung:** Einsatz von Let's Encrypt Zertifikaten für
    Subdomains, um durch das HTTPS Symbol im Browser falsche
    Sicherheit zu suggerieren.

## Kompetenznachweis & Standards
Die Analyse deckt Kernbereiche moderner IT-Sicherheit ab:

**Technisches Audit**
* **Headeranalyse:** Prüfung von E-Mail Authentifizierungsdaten
    wie SPF, DKIM und DMARC zur Verifikation der Absenderidentität.
* **OSINT Recherche:** Nutzung von RDAP und Zertifikatsregistern
    (`crt.sh`) zur Identifizierung feindlicher Infrastruktur.

**Vorfallsreaktion (Incident Response)**
* **Abwehrmaßnahmen:** Ableitung präziser Schutzstrategien wie
    dynamische Linkprüfung (Time of Click Protection) und der
    Einsatz physischer Sicherheitsschlüssel (FIDO2/MFA).
* **ISO 27001 Bezug:** Entspricht der Maßnahme A.5.7 (Threat
    Intelligence) durch das Sammeln und Auswerten von Informationen
    über Bedrohungen, um das Sicherheitsbewusstsein zu stärken.
