import sys
import requests
import os
import KeysandPaths
from PIL import Image
import io


def my_movie_dictionary(my_dir):
    titles_and_years = []
    titles_and_year_of_release = []
    cntr = 0
    for files in os.listdir(my_dir):
        cntr += 1
        titles_and_years.append(files)
        temp_split = titles_and_years[cntr - 1].split(')')[0]
        jst_title_and_year = temp_split.split('(')
        titles_and_year_of_release.append(jst_title_and_year)
    return titles_and_year_of_release


def get_imdb_movie_poster_and_id(title, year):
    url = f"https://imdb-api.com/en/API/SearchMovie/{KeysandPaths.SECERT_KEY1}/{title} {year}"
    response = requests.get(url)
    if response.status_code != 200:
        print("fail")
        sys.exit(-1)
    json_response = response.json()
    res = json_response['results'][0]

    mylist = [res]
    return mylist

def getmovieinfo(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={KeysandPaths.SECERT_KEY2}&language=en-US"
    response = requests.get(url)
    json_response = response.json()
    res = json_response


    mylist = [res]
    return mylist

def get_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={KeysandPaths.SECERT_KEY2}&language=en-US"
    response = requests.get(url)
    json_response = response.json()
    res = json_response
    mylist = [res]

    return mylist



def get_age_rating(movie_id):
    url = f"https://api.themoviedb.org/3/find/{movie_id}?api_key={KeysandPaths.SECERT_KEY2}&external_source=imdb_id"
    response = requests.get(url)
    json_response = response.json()
    res2 = json_response['movie_results'][0]['id']
    url2 = f"https://api.themoviedb.org/3/movie/{res2}/release_dates?api_key={KeysandPaths.SECERT_KEY2}"
    response2 = requests.get(url2)
    json_response2 = response2.json()
    res3 = json_response2['results']

    return res3



def download_image(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name
    with open(file_path, "wb") as f:
        image.save(f, 'JPEG')


def write_movie_overview(download_path, m_overview, file_name):
    file_path = download_path + file_name
    with open(file_path, "w") as f:
        f.write(m_overview)



