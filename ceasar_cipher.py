from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

#def caeser2(input_text, shift_amount, shift_direction):
#    output_text=""
#    for letter in input_text:
#        if letter not in alphabet:
#            output_text += letter
#        else:
#            input_index = alphabet.index(letter)
#            if shift_direction == "encode":
#                shifted_index = input_index + shift_amount
#            else:
#                shifted_index = input_index - shift_amount
#            if shifted_index > len(alphabet) - 1:
#                shifted_index -= len(alphabet)
#            output_text += alphabet[shifted_index]
#    print(f"{shift_direction}d output: {output_text}")

def caeser(input_text, shift_amount, shift_direction):
    output_text=""
    if shift_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter not in alphabet:
            output_text += letter
        else:
            input_index = alphabet.index(letter)
            shifted_index = input_index + shift_amount
            #if shifted_index > len(alphabet) - 1:
            #    shifted_index -= len(alphabet)
            output_text += alphabet[shifted_index]
    print(f"{shift_direction}d output: {output_text}")

done = False
clear()
print(logo)

while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    # valid_shift_input = False
    # while not valid_shift_input:
    #     shift = int(input("Type the shift number:\n"))
    #     if shift > 25 or shift < -25:
    #         print("Shift value must be between -25 and 25. Please enter a valid shift amount.")
    #     else:
    #         valid_shift_input = True

    caeser(input_text=text, shift_amount=shift, shift_direction=direction)
    again = input("\nType 'yes' if you want to encode/decode again. Otherwise type 'no'.\n")
    if again == "no":
        print("Goodbye.")
        done = True

