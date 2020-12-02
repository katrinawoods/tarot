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
print("Your Zodiac sign is :",astro_sign)

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
    
print("Your Tarot card is :",astro_card)
