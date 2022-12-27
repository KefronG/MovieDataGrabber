import sys
import requests
import os

folder_path = r'D:/ThatDudeuknow/Home Movies'
key = ''


def imdb_connection(title, year):
    url = f"https://imdb-api.com/en/API/SearchMovie/{key}/{title} {year}"
    # {key},{title},{year}
    response = requests.get(url)
    if response.status_code != 200:
        print("fail")
        sys.exit(-1)
    jsonresponse = response.json()
    res = jsonresponse
    mylist = []
    mylist.append(res)



    return mylist


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


def getmovieinfo(id):
    url = f"https://imdb-api.com/en/API/Movies/{key}/{id}/Posters,Images,Ratings"
    response = requests.get(url)
    if response.status_code != 200:
        print("fail")
        sys.exit(-1)
    jsonresponse = response.json()
    res = jsonresponse
    print(jsonresponse)
    mylist = []
    mylist.append(res)
    return mylist


if __name__ == '__main__':
    print(len(my_movie_dictionary(folder_path)))
    count = 0
    for i in range(len(my_movie_dictionary(folder_path)) - 1):
        T = my_movie_dictionary(folder_path)[i][0]
        Y = my_movie_dictionary(folder_path)[i][1]
        print(T,Y)
        ID = imdb_connection(T, Y)
        print(ID)
        #print(f"IMDB ID: {ID[0]['id']}")
        #print(f"Movie Poster: {ID[0]['image']}")
        count +=1
        print(count)