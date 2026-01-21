from rest_framework import serializers
from cinema.models import Movie, MovieSession, CinemaHall, Genre, Actor

class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "image")

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "image", "genres", "actors")
        read_only_fields = ("image",) # Image is read-only here so it's not available on POST

class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )

class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )
    # Add movie_image here pointing to the nested movie's image
    movie_image = serializers.ImageField(source="movie.image", read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "movie_image",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
