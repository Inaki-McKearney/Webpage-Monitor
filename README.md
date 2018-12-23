# Webpage-Monitor
A python tool to periodically check a web page and send an email alert regarding html changes  
Designed for personal use and has proved extremely useful for regularly checking ticket sites etc.  
Work needed as tool currently picks up every change, including arbitrary values. As such, it works best on smaller websites

## Prerequisites
Python 3.6+ needed as f-strings  are used  
Can easily be replaced with other string formatting if needed for older python versions such as the Raspberry Pi default

## Usage
For best results run with cron or another scheduler  
Can be run manually to view web page changes since the last time script was run  

**In ```Monitor.py```**  
Change the link and use the methods as shown in the example:
```python
    link = 'https://en.wikipedia.org/wiki/Main_Page'
    wiki_updater = Changes(link)
    wiki_updater.update()
    if wiki_updater.diff():
        wiki_updater.email()
```

**In ```EmailAlert.py```**  
Change the following email details:
```python
    username = 'EMAIL/USERNAME'
    password = 'EMAIL PASSWORD'
    fromaddr = 'SENDER EMAIL'
    toaddr = 'RECEIVER EMAIL'
```
**Note:** for non-Gmail users, the following line will need modified:
```python
    server = smtplib.SMTP('smtp.gmail.com', 587)
```
