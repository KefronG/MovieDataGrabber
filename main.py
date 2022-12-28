import sys
import requests
import os
import Keys
import time
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

def getcredits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key2}&language=en-US"
    response = requests.get(url)
    jsonresponse = response.json()
    res = jsonresponse
    mylist = []
    mylist.append(res)
    return mylist



def getmovieinfo(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={key2}&language=en-US"
    response = requests.get(url)
    jsonresponse = response.json()
    res = jsonresponse
    mylist = []
    mylist.append(res)
    return mylist
#
def get_imdb_movie_poster_and_id(title, year):
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
#time.sleep(12) TMDB 40 request every 10 secs so count the number of request at for sleep for 12 sec





if __name__ == '__main__':
    print(f'Total Movies in Dir {len(my_movie_dictionary(folder_path))} \n')
    count = 0
    imdb_ids = []
    #len(my_movie_dictionary(folder_path)) - 1
    for i in range(2):
        T = my_movie_dictionary(folder_path)[i][0]
        Y = my_movie_dictionary(folder_path)[i][1]
        print(f"{count}. {T} {Y}")
        ID = get_imdb_movie_poster_and_id(T, Y)

        print(f"IMDB ID: {ID[0]['id']}")
        imdb_ids.append(ID[0]['id'])
        print(f"Movie Poster: {ID[0]['image']} \n")

        print(f"Movie genres: {getmovieinfo(imdb_ids[i])[0]['genres']} \n")
        print(f"Movie overview: {getmovieinfo(imdb_ids[i])[0]['overview']} \n")
        print(f"Movie runtime: {getmovieinfo(imdb_ids[i])[0]['runtime']} \n")
        print(f"Movie vote average: {getmovieinfo(imdb_ids[i])[0]['vote_average']} \n")

        print("Starring: ")
        print(getcredits(imdb_ids[i])[0]['cast'][0]['name'])
        print(getcredits(imdb_ids[i])[0]['cast'][1]['name'])
        print(getcredits(imdb_ids[i])[0]['cast'][2]['name'])

        print("____________________________________________________________________________________________________\n")





        count +=1


        #producer

        #director


