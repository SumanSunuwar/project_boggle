from django.http.response import HttpResponse
from django.shortcuts import render
from .boggle import * 
from .drawboard import generate_words, drawBoard, get_boogle, randomLetters

def main(request):
    #list of words from the file
    d = generate_words()

    # get boogle board
    boggle, root = get_boogle(d)

    print("starting to find")
    print(findWords(boggle, root))
    print("end")

    return render(
        request, 
        "main.html", 
        context={
            "data": d, 
            "boggle": boggle, 
            "result": findWords(boggle, root)})