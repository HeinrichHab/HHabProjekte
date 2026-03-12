# Bruteforce IP Scanner

## TL;DR
Dieses Skript analysiert die `auth.log` auf fehlgeschlagene
SSH Loginversuche und identifiziert potenzielle Bruteforce Angriffe.
Version 2 nutzt striktes Exceptionhandling und verhindert Abstürze.
Version 1 ist ein Proof of Concept ohne Error Handling und erfüllt
keine Secure Coding Standards.

## Funktionsweise
Das Skript liest die Systemdatei `/var/log/auth.log` Zeile für Zeile
aus. Es sucht nach dem String "Failed password", extrahiert die
dazugehörige IP Adresse und zählt die Vorfälle. Überschreitet eine
IP Adresse das Limit von 10 Fehlversuchen, wird sie als verdächtig
eingestuft und im Terminal ausgegeben.

## Versionsvergleich & IT-Sicherheit
Der technische Unterschied liegt in der Fehlerbehandlung.

**Version 1 (Proof of Concept)**
* **Keine Fehlertoleranz:** Das Skript stürzt sofort ab, wenn die
  Datei nicht existiert (`FileNotFoundError`), Berechtigungen fehlen
  (`PermissionError`) oder Logzeilen unerwartet formatiert sind
  (`IndexError`).
* **Sicherheitsrisiko:** Ein Sicherheitstool, das bei Fehlern
  abbricht, verliert seine Verfügbarkeit und bietet keinen Schutz.
 
  **Version 2 (Produktionsnah)**
* **Robustes Exceptionhandling:** Dateizugriffe und das String Parsing
  sind in Try Blöcke gekapselt.
* **Failsafe Design:** Einzelne fehlerhafte Logzeilen werden
  übersprungen (`pass`), anstatt den Scan abzubrechen.
* **Informative Fehlermeldungen:** Der Benutzer erhält konkrete
  Hinweise (z. B. auf fehlende Rootrechte). Das Skript gibt keine
  kryptischen Systemmeldungen aus, die potenziellen Angreifern
  sensible Details über das System verraten könnten.
* **Erfüllte Standards:** Entspricht CWE-755 (Improper Handling
  of Exceptional Conditions). Fehler in der Logdatei führen nicht
  zum Ausfall der Überwachung.
