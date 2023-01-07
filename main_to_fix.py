import os
os.system("clear")

import requests
from bs4 import BeautifulSoup
import json, csv, time, random
from core.config import HEADERS, DOMEN, URL

#Вытащили главную страницу
#__________________________________________________________________________________________
# response = requests.get(url=URL, headers=HEADERS)
# soup = BeautifulSoup(response.text, 'lxml')

# with open('core/html/index.html', "w", encoding='UTF-8') as file:
#     file.write(str(soup))
# #__________________________________________________________________________________________



# Вытащили название из ссылки
# #__________________________________________________________________________________________
# with open('core/html/index.html', "r", encoding='UTF-8') as file:
#     src = file.read()


# soup = BeautifulSoup(src, 'lxml')
# anime = soup.find("div", id = "dle-content").find_all("article")

# all_anime_dict = { 

# }

# for item in anime:
#     name_anime = item.find("h2").text
#     url_anime = item.find("span",).find("a").get("href")
#     # print(name_anime)
#     # print(url_anime)
#     all_anime_dict[name_anime] = url_anime

# # with open('core/html/index.html', "w", encoding='UTF-8') as file:
# #     file.write(str(soup))

# with open(f"core/json/all_anime_dict.json", "w", encoding = "UTF-8") as file:
#     json.dump(all_anime_dict, file, indent = 4, ensure_ascii = False)  
#_____________________________________________________________________________________________



# Вытащили информацию об аниме
#______________________________________________________________________________________________
with open(f"core/json/all_anime_dict.json", "r") as file:
    all_anime = json.load(file)

iter_count = int(len(all_anime)) - 1
count = 0
for anime_name, anime_url in all_anime.items():
    rep = [",", " ", "-", "'", "/"]
    for item in anime_name:
        if item in rep:
            anime_name = anime_name.replace(item, "_")
    
    response = requests.get(url=anime_url, headers=HEADERS)
    src = response.text 

    with open(f"core/html/{count}_{anime_name}.html", "w", encoding="UTF-8") as file:
        file.write(src)
    
    with open(f"core/html/{count}_{anime_name}.html", "r", encoding="UTF-8") as file:
        src = file.read() 

    soup = BeautifulSoup(src, 'lxml')
    anime_block = soup.find(class_ = "infoContent")
    all_p = anime_block.find_all("p")
    
    
    episode_photo = DOMEN + anime_block.find("img").get("src")
    episode_name = anime_block.find("h3").text
    episode_release = all_p[0].text
    episode_genre = all_p[1].text
    episode_type = all_p[2].text
    episode_count = all_p[3].text
    episode_description = all_p[5].text


    # print(episode_photo)
    # print(episode_release)
    # print(episode_genre)
    # print(episode_type)
    # print(episode_count)
    # print(episode_description)


    all_informations_anime = {
        "photo": episode_photo,
        "name": episode_name,
        "release": episode_release,
        "genre": episode_genre,
        "type": episode_type,
        "count": episode_count,
        "description": episode_description
    }


    with open(f"core/json/{count}_info_anime.json", "a") as file:
        json.dump(all_informations_anime, file, indent = 4, ensure_ascii=False) 
        count += 1 

    print(f"Проход по {count}, и {anime_name} записан...")

    iter_count = iter_count - 1
    if iter_count == 0:
        print("Работа выполнена")
        os.system("clear")
        break
    
    print(f"Осталось итерации: {iter_count}")
    time.sleep(random.randrange(2,4))
    os.system("clear")

