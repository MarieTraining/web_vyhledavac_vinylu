import os

directory = os.path.dirname(__file__) #oprava relativni cesty
file_path = os.path.join(directory,"datas","gramodesky.csv")
print(file_path)