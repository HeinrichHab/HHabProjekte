Analyse einer Phishingmail (10. März 2026)

TL;DR 
Dieses Projekt dokumentiert die systematische Untersuchung einer realen, am 10. März 2026 empfangenen Phishingmail. Ziel des Angriffs war der Diebstahl von Zugangsdaten der Advanzia Bank.
Die Analyse belegt praktische Fähigkeiten in der Bedrohungserkennung, der Anwendung von OSINT Methoden und der Ableitung konkreter Schutzmaßnahmen für die IT-Sicherheit.

Kernfakten der Analyse

    Angriffsvektor: Missbrauch eines legitimen Marketingdienstleisters (Constant Contact, Server IP: 208[.]75[.]122[.]14),
    um standardisierte Spamfilter zu umgehen.

    Täuschung: Nutzung von Namensfälschungen (Typosquatting) im Absendernamen (loginADVANZIA[.]app statt Advanzia)
    und in der Adresse (advanzla-maildrop[.]cc@sharedl[.]ccsend[.]com).

    Infrastruktur: Die gefälschte Loginseite wurde auf der kompromittierten Domain juanjosesese[.]com gehostet.
    Eine OSINT Recherche (RDAP) ergab, dass diese Domain bereits am 16. April 2008 registriert wurde.
    Das extrem hohe Alter wird gezielt genutzt, um Reputationssysteme auszutricksen.

    Verschlüsselung: Die Angreifer nutzten kostenlose Zertifikate (Let's Encrypt) für gezielte Subdomains
    (z. B. hxxps://advanzla-caseid[.]juanjosesese[.]com),
    um verschlüsselte Internetseiten bereitzustellen und falsche Sicherheit zu suggerieren.

Nachgewiesene Kompetenzen

    Vektoranalyse: Auswertung von Headerdaten und E-Mail Authentifizierung (SPF, DKIM, DMARC).

    Informationsbeschaffung: Nutzung von Netzwerkrecherchen und Zertifikatsregistern (crt[.]sh)
    zur Aufdeckung der feindlichen Infrastruktur.

    Vorfallsreaktion: Formulierung präziser technischer Abwehrmaßnahmen, wie die dynamische Prüfung von Links exakt beim Anklicken
    (statt beim Posteingang) und der zwingende Einsatz physischer Sicherheitsschlüssel (MFA).
