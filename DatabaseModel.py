from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import DataGrabber
import KeysandPaths

#Outline Movie table has an ID, title, year of release, IMDB ID, poster directory, overview text file directory, may or
#may not have an age rating and viewer rating, but has a runtime, and actor IDs and director IDs and genre IDS
#actor names can be returned using ID as well as Directors and genre types. A movie must have actors and directors and
#at least 1 genre, actors may or may not have a movie ID which represant movie they where in, A director must have a
#movie ID to be a director and finally Genres may or may not have a movie ID.


Base = declarative_base()

class Movie(Base):
    __tablename__ = "Movies"

    Movie_ID = Column("Movie_ID", Integer, primary_key=True,  unique=True)
    Title = Column("Title", String)
    Year = Column("Release Year", Integer)
    IMDB_ID = Column("IMDB_ID", Integer)
    Poster_Dir = Column("Poster_Dir", String)
    Overview_Dir = Column("Overview_Dir", String)
    Subtitle_Dir = Column("Subtitle_Dir", String)
    Age_rating = Column("Age_rating", String)
    Viewer_rating = Column("Viewer_rating out of 10", Integer)
    Runtime = Column("Runtime", Integer)

    def __int__(self, Movie_ID, Title,  Year, IMDB_ID, Poster_Dir, Overview_Dir, Subtitle_Dir, Age_rating, Viewer_rating,
                Runtime):
        self.Movie_ID = Movie_ID
        self.Title = Title
        self.Year = Year
        self.IMDB_ID = IMDB_ID
        self.Poster_Dir = Poster_Dir
        self.Overview_Dir = Overview_Dir
        self.Subtitle_Dir = Subtitle_Dir
        self.Age_rating = Age_rating
        self.Viewer_rating = Viewer_rating
        self.Runtime = Runtime

    def __repr__(self):
        return f"({self.Movie_ID}) {self.Title} {self.Year} {self.IMDB_ID} {self.Poster_Dir} {self.Overview_Dir}" \
               f" {self.Subtitle_Dir} {self.Age_rating} {self.Viewer_rating} {self.Runtime}"



class Actor(Base):
    __tablename__ = "Actors"
    Actor_ID = Column("Actor_ID", Integer, primary_key=True)
    Movie_ID = Column(Integer, ForeignKey("Movies.Movie_ID"))
    Actor_name = Column("Actor_Name", String)
    popularity = Column("popularity score out of 100", Integer)

    def __int__(self, Actor_ID, Movie_ID, Actor_name, popularity):
        self.Actor_ID = Actor_ID
        self.Movie_ID = Movie_ID
        self.Actor_name = Actor_name
        self.popularity = popularity


    def __repr__(self):
        return f"({self.Actor_ID}) {self.Movie_ID} {self.Actor_name} {self.popularity}"



class Director(Base):
    __tablename__ = "Directors"
    Director_ID = Column("Director_ID", Integer, primary_key=True)
    Movie_ID = Column(Integer, ForeignKey("Movies.Movie_ID"))
    Director_name = Column("Director_name", String)

    def __int__(self, Director_ID, Movie_ID, Director_name):
        self.Director_ID = Director_ID
        self.Movie_ID =Movie_ID
        self.Director_name = Director_name

    def __repr__(self):
        return f"({self.Director_ID}) {self.Movie_ID} {self.Director_name}"


class Genre(Base):
    __tablename__ = "Genres"
    Genre_ID = Column("Genre_ID", Integer, primary_key=True)
    Movie_ID = Column(Integer, ForeignKey("Movies.Movie_ID"))
    Genre_name = Column("Genre_name", String)

    def __int__(self, Genre_ID, Movie_ID, Genre_name):
        self.Genre_ID = Genre_ID
        self.Movie_ID =Movie_ID
        self.Genre_name =Genre_name

    def __repr__(self, ):
        return f"({self.Genre_ID}) {self.Movie_ID} {self.Genre_name}"


class User(Base):
    __tablename__ = "Users"
    User_ID = Column("User_ID", Integer, primary_key=True, unique=True)
    User_Name = Column("User_Name", String)
    email = Column("Email", String,unique=True)
    password = Column("Password", String)

    def __int__(self, User_ID, User_Name, email, password):
        self.User_ID = User_ID
        self.User_Name = User_Name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"({self.User_ID}) {self.User_Name} {self.email} {self.password}"


engine = create_engine("sqlite:///Home_Movies.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

print(f'Total Movies in Home Movies Folder {len( DataGrabber.my_movie_dictionary(KeysandPaths.rtnfolder_path()))} \n')
count = 1
imdb_ids = []

# For each Movie In my home movies folder get:
# len(my_movie_dictionary(KeysandPaths.rtnfolder_path()))
for i in range(30):

    # Title and Year
    T = DataGrabber.my_movie_dictionary(KeysandPaths.rtnfolder_path())[i][0]
    Y =  DataGrabber.my_movie_dictionary(KeysandPaths.rtnfolder_path())[i][1]
    print(f"{count}.", f"{T} {Y}")
    ID =  DataGrabber.get_imdb_movie_poster_and_id(T, Y)

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
    age_rating_certification = [rating for rating in  DataGrabber.get_age_rating(imdb_ids[i]) if rating["iso_3166_1"] == "US"]
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
    genres =  DataGrabber.getmovieinfo(imdb_ids[i])[0]['genres']
    print("Genres:")
    for g in range(len(genres)):
        movie_genres.append(genres[g]['name'])
    for g in range(len(genres)):
        print(movie_genres[g])

    # Overview
    overview =  DataGrabber.getmovieinfo(imdb_ids[i])[0]['overview']
    print(f"\nOverview: {overview} \n")
    overview_dir = T + "(" + Y + ")"
    path_4_overview = KeysandPaths.rtnpath_4_overview(overview_dir)
    # write_movie_overview(f"{path_4_overview}",overview,f"{T}{Y} overview.txt" )

    path_4_subtitles = KeysandPaths.rtnpath_4_subtites(overview_dir)

    # Runtime
    runtime = DataGrabber.getmovieinfo(imdb_ids[i])[0]['runtime']
    print(f"Runtime: {runtime} \n")
    v_rating = int(DataGrabber.getmovieinfo(imdb_ids[i])[0]['vote_average'])
    # Viewer rating
    print(f"Viewer rating: {v_rating} \n")

    # starring cast
    print("Starring: ")
    crew = DataGrabber.get_credits(imdb_ids[i])[0]['cast']
    crew_scores = [c for c in crew if crew[len(crew) - 1]['popularity']]
    pop_score = []
    for c in range(len(crew_scores)):
        pop_score.append(crew_scores[c]['popularity'])
    pop_score.sort()
    mod_score = pop_score[len(pop_score) - 1] / 2
    cast = []
    for c in range(len(crew)):
        if int(crew[c]['popularity']) >= int(mod_score):
            cast.append(crew[c])
    for c in range(len(cast)):
        print(cast[c]['name'])

    # Directors
    Directors = []
    lst_directors = [credit for credit in  DataGrabber.get_credits(imdb_ids[i])[0]['crew'] if credit["job"] == "Director"]
    for people in range(len(lst_directors)):
        Directors.append(lst_directors[people]['name'])
    for name in range(len(lst_directors)):
        print(f"\nDirector: {Directors[name]}")

    print("____________________________________________________________________________________________________\n")

    movie = Movie(Title=T, Year=Y, IMDB_ID=imdb_ids[0], Poster_Dir=path_4_posters, Overview_Dir=path_4_overview,
                  Subtitle_Dir=path_4_subtitles, Age_rating=rating[0], Viewer_rating=v_rating, Runtime=runtime)
    session.add(movie)
    session.commit()

    for c in range(len(cast)):
        actor = Actor(Movie_ID=movie.Movie_ID, Actor_name=cast[c]['name'], popularity=int(crew[c]['popularity']))
        session.add(actor)


    for d in range(len(Directors)):
        director = Director(Movie_ID=movie.Movie_ID, Director_name=Directors[d])
        session.add(director)


    for g in range(len(movie_genres)):
        genre = Genre(Movie_ID=movie.Movie_ID, Genre_name=movie_genres[g])
        session.add(genre)




    count += 1
user = User(User_Name="My_name", email="MyEmail@gmail.com", password="password123")
session.add(user)
session.commit()