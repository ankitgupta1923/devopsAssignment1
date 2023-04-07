def reverseWordSentence(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
 
    return newSentence
    
Sentence = input("Enter your string: ")
if not Sentence:
    print ("No input provided")
else:    
    print(reverseWordSentence(Sentence))