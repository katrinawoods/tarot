class Card(object):
    def __init__(self, name, suit, value, description):
        self.name = name
        self.suit = suit
        self.value = value
        self.description = description


cards = [
    Card("The Joker","jokers",1,"innocence, spontenaiety"),
    Card("The Magician", "jokers", 2,"power, resourcefulness"),
    Card("The High Priestess", "jokers", 3, "intuition, subconscious"),
    Card("The Empress","jokers",4,"nature, abudance"),
    Card("The Emperor","jokers",5, "authority"),
    Card("The Hierophant","jokers",6,"conformity, tradition"),
    Card("The Lovers","jokers",7,"harmony"),
    Card("The Chariot","jokers",8,"willpower"),
    Card("Strength","jokers",9,"courage, influence"),
    Card("The Hermit","jokers",10,"soul searching"),
    Card("Wheel of Fortune", "jokers",10,"destiny, turning point"),
    Card("Justice","jokers",11,"truth, cause and effect"),
    Card("The Hanged Man","jokers",12,"pause, surrender"),
    Card("Death","jokers",13,"change, transformation"),
    Card("Temperance","jokers",14,"balance, patience"),
    Card("The Devil","jokers",15,"shadow self, sexuality"),
    Card("The Tower","jokers",16,"chaos, upheaval"),
    Card("The Star","jokers",17,"hope, faith"),
    Card("The Moon","jokers",18,"fear, anxiety"),
    Card("The Sun","jokers",19,"success, joy"),
    Card("Judgement","jokers",20,"rebirth"),
    Card("The World","jokers",21,"accomplishment, travel"),
    Card("Ace of Pentacles","pentacles",1,"opportunity"),
    Card("Two of Pentacles","pentacles",2,"priorities"),
    Card("Three of Pentacles","pentacles",3,"teamwork"),
    Card("Four of Pentacles","pentacles",4,"saving"),
    Card("Five of Pentacles","pentacles",5,"loss, worry"),
    Card("Six of Pentacles","pentacles",6,"generosity"),
    Card("Seven of Pentacles","pentacles",7,"perseverance"),
    Card("Eight of Pentacles","pentacles",8,"mastery"),
    Card("Nine of Pentacles","pentacles",9,"luxury"),
    Card("Ten of Pentacles","pentacles",10,"wealth"),
    Card("Page of Pentacles","pentacles",11,"manifestation"),
    Card("Knight of Pentacles","pentacles",12,"hard work, routine"),
    Card("Queen of Pentacles","pentacles",13,"nurturing, providing"),
    Card("King of Pentacles","pentacles",14,"wealth, security"),
    Card("Ace of Swords","swords",1,"ideas, success"),
    Card("Two of Swords","swords",2,"impasse"),
    Card("Three of Swords","swords",3,"heartbreak, sorrow"),
    Card("Four of Swords","swords",4,"rest, recuperation"),
    Card("Five of Swords","swords",5,"conflict"),
    Card("Six of Swords","swords",6,"change"),
    Card("Seven of Swords","swords",7,"betrayal"),
    Card("Eight of Swords","swords",8,"victimhood"),
    Card("Nine of Swords","swords",9,"anxiety"),
    Card("Ten of Swords","swords",10,"crisis, pain, betrayal"),
    Card("Page of Swords","swords",11,"curiosity"),
    Card("Knight of Swords","swords",12,"ambition"),
    Card("Queen of Swords","swords",13,"clarity"),
    Card("King of Swords","swords",14,"truth"),
    Card("Ace of Cups","cups",1,"love"),
    Card("Two of Cups","cups",2,"mutual attraction"),
    Card("Three of Cups","cups",3,"celebration, friendship"),
    Card("Four of Cups","cups",4,"meditation, contemplation"),
    Card("Five of Cups","cups",5,"regret, failure"),
    Card("Six of Cups","cups",6,"innocence"),
    Card("Seven of Cups","cups",7,"opportunities"),
    Card("Eight of Cups","cups",8,"disappointment, abandonment"),
    Card("Nine of Cups","cups",9,"gratitude, contentment"),
    Card("Ten of Cups","cups",10,"divine love, bliss"),
    Card("Page of Cups","cups",11,"creativity"),
    Card("Knight of Cups","cups",12,"romance"),
    Card("Queen of Cups","cups",13,"compassion, intuition"),
    Card("King of Cups","cups",14,"diplomatic, emotionally balanced"),
    Card("Ace of Wands","wands",1,"growth, potential"),
    Card("Two of Wands","wands",2,"plans,decisions"),
    Card("Three of Wands","wands",3,"progress, expansion"),
    Card("Four of Wands","wands",4,"celebration, joy"),
    Card("Five of Wands","wands",5,"conflict"),
    Card("Six of Wands","wands",6,"success"),
    Card("Seven of Wands","wands",7,"challenge, protection"),
    Card("Eight of Wands","wands",8,"movement, travel"),
    Card("Nine of Wands","wands",9,"resilience, courage"),
    Card("Ten of Wands","wands",10,"burden, hard work, completion"),
    Card("Page of Wands","wands",11,"inspiration"),
    Card("Knight of Wands","wands",12,"energy, passion"),
    Card("Queen of Wands","wands",13,"determination, independence"),
    Card("King of Wands","wands",14,"vision, leadership")
]

day = int(input("What date were you born (dd)? "))
month = input("What month were you born in? (mm)? ")

if month == '12':
	astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
elif month == '01':
	astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == '02':
	astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
elif month == '03':
	astro_sign = 'Pisces' if (day < 21) else 'Aries'
elif month == '04':
	astro_sign = 'Aries' if (day < 20) else 'Taurus'
elif month == '05':
	astro_sign = 'Taurus' if (day < 21) else 'Gemini'
elif month == '06':
	astro_sign = 'Gemini' if (day < 21) else 'Cancer'
elif month == '07':
	astro_sign = 'Cancer' if (day < 23) else 'Leo'
elif month == '08':
	astro_sign = 'Leo' if (day < 23) else 'Virgo'
elif month == '09':
	astro_sign = 'Virgo' if (day < 23) else 'Libra'
elif month == '10':
	astro_sign = 'Libra' if (day < 23) else 'Scorpio'
elif month == '11':
	astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

if astro_sign == 'Pisces':
  astro_card = 'The Moon'
elif astro_sign == 'Aries':
    astro_card = 'The Emperor'
elif astro_sign == 'Taurus':
  astro_card = 'The Hierophant'
elif astro_sign == 'Gemini':
  astro_card = 'The Lovers'
elif astro_sign == 'Cancer':
  astro_card = 'The Chariot'
elif astro_sign == 'Leo':
  astro_card = 'Strength'
elif astro_sign == 'Virgo':
  astro_card = 'The Hermit'
elif astro_sign == 'Libra':
  astro_card = 'Justice'
elif astro_sign == 'Scorpio':
  astro_card = 'Death'
elif astro_sign == 'Sagittarius':
  astro_card = 'Temperance'
elif astro_sign == 'Capricorn':
  astro_card = 'The Devil'
elif astro_sign == 'Aquarius':
  astro_card = 'The Star'

import random
random.shuffle(cards)

print(astro_card + " channels " + astro_sign + " energy into the deck.")

print("Your Tarot card for today is the " + cards[0].name + ": " + cards[0].description)
