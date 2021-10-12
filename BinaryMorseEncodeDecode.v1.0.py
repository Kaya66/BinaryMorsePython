######################################################
# Binary Morse Encode/Decode                         #
# Author: OpSecCat                                   #
# Version 1.0                                        #
# Licenses GPLv3                                     #
######################################################
def main():
    #alphabet defines what characters are addrssable
    #binary is the morse/binary conversion of the alphabet.
    #it is important that any edits to either one be adjusted in the other. the order is important to proper addressing of characters to their binary counterpart and vice versa.
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," "]
    binary = ["10000010","01110100","01010100","01100011","10000001","11010100","00100011","11110100","11000010","10000100","01000011","10110100","00000010","01000010","00000011","10010100","00100100","10100011","11100011","00000001","11000011","11100100","10000011","01100100","01000100","00110100","00000101","10000101","11000101","11100101","11110101","11111101","01111101","00111101","00011101","00001101","00000111"]
######################################################
    def encode(alpha,bin,text):
        enc_result = []
        length = len(text)
        for x in range (0, int(length)):
            for y in range (0, 36):
                if (alpha[36] == text[x]):
                    enc_result.append(binary[36])
                    break
                elif (alpha[y] == text[x]):
                    enc_result.append(binary[y])
                    break
                else:
                    pass
        encode_format(enc_result)
        #the encoder takes the alphabet and binary arrays for comparison to the user supplied text.
        #the user supplied text then has each character compared to the alphabet.
        #when a match is found. take the posiiton of the match form alphabet and get the binary segment form that same position and adds it to the encode_result.
        #then its sent to the formater.
######################################################
    def decode(alpha, bin, enc_text):
        dec_result = []
        for x in range (0, int(len(enc_text))):
            for y in range (0, 36):
                if (enc_text[x] == bin[36]):
                    dec_result.append(alpha[36])
                    break
                elif (enc_text[x] == bin[y]):
                    dec_result.append(alpha[y])
                    break
        decode_format(dec_result)
        #does the same thing as encode but in reverse. compare the binary block from enc_text to binary.  when a match is found, add the alphabet positoin to dec_result
######################################################
    def encode_format(encoded_text):
        finalstring = ' '.join(encoded_text)
        print(finalstring)
        #remove strange formatting from arrays in python.  prints out just a clean line of binary separated by spaces.
######################################################
    def decode_format(decoded_text):
        finalstring = ''.join(decoded_text)
        print(finalstring)
        #removes strange formatting from arrays in python. prints out a clean line of text.
######################################################
    def start():
        selection = input("Please select (E)ncode, or (D)ecode: ")
        non_array_text = input("Input your text to encode/decode: ")
        non_array_text1 = non_array_text.lower()
        text = []
        #the top sectoion takes input from the user and sets it to lower case as the program has no case sensitivity.
        if (selection == "e" or selection == "E"):
            for x in range (0, int(len(non_array_text1))):
                if(non_array_text1[x] == alphabet[36]):
                    text.append(alphabet[36])
                else:
                 text.append(non_array_text1[int(x)])
            encode(alphabet, binary, text)
        #E is for Encode.   takes the user input and piece by piece, puts each character (spaces included) into an array to pass onto the encoder.
        elif (selection == "d" or selection == "D"):
            text = non_array_text1.split(' ')
            decode(alphabet, binary, text)
        #D is for Decode.   Takes the user supplied binary morse with each byte separated by a space, and dumps it into an array using the space as the separateor for words.
        else:
            print("invalid selection, Try again.")
            start()
        #if supplied the wrong input in selection, throw error and restart the input selectoin dialogue.
        #i may go back and re-arrange selection so it will throw an error immediately if supplied a wrong input.
    start()
main()
#Little explination on how the binary / morse code system works
#in morse, you can write out any standard letters and numbers with a max of 5 dots or dashes.
#in binary we have 8 digits that are addrssable in a byte.
#split up a byte into 5 and 3.   00000 / 000
#the 3 on the right tell you how many digits on the left you need to pay attention to.
#The letter C written out in this method would be 01010100    01010 / 100
#0 = dash
#1 = dot
#the three digits on the right read out 4 so you read the 5 on the left starting left to right.  and read the first 4.
# -.-.   = C
#any trailing zero's past what you need to pay attention to can be safely ignored.
#i may go back later and use the 2 extra numbers i have in the right 3 bits to add extra stuff such as periods, commas, and such.
