# Lumenaria-Utilities-bot
----
## Cos'è
Lumenaria Utilities è un bot che aiuta la micronazione [Lumenaria](https://t.me/RepubblicaLumenaria) nella gestione dei cittadini
## Le funzionalità
La versione attualmente più aggiornata (16/02/2021) permette di importare una lista JSON di cittadini già esistente ed aggiungere o eliminare un cittadino dalla lista
## I comandi
I comandi attualmente presenti sono:
1. /start - Inizializza il bot
1. /newlist - Aggiungi una lista di cittadini
1. /cittadini - Mostra la lista di cittadini registrata
1. /newcit <nome> <cognome> <*username> *opzionale - Aggiunge un cittadino alla lista
1. /delcit <posizione-lista> - Rimuove un cittadino dalla lista
2. /getlist - Manda la lista importata più recente
----
# Dipendenze
----
Per la creazione di questo bot ho usato la libreria [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
Per eseguire il bot l'installazione di tale libreria è necessaria.
## Installazione della libreria
### Via pip
Soddisfatto questo requisito, dal prompt dei comandi/terminale si esegue `pip install python-telegram-bot`. In caso non dovesse funzionare, provare
`python -m pip install python-telegram-bot`
### Via git
Un'alternativa a pip sarebbe utilizzando git (Assicurarsi di avere git installato):
1. `git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive`
2. `cd python-telegram-bot`
3. `python setup.py install`
## Eseguire il codice
Per eseguire il codice, sempre da cmd o bash, lanciare il seguente comando:
`python3 bot.py`
