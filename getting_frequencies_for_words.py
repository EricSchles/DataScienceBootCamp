#A simple approach to creating features in text

class frequency:
    def __init__(self,text):
        self.text = text.split(" ")
        self.freqs = self.__freq()
        self.rel_freqs = self.__prob_word()
        
    def __freq(self):
        frequencies = {}
        for word in self.text:
            if word == " ":
                continue
            if word == '':
                continue
            if not word in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        return frequencies
    
    def __prob_word(self):
        sum_freq = 0
        rel_freq = {}
        for word in self.freqs.keys():
            sum_freq += self.freqs[word]
        for word in self.freqs.keys():
            rel_freq[word] = self.freqs[word]/float(sum_freq)
        return rel_freq
    
    def result(self):
        return self.rel_freqs
    
f = frequency("This is some text, it's not very exciting, but I'll take it.  And I'll share it with the world.  We can do so much with this text.")
print f.result()

#or do this:

#import collections, re
#texts = ['John likes to watch movies. Mary likes too.',
#   'John also likes to watch football games.']
#bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
#            for txt in texts]
#print bagsofwords[0]
#print bagsofwords[1]
#sumbags = sum(bagsofwords, collections.Counter())
#total_words = sum([len(elem) for elem in texts]) 
#print total_words
#relbags =  {elem:sumbags[elem]/float(total_words) for elem in sumbags.keys()}
#print relbags
 
