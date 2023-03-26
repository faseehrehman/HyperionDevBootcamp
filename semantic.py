
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("dog")
word2 = nlp("horse")
word3 = nlp("apple")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('dog apple horse berries ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#What I found interesting is the output prints out integers. The most interesting thing is that whether it is Cat Monkey or Monkey Cat the number that is printed is the same. 
#In my own example I had found the same as above. Whether id was dog apple or apple dog. the number printed out was exactly the same

#the first thing I notice when I ran the example file in MD and SM is that SM is not able to run word vectors.Another major difference is the values of the outputs are completely different. 