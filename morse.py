user_message = raw_input('Enter your message: ')
n = len(user_message)

morse_code = {'A': '.-', 'B': '---.', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K':  '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': ' ', }

translated = []
for i in range(n):
	letter = user_message[i]	
	
	if letter.isalnum():
		morse = morse_code[letter.upper()]
		translated.append(morse)
	else:
		translated.append(letter)
	
print ' '.join(translated)
	


	


