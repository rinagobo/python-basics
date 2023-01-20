morse_dic = {
           'A':'.-', 'B':'-...',
           'C':'-.-.', 'D':'-..', 'E':'.',
           'F':'..-.', 'G':'--.', 'H':'....',
           'I':'..', 'J':'.---', 'K':'-.-',
           'L':'.-..', 'M':'--', 'N':'-.',
           'O':'---', 'P':'.--.', 'Q':'--.-',
           'R':'.-.', 'S':'...', 'T':'-',
           'U':'..-', 'V':'...-', 'W':'.--',
           'X':'-..-', 'Y':'-.--', 'Z':'--..',
           '1':'.----', '2':'..---', '3':'...--',
           '4':'....-', '5':'.....', '6':'-....',
           '7':'--...', '8':'---..', '9':'----.',
           '0':'-----'
}

user_mess = input("Write your message that you want to encode! (Use characters only from 'A' to 'Z' and numbers from '1' to '0'.)\n")
# print(user_mess.upper())

morse_mess = ""
for char in user_mess.upper():
    if char == " ":
        char_morse = "\n"
        morse_mess = morse_mess + char_morse
    else:
        char_morse = morse_dic[char]
        if morse_mess == "":
            morse_mess = '   ' + morse_mess + char_morse
        else:
            morse_mess = morse_mess + '   ' + char_morse



print(f"Your message using Morse Code is: \n{morse_mess}\n"
      f"\nHow to read the code: \nEvery word is shown in a new line, in order and there is a space between every characters.")

