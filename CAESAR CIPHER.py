#CAESAR CIPHER
message = "GibsonGodsan"
index = 0
while index<len(message):
	letter = message[index]
	print(chr(ord(letter)+6), end=' ')
	index += 1