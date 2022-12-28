import sys
import requests
import os
import Keys
key1 = Keys.SECERT_KEY1
key2 = Keys.SECERT_KEY2

folder_path = r'D:/ThatDudeuknow/Home Movies'


def my_movie_dictionary(mydir):
    titles_and_years = []
    titles_and_year_of_release = []
    cntr = 0
    for files in os.listdir(mydir):
        cntr += 1
        titles_and_years.append(files)
        tempSplit = titles_and_years[cntr - 1].split(')')[0]
        jst_title_and_year = tempSplit.split('(')
        titles_and_year_of_release.append(jst_title_and_year)
    return titles_and_year_of_release


def getmovieinfo(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={key2}&language=en-US"
    response = requests.get(url)
    jsonresponse = response.json()
    res = jsonresponse
    print(jsonresponse)
    mylist = []
    mylist.append(res)
    return mylist
#
def get_imdb_movie_poster(title, year):
    url = f"https://imdb-api.com/en/API/SearchMovie/{key1}/{title} {year}"
    response = requests.get(url)
    if response.status_code != 200:
        print("fail")
        sys.exit(-1)
    jsonresponse = response.json()
    res = jsonresponse['results'][0]
    mylist = []
    mylist.append(res)
    return mylist


if __name__ == '__main__':
    print(f'Total Movies in Dir {len(my_movie_dictionary(folder_path))}')
    count = 0
    imdb_ids = []
    len(my_movie_dictionary(folder_path)) - 1
    for i in range(len(my_movie_dictionary(folder_path)) - 1):
        T = my_movie_dictionary(folder_path)[i][0]
        Y = my_movie_dictionary(folder_path)[i][1]
        print(f"{count}. {T} {Y}")
        ID = get_imdb_movie_poster(T, Y)
        #print(ID)
        print(f"IMDB ID: {ID[0]['id']}")
        imdb_ids.append(ID[0]['id'])
        print(f"Movie Poster: {ID[0]['image']} \n")
        count +=1

    getmovieinfo(imdb_ids[0])