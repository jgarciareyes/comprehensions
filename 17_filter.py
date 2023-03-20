numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x%2==0, numbers))
print (new_numbers)
print (numbers)

def filter_by_length(words):
   new_words= list(filter(lambda word: len(word)>3, words))
   return new_words

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)