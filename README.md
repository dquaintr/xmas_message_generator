This Script generates a christmas message (in german) and automatically sends it over Whatsapp.
(Note: you need to be logged in to Whatsapp on the device you are running this code on, either in the Web Browser or the App.)

Using a list of tuples with the contact name and contact phonenumber, a message is created for 
each contact and sent using the pywhatkit library (pip install pywhatkit): https://pypi.org/project/pywhatkit/.

The message has the basic form:

"Hello [name],

emoji/emoji/emoji

Ich hoffe, du hast ein schönes Fest [aktuelles Jahr] mit deinen Liebsten und bekommst tolle Geschenke!
emoji
[Phrase] emoji, emoji, emoji
Komm gut ins Jahr [nächstes Jahr]
Herzliche Grüße [name]"

The emojis and phrases are randomly selected from a set. In this form, the code can generate 78 million different versions
of the message. Of course you can add your own, thus increasing the possible combinations even more.

