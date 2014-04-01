import KyanToolKit_Py
import EncryptKey
import string
ktk = KyanToolKit_Py.KyanToolKit_Py()

#--Key Generation-------------------------------------------------
# print(ktk.banner("Key Initiation"))
# key = ktk.getInput("Please Enter Your Key")
# if "" == key:
# 	ktk.Err("Input key please")
key = "abcde"

#--init-----------------------------------------------------------
while True:
	ktk.clearScreen()
	# get input
	print(ktk.banner("Encryption: " + "key = " + key))
	original = ktk.getInput("Please Enter Your Words:")
	# original = "I'm coming"
	ciphered = ""
	for i in range(len(original)):
		if original[i] in string.ascii_letters:
			ciphered += str(ord(original[i]) ^ ord(key[i%len(key)])) + "-"
		else:
			ciphered += original[i]
	print(ciphered)

	ktk.pressToContinue("Press any key to continue ...")
