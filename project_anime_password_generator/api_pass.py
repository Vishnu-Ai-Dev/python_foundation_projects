import random
import string
import requests

print("           📡connecting to the main data base       ")

url = "https://api.jikan.moe/v4/top/characters"
response = requests.get(url)
anime_data = response.json()
master_list=[]
for character in anime_data["data"]:
    clean_name = character["name"].split(",")[0].strip()
    master_list.append(clean_name)

special_character=string.punctuation
amount=int(input("how many passwords do you want:"))
for i in range(amount):
    first_half=random.choice(master_list)
    second_one=random.choice(special_character)
    middle_one=random.choice(special_character)
    next_one=random.choice(special_character)
    tail_end=random.choice(master_list)
    num_end=random.randint(10,100)
    final_pass=f"{first_half}{second_one}{middle_one}{tail_end}{next_one}{num_end}"
    print(f"🛡️your secure password is:{final_pass}")
