from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    Viewer_rating = Column("Viewer_rating", Integer)
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
    Actor_ID = Column("Actor_ID", Integer, primary_key=True,  unique=True)
    Movie_ID = Column(Integer, ForeignKey("Movies.Movie_ID"))
    Actor_name = Column("Actor_Name", String)

    def __int__(self, Actor_ID, Movie_ID, Actor_name):
        self.Actor_ID = Actor_ID
        self.Movie_ID = Movie_ID
        self.Actor_name = Actor_name


    def __repr__(self):
        return f"({self.Actor_ID}) {self.Movie_ID} {self.Actor_name}"



class Director(Base):
    __tablename__ = "Directors"
    Director_ID = Column("Director_ID", Integer, primary_key=True, unique=True)
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
    Genre_ID = Column("Genre_ID", Integer, primary_key=True, unique=True)
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


session.commit()