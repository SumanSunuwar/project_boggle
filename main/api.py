import requests

link = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
f = requests.get(link)
print(f.text[0])