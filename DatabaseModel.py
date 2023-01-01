
#Outline Movie table has an ID, title, year of release, IMDB ID, poster directory, overview text file directory, may or
#may not have an age rating and viewer rating, but has a runtime, and actor IDs and director IDs and genre IDS
#actor names can be returned using ID as well as Directors and genre types. A movie must have actors and directors and
#at least 1 genre, actors may or may not have a movie ID which represant movie they where in, A director must have a
#movie ID to be a director and finally Genres may or may not have a movie ID.

#Movie class:
    #__init__
     #Movie_ID(int,PK,non null, unique, auto inrc)
     #Title(str,non null)
     #Year(int,non null)
     #IMDB ID(int,non null)
     #Poster/Dir(str)
     #Overview Dir(str)
     #Age rating(str,non null)
     #Viewer rating(int)
     #Runtime(int,non null)
     #actor_ID(int,FK,non null,unique,auto inrc, ref=Actor.actor_ID)
     #director_ID(int,FK,non null,unique,auto inrc, ref=Director.director_ID)
     #genre_ID(int,FK,non null,unique,auto inrc, ref=Genre.genre_ID)


#Actor class:
    #__init__
     #actor_ID(int,PK,non null, unique, auto inrc)
     #Movie_ID(int,FK,unique,auto inrc, ref=Movie.Movie_ID)
     #actor name(str, non null)



#Director class:
    #__init__
     #director_ID(int,PK,non null, unique, auto inrc)
     #Movie_ID(int,FK,non null,unique,auto inrc, ref=Movie.Movie_ID)
     #director name(str, non null)


#Genre class:
    #__init__
     #genre_ID(int,PK,non null, unique, auto inrc)
     #Movie_ID(int,FK,non null,unique,auto inrc, ref=Movie.Movie_ID)
     #genre name(str,non null, unique)


