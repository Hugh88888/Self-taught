import csv

answer = input("好きな色は？")
with open("000.txt", "w", encoding="utf-8") as f:
    f.write(answer)

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
