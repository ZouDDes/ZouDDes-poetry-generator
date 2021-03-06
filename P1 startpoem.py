# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:37:34 2018

script color and feeling poem
@author: junjiang
liense 
"""
import markovify 

import random

random.seed ( )

# line break
print ""


# list of words
minds = ["Plato", "Newton", "Da Vinci", "Goethe", "Einstein"]
nouns = ["sky", "grass", "rose"]
names = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "earth", ]
feelings = ["chaos", "powerful", "gentle", "soft", "radiant", "splendid", "mystery",]

second_nouns = ["eyes", "toast", "ocean", "lenses", "sights", "nights"]
verbs = ["are", "like", "are", "depict"]
adjectives = ["curved", "dark", "deep", "rigid"]
adverbs = ["and"]

#select random words from lists
mind = random.choice(minds)
name = random.choice(names)
feeling = random.choice(feelings)
noun = random.choice(nouns)
second_noun = random.choice(second_nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

#print a sentence with random words from the lists
print "{mind} {name} {feeling} {noun} {adverb} {second_noun} {verb} {adjective}.".format(mind=mind, name=name, feeling= feeling, noun=noun,adverb=adverb,
    second_noun=second_noun, verb=verb, adjective=adjective)

singletext_model = markovify.Text(minds)

mylist = []
for i in range(0,5):
    mylist.append(singletext_model.make_short_sentence(140))
    
with open("poem.md", "w") as w:
    for item in mylist:
        w.write(item)
        w.write("\n")
        
##select random words from lists
#
#noun = random.choice(nouns)
#second_noun = random.choice(second_nouns)
#verb = random.choice(verbs)
#adjective = random.choice(adjectives)
#adverb = random.choice(adverbs)
#
##print a sentence with random words from the lists
#print "{noun} {adverb} {second_noun} {verb} {adjective}.".format(noun=noun,adverb=adverb,
#       second_noun=second_noun, verb=verb, adjective=adjective)
#
##line break
#print ""
#
##shuffle the list of adjectves
#random.shuffle(adjectives)

##print the shuffled list of adjectives with increasing whitespace
#i = 0
#print "The"
#for adjectives in adjectives:
#    i = i + 2
#    whitespace = " " * i
#    print whitespace + adjective
#    
## print the rest of the sentence
#    print "{noun} {verb}.".format(noun=noun, verb=verb)
               





