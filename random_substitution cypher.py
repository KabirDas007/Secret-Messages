
import string
from ps4a import get_permutations
import random

### HELPER CODE ###
def load_words(file_name):
    
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        
        dic = {}
        for i in range(len(VOWELS_LOWER)):
            dic[VOWELS_LOWER[i]] = vowels_permutation[i]
            dic[VOWELS_UPPER[i]] = vowels_permutation.upper()[i]
        for i in range(len(CONSONANTS_LOWER)):
            dic[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            dic[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
        return dic

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        enc_msg = ''                                        #enc_mesg = encripted_message
        #transpose_dict= self.build_transpose_dict('eiauo')
        
        for i in range(len(self.message_text)):
            if self.message_text[i] in transpose_dict:
                enc_msg = enc_msg + transpose_dict[self.message_text[i]]
            else:
                enc_msg += self.message_text[i]
        return enc_msg
    

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self,text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        Returns: the best decrypted message    
        
        '''
        perm_list = []
        perm_list.extend(get_permutations('aeiou'))
        length = 0
    
        max_count = 0
        good_perm = ''
        

        for item in perm_list:
            curr_dic = self.build_transpose_dict(item)
            poss_decrypt = self.apply_transpose(curr_dic)
            list_poss_dec = poss_decrypt.split(' ')
            count = 0
    
            for e in list_poss_dec:
                if is_word(self.valid_words,e):
                    count += 1
                    if max_count <count:
                        max_count = count
                        good_perm = item
            #print(list_poss_dec,count, max_count,item,good_perm)
        curr_dic = self.build_transpose_dict(good_perm)
        return self.apply_transpose(curr_dic)
    
            #Alternatively the code below also works:
        #     l = [x for x in list_poss_dec if is_word(self.valid_words,x)]
        #     if len(l) >length:
        #             length = len(l)
        #             good_decrpt = poss_decrypt
        # return good_decrpt

a = SubMessage('Wound is the palce where light enters you.')
print(a.apply_transpose(a.build_transpose_dict('eiauo')))
encr_a = EncryptedSubMessage('Wuond as thi pelci whiri laght intirs yuo.')
print(encr_a.decrypt_message())

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    