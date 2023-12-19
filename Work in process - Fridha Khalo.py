# Creates a list with titles and dates for each painting.
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait with Monkeys"]
dates = [1939, 1933, 1946, 1940]
paintings = list(zip(paintings, dates))
print(paintings)

# Adds extra items to the list
last_minute_additions = [["The Broken Column", 1944], ["The Wounded Deer", 1946], ["Me and My Doll", 1937]]
paintings += last_minute_additions
print(paintings)

# Prints the lenght of the list and creates a range based on it
print(len(paintings))
audio_tour_number = range(1, len(paintings))
print(audio_tour_number)

# Prints the master list with titles, dates and audio tour number
master_list = list(zip(paintings, audio_tour_number))
print(master_list)