import json

with open('data.json') as f:
	movieObjects = json.load(f)

#creates an empty dictionary to store key value pairs of stars and their ratings
myData = dict()

#iterates through every object in the json file and obtains the naems of stars and their movie ratings
for obj in movieObjects:
	for star in obj['stars'].split(", "):
		#Checks for any duplicates, if found we append movie rating to existing entry, else we create a new entry with the corresponding movie ratings
		if star in myData:
			myData[str(star)].append(obj['rating'])
		else:
			myData[str(star)] = [obj['rating']]

#myData dictionary contains list of all unique actors with their corresponding movie ratings
#for key, value in myData.items():
	#print(key, ' : ', value)

#Filter only actors with 2 or more movies
sortedData = dict()
for key, value in myData.items():
	if(len(value) >= 2):
		sortedData[key] = value

#sorts dictionary in ascending order by number of movies for each actor
for key, value in sorted(sortedData.items(), key= lambda x:len(x[1])):
	#Calculates average rating and prints entry to the console
	numMovies = len(value)
	avgRating = (sum(list(map(float, value))))/numMovies
	print(key, ' | ', 'Movies: ', numMovies, ' | ', 'AVG Rating: ', avgRating)

