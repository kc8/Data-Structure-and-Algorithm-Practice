import random

def rand_string(length):
    alphabet = "abcdefghijklmnopqrstvxyz "
    phrase = ""
    count = 0
    while count < length:
        phrase += (alphabet[random.randrange(0, 25, 1)])
        count += 1 
    return phrase


def generate_score(phrase, actual_value, phrase_length):
    return_dict = {'score':0}
    char_correct = 0
    char_placement = 0
    #phrase = "methinks it is a like a weasel" #for checking
    if phrase == actual_value:
        return_dict['found'] = True
    else:   
        return_dict['found'] = False
    for i in phrase:
        if (i == actual_value[char_placement]) and (char_placement <= phrase_length):
            char_correct += 1 
            return_dict.update({'score':(char_correct/phrase_length*100)})
        char_placement += 1
    return return_dict
                

def main():
    check_phrase = {'found':False}
    actual_phrase = "methinks it is a like a weasel"
    phrase_length = len(actual_phrase)
    current_count = 0 
    while check_phrase['found'] == False:
        phrase = rand_string(phrase_length)
        check_phrase = generate_score(phrase, actual_phrase, phrase_length)
        current_count += 1
        if current_count == 1000:
            print(check_phrase['score'])
            current_count = 0
        if check_phrase['found'] == True:
            print("FOUND THE STRING! Your score is: %d", check_phrase['score'])
            
main()