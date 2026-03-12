# Simulation: Mainstream Capital Bank

## TL;DR
Analyse eines Phishingangriffs auf VPN Zugangsdaten via Typosquatting.
Simulation der Untersuchung in einer Microsoft Sentinel Umgebung zur
Validierung von SOC L1 Analysefähigkeiten.

## Alert Details (Sentinel Schema)
Die Investigation wird durch den folgenden Systemalarm ausgelöst. Die
Struktur spiegelt das technische Alertschema der SIEM Instanz wider:

| Eigenschaft | Technischer Wert |
| :--- | :--- |
| **Alert Name** | High Volume Suspicious Inbound Mail |
| **Severity** | Medium |
| **Timestamp** | 20. Mai 2026, 14:30:15 |
| **Sender** | `security-noreply@mainstreancapital-verify.com` |
| **Subject** | DRINGEND: Sicherheitslücke in Ihrem Onlinebanking Zugang |
| **Phishing URL** | `hxxps://mainstreancapital-auth.net/login/verify.php` |

## Datenstruktur & Telemetrie
Für die Aufklärung stehen folgende Tabellen zur Verfügung, um den
Impact des Angriffs auf die Infrastruktur zu bewerten:

| Tabellenname | Verfügbare Spalten (Auszug) |
| :--- | :--- |
| **EmailEvents** | Timestamp, SenderMailFromAddress, Subject, SenderIPv4 |
| **UrlClickEvents** | Timestamp, UserEmail, Url, IsClickedThrough |
| **SigninLogs** | Timestamp, UserPrincipalName, IPAddress, ResultType |
| **DeviceNetwork** | Timestamp, DeviceName, RemoteUrl, InitiatingProcess |

## Hinweis zur Struktur
In diesem Dokument wird die Ausgangslage definiert. Die technischen
KQL Queries zur Extraktion der Daten, die Liste der betroffenen User
sowie die finalen Härtungsempfehlungen befinden sich in den
Unterdateien dieser Simulation.
