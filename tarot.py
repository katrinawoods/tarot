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
    Card("King of Cups","cups",14,"diplomatic, emotionally balanced")
]


import random
random.shuffle(cards)
print(cards[0].name)
print(cards[0].description)

## for c in cards: 
##	print(c.description)
    