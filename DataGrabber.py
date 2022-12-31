import sys
import requests
import os
import KeysandPaths
from PIL import Image
import io


def my_movie_dictionary(mydir):
    titles_and_years = []
    titles_and_year_of_release = []
    cntr = 0
    for files in os.listdir(mydir):
        cntr += 1
        titles_and_years.append(files)
        temp_split = titles_and_years[cntr - 1].split(')')[0]
        jst_title_and_year = temp_split.split('(')
        titles_and_year_of_release.append(jst_title_and_year)
    return titles_and_year_of_release


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


def get_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={KeysandPaths.SECERT_KEY2}&language=en-US"
    response = requests.get(url)
    json_response = response.json()
    res = json_response
    mylist = [res]
    return mylist


def getmovieinfo(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={KeysandPaths.SECERT_KEY2}&language=en-US"
    response = requests.get(url)
    json_response = response.json()
    res = json_response
    mylist = [res]
    return mylist


#
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


if __name__ == '__main__':
    print(f'Total Movies in Home Movies Folder {len(my_movie_dictionary(KeysandPaths.rtnfolder_path()))} \n')
    count = 1
    imdb_ids = []

    # len(my_movie_dictionary(KeysandPaths.rtnfolder_path()))
    # For each Movie In my home movies folder get:
    for i in range(10):

        # Title and Year
        T = my_movie_dictionary(KeysandPaths.rtnfolder_path())[i][0]
        Y = my_movie_dictionary(KeysandPaths.rtnfolder_path())[i][1]
        print(f"{count}.", f"{T} {Y}")
        ID = get_imdb_movie_poster_and_id(T, Y)

        # IMDB ID
        print(f"IMDB ID: {ID[0]['id']}")
        imdb_ids.append(ID[0]['id'])

        # Posters
        print(f"Movie Poster: {ID[0]['image']} \n")
        img_url = ID[0]['image']
        img_dir = T + "(" + Y + ")"
        path_4_posters = KeysandPaths.rtnpath_4_posters(img_dir)
        # download_image(f"{path_4_posters} ", img_url,f"{T}{Y} poster.jpg")

        # Age rating
        age_rating_certification = [rating for rating in get_age_rating(imdb_ids[i]) if rating["iso_3166_1"] == "US"]
        rating = []
        if not age_rating_certification:
            rating.append('NR')
        else:
            age_rating = [rating for rating in age_rating_certification[0]['release_dates'] if rating['certification']]
            for r in range(len(age_rating)):
                rating.append(age_rating[r]['certification'])
            if not age_rating:
                rating.append('NR')
        print(f"Age rating: {rating[0]}\n")

        # Genres
        movie_genres = []
        genres = getmovieinfo(imdb_ids[i])[0]['genres']
        print("Genres:")
        for g in range(len(genres)):
            movie_genres.append(genres[g]['name'])
        for g in range(len(genres)):
            print(movie_genres[g])

        # Overview
        overview = getmovieinfo(imdb_ids[i])[0]['overview']
        print(f"\nOverview: {overview} \n")
        overview_dir = T + "(" + Y + ")"
        path_4_overview = KeysandPaths.rtnpath_4_overview(overview_dir)
        # write_movie_overview(f"{path_4_overview}",overview,f"{T}{Y} overview.txt" )

        # Runtime
        print(f"Runtime: {getmovieinfo(imdb_ids[i])[0]['runtime']} \n")

        # Viewer rating
        print(f"Viewer rating: {getmovieinfo(imdb_ids[i])[0]['vote_average']} \n")

        # starring cast
        print("Starring: ")
        crew = get_credits(imdb_ids[i])[0]['cast']
        crew_scores = [c for c in crew if crew[len(crew) - 1]['popularity']]
        pop_score = []
        for c in range(len(crew_scores)):
            pop_score.append(crew_scores[c]['popularity'])
        pop_score.sort()
        ajst_score = pop_score[len(pop_score) - 1] / 2
        cast = []
        for c in range(len(crew)):
            if int(crew[c]['popularity']) >= int(ajst_score):
                cast.append(crew[c])
        for c in range(len(cast)):
            print(cast[c]['name'])

        # Directors
        Directors = []
        lst_directors = [credit for credit in get_credits(imdb_ids[i])[0]['crew'] if credit["job"] == "Director"]
        for people in range(len(lst_directors)):
            Directors.append(lst_directors[people]['name'])
        for name in range(len(lst_directors)):
            print(f"\nDirector: {Directors[name]}")

        print("____________________________________________________________________________________________________\n")
        count += 1
