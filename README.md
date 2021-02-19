# Lumenaria-Utilities-bot
## Cos'è
Lumenaria Utilities è un bot che aiuta la micronazione [Lumenaria](https://t.me/RepubblicaLumenaria) nella gestione dei cittadini
## Le funzionalità
La versione attualmente più aggiornata (18/02/2021) permette di importare una **lista JSON** di cittadini già esistente ed aggiungere o eliminare un cittadino dalla lista.
Esempio di lista:  
```
["Nome Cognome @Tag", "Nome2 Cognome2 @Tag2"]
```
Per creare una lista vuota creare un file inserire `[]`.

## I comandi
Comandi implementati fino ad ora:
```
/start                         - Inizializza il bot
/newlist                       - Aggiungi una lista di cittadini taggando il file json
/cittadini                     - Mostra la lista di cittadini registrata
/newcit <nome> <cognome> <*username> - Aggiunge un cittadino alla lista
/delcit <posizione-lista>      - Rimuove un cittadino dalla lista
/getlist                       - Manda la lista importata più recente

*opzionale
```  
# Eseguire il codice
Per poter eseguire il bot è necessaria la libraria [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
## Installazione delle dipendenze
### Via pip
Soddisfatto questo requisito, dal prompt dei comandi/terminale si esegue  
`$ pip install python-telegram-bot`.  
In caso non dovesse funzionare, provare  
`$ python -m pip install python-telegram-bot`
### Via git
Un'alternativa a pip sarebbe utilizzando git (Assicurarsi di avere git installato):
``` 
  $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
  $ cd python-telegram-bot
  $ python setup.py install
```
## Eseguire il codice
Per eseguire il codice, sempre da cmd o bash, lanciare il seguente comando:  
`$ python3 bot.py`
