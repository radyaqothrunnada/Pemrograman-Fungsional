from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spyder-Man: No Way Home", "year": 2021, "rating": 7.0, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time To Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power Of The Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]
#Pilihan 1
def count_movies_by_genre(movies):
    genres = list(map(lambda film: film['genre'], movies))
    unique_genres = list(set(genres))

    genre_count = {genre: len(list(filter(lambda x: x == genre, genres))) for genre in unique_genres}

    print("\nJumlah Film Berdasarkan Genre:")
    for genre, count in genre_count.items():
        print(f"- {genre.ljust(10)} : {count}")

#Pilihan 2
def average_rating_by_year(movies):
    ratings_by_year = {}
    counts_by_year = {}

    for film in movies:
        year = film['year']
        if year in ratings_by_year:
            ratings_by_year[year] += film['rating']
            counts_by_year[year] += 1
        else:
            ratings_by_year[year] = film['rating']
            counts_by_year[year] = 1

    average_ratings_by_year = {
        year: ratings_by_year[year] / counts_by_year[year] for year in ratings_by_year
    }

    result = reduce(lambda acc, year: acc + f"- {year} : {average_ratings_by_year[year]}\n", average_ratings_by_year, "")
    print("Rata-rata Rating Film Berdasarkan Tahun Rilis :")
    print(result)

#Pilihan 3
def movie_with_highest_rating():
    film_rating_tertinggi = max(movies, key=lambda x: x['rating'])

    print("\nFilm Dengan Rating Tertinggi :")
    print(f"Judul Film  : {film_rating_tertinggi['title']}")
    print(f"Rating      : {film_rating_tertinggi['rating']}")
    print(f"Tahun Rilis : {film_rating_tertinggi['year']}")
    print(f"Genre       : {film_rating_tertinggi['genre']}")

#Pilihan 4
def display_movie_data(movies):
    search = input("Masukkan judul film yang ingin dicari: ")
    movie_found = next((film for film in movies if film['title'] == search), None)

    # Jika film ditemukan, tampilkan informasinya
    if movie_found:
        print(f"\nJudul Film : {movie_found['title']}")
        print(f"Rating       : {movie_found['rating']}")
        print(f"Tahun Rilis  : {movie_found['year']}")
        print(f"Genre        : {movie_found['genre']}")
    else:
        print("\nFilm dengan judul tersebut tidak ditemukan.")


while True:
    print("\nPilih ugas yang ingin dilakukan : ")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Keluar")
    opsi = input("Masukkan Pilihan (1/2/3/4/5) : ")

    if opsi == '1' :
        count_movies_by_genre(movies)
    elif opsi == '2' :
        average_rating_by_year(movies)
    elif opsi == '3' :
        movie_with_highest_rating()
    elif opsi == '4' :
        display_movie_data(movies)
    elif opsi == '5' :
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang sesuai.")