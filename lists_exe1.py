songs = ["My Heart", "Her Brain", "The Light", "A Shadow", "One Dance", "Two Monkeys", "Happy Jumping"]
playlist = songs[0:5:2]
playlist[2] += " - Together"
playlist.pop(1)
print(playlist)