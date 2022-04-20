import random

wordlist = ["apple" ,"mangoe","banana"]
chosen_word = random.choice(wordlist).lower()
empty_list = []
for i in range(0,len(chosen_word)):
    empty_list+="_"
      
print(empty_list)





life = int(input("lives for life "))

l = 0
while l<life:
    user_input = input("guess later ").lower()
    if user_input in chosen_word:
        for a in range(0,len(chosen_word)):
            if(chosen_word[a] == user_input):
                empty_list[a] = user_input
                
    else:
        l+=1  

    print(empty_list)      
    if "_" not in empty_list:
        print("game is over")
        break

if l == life:
    print("game is over")


    
               
        


        



