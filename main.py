import pywhatkit
import random
import datetime

class WeihnachtsBot:
    def __init__(self, name, kontakte):
        self.name = name
        self.kontakte = kontakte
        # this list contains 4 different phrases,
        # of which one is chosen randomly and placed in the message
        self.phrasen = [
            "Frohe Weihnachten",
            "Frohes Fest!",
            "Happy Xmas!",
            "Merry Christmas!"
        ]

        #simular to the phrase list, this one contains emojis
        #using the CLDR short name. Here, in total seven are selected randomly
        #and placed in the message
        self.emoji = [
                    "\N{Christmas tree}",
                      "\N{bell}",
                      "\N{snowflake}",
                      "\N{candle}",
                      "\N{Baby Angel}",
                      "\N{Heart with Ribbon}",
                      "\N{Snowman}",
                      "\N{Glowing Star}",
                      "\N{sled}",
                      "\N{cookie}",
                      "\N{candy}",
                      ]
        #the current year is imported
        self.jahr = datetime.date.today().year

    def erstelle_nachricht(self, person):

        #the message is generated. This methode is called
        #by the sende_nachricht methode later
        nachricht = (
            f"Hallo {person[0]}!\n"
            f"{random.choice(self.emoji)}{random.choice(self.emoji)}{random.choice(self.emoji)}\n"
            f"Ich hoffe, du hast ein schönes Fest {self.jahr} mit deinen Liebsten und bekommst tolle Geschenke! "
            f"{random.choice(self.emoji)}\n"
            f"{random.choice(self.phrasen)} {random.choice(self.emoji)}{random.choice(self.emoji)}{random.choice(self.emoji)}\n"
            f"Komm gut ins Jahr {self.jahr + 1}!\n"
            f"Herzliche Grüße {self.name}"
        )
        return nachricht

    def sende_nachrichten(self)\
            :
        """This methode uses a for-loop to iterate through the contacts. For each contact,
        the erstelle_nachricht_methode is called. Once created, the message is sent instantly
        using the sendwhatmsg_instantly methode from pywhatkit. Pywhatkit also offers methodes
        to send messages at a certain time. Check out the documentation: https://pypi.org/project/pywhatkit/"""
        for person in self.kontakte:
            nachricht = self.erstelle_nachricht(person)
            try:
                pywhatkit.sendwhatmsg_instantly(person[1], nachricht)
                print(f"Nachricht erfolgreich an {person[0]} gesendet!")
            except Exception as e:
                print(f"Fehler beim Senden an {person[0]}: {e}")

if __name__ == "__main__":

    """If you want to use the code, you have to
    change this part. All else can stay the same."""

    #enter your name in the name variable
    name = "{mein_name}"
    #fill the tuple list with the information of the people you want to send the message to.
    #Note: the name you put here will be the name the people are addressed with in the message.
    #So don't use any stupid nicknames like "idiot brother"
    kontakte = [
         ("Papa", "+49 22222222"),
        ("Sam", "+49 22223333"),
        ("{kontakt_name}", "{telefon_nummer}")]


    bot = WeihnachtsBot(name, kontakte)
    bot.sende_nachrichten()


