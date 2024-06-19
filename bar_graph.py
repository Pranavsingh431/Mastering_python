#BAR GRAPH
movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
oscars = [5,11,3,8,10]

plt.bar(movies, oscars, color= 'red')
plt.title('movies vs number of oscars')
plt.xlabel('movies')
plt.ylabel('number of oscars')
plt.show()
