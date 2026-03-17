import random
import string
special_character=string.punctuation
pass_1=["gojo","sukuna","shirou","gilgamesh","ichigo","luffy"]
pass_2=["zoro","natsu","lelouch","naruto","isagi","saiki"]
amount=int(input("how many passwords do you want:"))
for i in range(amount):
    first_half=random.choice(pass_1)
    second_one=random.choice(special_character)
    middle_one=random.choice(special_character)
    next_one=random.choice(special_character)
    tail_end=random.choice(pass_2)
    num_end=random.randint(10,100)
    final_pass=f"{first_half}{second_one}{middle_one}{tail_end}{next_one}{num_end}"
    print(f"🛡️your secure password is:{final_pass}")
