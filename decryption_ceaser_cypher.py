import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
       
        return self.message_text
        

    def get_valid_words(self):
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        
        n = shift
        dic = {}
        a2z = string.ascii_lowercase
        A2Z = string.ascii_uppercase
        for i in range(len(a2z)):
            if (i + n)< len(a2z):
                dic[a2z[i]] = a2z[i+n]
            else:
                d = i + n - len(a2z)
                dic[a2z[i]] = a2z[d]
        for i in range (len(A2Z)):
            if i+n < len(A2Z):
                dic[A2Z[i]] = A2Z[i+n]
            else:
                d = i+n - len(A2Z)
                dic[A2Z[i]] = A2Z[d]
        return  dic
    

    def apply_shift(self, shift):

        s = self.get_message_text()
        ss = ''
        n = shift
        for i in range(len(s)):
            if s[i] in self.build_shift_dict(n):
                ss =ss + self.build_shift_dict(n)[s[i]]
            else:
                ss= ss + s[i]
        return ss




class PlaintextMessage(Message):
    def __init__(self, text, shift):
        
        Message.__init__(self,text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted


    def change_shift(self, shift):
        
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self,text)
        


    def decrypt_message(self):
        length = 0
        poss_shift = 0
        for i in range(26):
            a = (self.apply_shift(i).split(' '))                #In this line takes the message in self and shifts it by i letters, and then makes a list of 
                                                                    #those wordsby split(''), so a is a list.
            l = [x for x in a if is_word(self.valid_words,x)]
            #print(len(l))
            if len(l)> length:
                length = len(l)
                poss_shift = i
        return (poss_shift,self.apply_shift(poss_shift))
            



bb = Message('silence is the language of god, all else is poor translation')
print(bb.apply_shift(12))
cc = CiphertextMessage('aqtmvkm qa bpm tivociom wn owl, itt mtam qa xwwz bzivatibqwv')
print(cc.decrypt_message())
#print(cc.get_valid_words())

if __name__ == '__main__':

   #Example test case (PlaintextMessage)
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   #Example test case (CiphertextMessage)
   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())

