# function to define string
interrogatives = ("how", "what", "why")
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#use a loop and make it conditional to end with \end
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
       results.append(sentence_maker(user_input))

#print(results)
print(" ".join(results))