def crypto(privateText, mode):
	''' A modified reverse cipher algorithm function for encryption and decryption '''
	keys = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,.!@#$%&*^?/"'
	value = keys[::-1]
	if mode.upper() == 'E':
		encrypyDict = dict(zip(keys, value))
		newMessage = ''.join([encrypyDict[letter] for letter in privateText.lower()])
	elif mode.upper() == "D":
		decryptDict = dict(zip(value, keys))
		newMessage = ''.join([decryptDict[letter] for letter in privateText.lower()])
	else:
		newMessage = "Sorry, try again!"
		print("Invalid input given")
	return newMessage

# def encrypt(text,s):
# result = ""
#    # transverse the plain text
#    for i in range(len(text)):
#       char = text[i]
#       # Encrypt uppercase characters in plain text
#       if (char.isupper()):
#          result += chr((ord(char) + s-65) % 26 + 65)
#       # Encrypt lowercase characters in plain text
#       else:
#          result += chr((ord(char) + s - 97) % 26 + 97)
#       return result