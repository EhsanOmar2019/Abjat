# Default number set in dectionary
default_alph_value = {"ا": 1, "ش": 300, "ب": 2, "ت": 400,
                      "ج": 3, "ث": 500,"د": 4, "خ": 500,
                      "ه": 5, "ذ": 700, "و": 6, "ض": 800,
                      "ز": 7, "ظ": 900, "ح": 8, "غ": 1000,
                      "ط": 9, "ی": 10, "ک": 20, "ل": 30,
                      "م": 40, "ن": 50, "س": 60, "ع": 70,
                      "ف": 80, "ص": 90 ,"ق": 100,  "ر": 200}

# in arabic there is no such alphabet  we called bad char
bad_characters = {'پ', 'ژ', 'گ', 'چ'}

# get input String from user
name = input("please Enter your String without : (ژ پ چ گ)  :  ")

# loop and check that the entered String  these not have the bad char
while bad_characters.intersection(name):
       name = input("please Enter your name without : (ژ پ چ گ)  :  ")
# total of alpha value
abj = 0
# sum all char number value in total variable
for alpha in name:
    abj += default_alph_value[alpha]

# print last result
print(abj)
