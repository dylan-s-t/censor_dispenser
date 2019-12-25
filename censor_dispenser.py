# coding=utf-8

# completed on codecademy.com by dylan trerise on 22-dec-2019


# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open('email_one.txt', "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


# function to censor all instances of the phrase learning algorithms from the first email, email_one
# returns text
def censor_one(body_of_text):
  body_of_text_censored = body_of_text.replace('learning algorithms','*****')
  return body_of_text_censored

print(censor_one(email_one))

# censor all propietary terms from a list of terms in a body of text
# proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

"""
def censor_two(body_of_text, proprietary_terms):
  body_of_text_split = body_of_text.split()
  for i in range(len(body_of_text_split)):
    word = body_of_text_split[i]
    word = word.lower()
    if word[-1].isalpha() == True:
      if word in proprietary_terms:
        body_of_text_split[i] = '######'
    else:
      word_end = word[-1]
      word_start = word[:-1]
      if word_start in proprietary_terms:
        body_of_text_split[i] = '******' + word_end
  body_joined = ' '.join(body_of_text_split)
  for term in proprietary_terms:
    body_joined.replace(term, 'XXXX')
  return body_joined
"""

def censor_two(body_of_text, proprietary_terms): 
  split_lines = body_of_text.split('\n')
  split_words = []
  for line in split_lines:
    split_words.append(line.split())
    
  for line in split_words:
    for i in range(len(line)):
      word = line[i]
      word = word.lower()
      if word.isalpha() == True and word in proprietary_terms:
        line[i] = '####'
      else:
        word_end = word[-1]
        word_start = word[:-1]
        if word_start in proprietary_terms:
          line[i] = '******' + word_end
  join_words = []
  for line in split_words:
    join_words.append(' '.join(line))
  join_lines = "\n".join(join_words)
    
  return join_lines
        
      

print(censor_two(email_two, proprietary_terms))