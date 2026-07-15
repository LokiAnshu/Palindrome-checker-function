def check(input_str):
   # converting the original string into lowercase
    text = input_str.lower()
    
    # converting the string into a string with only the alphabets
    raw_text = ""                           
    for letter in text:
        if letter.isalpha() == True:
            raw_text += letter
    
    # reversing the raw text
    reversed_raw_text = ""
    for ch in raw_text:
        reversed_raw_text = ch + reversed_raw_text
    
    # checking for palindrome
    if raw_text == reversed_raw_text: 
        return("This is a palindrome")
    else:
        return("This is not a palindrome")