import sys
import requests
import os
import Keys
from PIL import Image




import io
key1 = Keys.SECERT_KEY1
key2 = Keys.SECERT_KEY2
folder_path = 'D:/ThatDudeuknow/Home Movies/'



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


def get_age_rating(movie_id):
    url= f"https://age-ratings.com/api2/s/{movie_id}/de"
    response = requests.get(url)
    jsonresponse = response.json()
    res = jsonresponse
    print(res)
    DE = [0,6,12,16,18,100, "16+", 7, "18+", "R21", "10+",11, "NC16","M/6","10A","IIB","M/18", "18A"]
    IE = ["G", "12A", "15A"]
    AU =["G", "PG", "MA15+", "M", "R18+", "X18+"]
    NL =["AL", 6, 9, 12, 16]
    UK =["U", "PG", "12A", 12, 15, 18,"R18"]
    TWN = ["청소년 관람불가"]
    US = ["G","PG","PG-13-R","R","UR"]
    if res == DE[0]:return US[0]
    elif res == DE[1]:return US[1]
    elif res == DE[2]:return US[2]
    elif res == DE[3]:return US[3]
    elif res == DE[4]:return US[3]
    elif res == DE[5]:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates?api_key={key2}"
        response = requests.get(url)
        jsonresponse = response.json()
        res2 = jsonresponse['results'][0]['release_dates'][0]['certification']
        if res2 == "":return US[4]
        elif res2 == str(DE[1]):return US[1]
        elif res2 == str(DE[2]):return US[2]
        elif res2 == str(DE[3]):return US[3]
        elif res2 == str(DE[4]):return US[3]
        elif res2 == str(UK[0]):return US[0]
        elif res2 == str(UK[2]):return US[2]
        elif res2 == str(UK[4]):return US[2]
        elif res2 == str(UK[6]):return US[3]
        elif res2 == str(NL[0]):return US[0]
        elif res2 == str(NL[2]):return US[1]
        elif res2 == str(AU[2]):return US[2]
        elif res2 == str(AU[3]):return US[3]
        elif res2 == str(AU[4]):return US[3]
        elif res2 == str(AU[5]):return US[5]
        elif res2 == str(IE[1]):return US[2]
        elif res2 == str(IE[2]):return US[2]
        elif res2 == str(DE[6]):return US[3]
        elif res2 == str(DE[7]):return US[3]
        elif res2 == str(DE[8]):return US[3]
        elif res2 == str(DE[9]):return US[3]
        elif res2 == str(DE[9]):return US[2]
        elif res2 == str(DE[10]):return US[2]
        elif res2 == TWN[0]:return US[2]
        elif res2 == str(DE[11]):return US[3]
        elif res2 == str(DE[12]):return US[1]
        elif res2 == str(DE[13]):return US[2]
        elif res2 == str(DE[13]):return US[2]
        elif res2 == str(DE[14]):return US[3]
        elif res2 == str(DE[15]):return US[3]
        else:
            return res2
    else:
        return res

#:Mid90s  2018
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
def download_image(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name
    with open(file_path, "wb") as f:
        image.save(f,'JPEG')

def write_movie_overview():
    pass




if __name__ == '__main__':
    print(f'Total Movies in Home Movies Folder {len(my_movie_dictionary(folder_path))} \n')
    count = 1
    imdb_ids = []
    movie_genres = []
    # len(my_movie_dictionary(folder_path))
    for i in range(len(my_movie_dictionary(folder_path))):
        T = my_movie_dictionary(folder_path)[i][0]
        Y = my_movie_dictionary(folder_path)[i][1]
        print(f"{count}.", f"{T} {Y}")
        ID = get_imdb_movie_poster_and_id(T, Y)

        print(f"IMDB ID: {ID[0]['id']}")
        imdb_ids.append(ID[0]['id'])
        print(f"Movie Poster: {ID[0]['image']} \n")
        img_url = ID[0]['image']

        img_dir = T + "("+Y+")"
        path_4_posters = "D:/ThatDudeuknow/Home Movies/"+img_dir+"/"
        #download_image(f"{path_4_posters} ", img_url,f"{T}{Y} poster.jpg")

        print(f"Age rating: {get_age_rating(imdb_ids[i])}\n")

        genres = getmovieinfo(imdb_ids[i])[0]['genres']
        print("Genres:")
        for g in range(len(genres)): print(f"{genres[g]['name']}")
        print(f"\nOverview: {getmovieinfo(imdb_ids[i])[0]['overview']} \n")
        print(f"Runtime: {getmovieinfo(imdb_ids[i])[0]['runtime']} \n")
        print(f"Viewer rating: {getmovieinfo(imdb_ids[i])[0]['vote_average']} \n")

        print("Starring: ")
        print(getcredits(imdb_ids[i])[0]['cast'][0]['name'])
        print(getcredits(imdb_ids[i])[0]['cast'][1]['name'])
        print(getcredits(imdb_ids[i])[0]['cast'][2]['name'])


        directors = [credit for credit in getcredits(imdb_ids[i])[0]['crew'] if credit["job"] == "Director"]

        for people in range(len(directors)): print(f"\nDirector: {directors[people]['name']}")


        print("____________________________________________________________________________________________________\n")
        count += 1
