from django.shortcuts import render
from pydictionary import Dictionary


# Create your views here.


def home(request):
    if request.method == 'POST':
        word = request.POST['word']
        dict = Dictionary(word)

        data = {
            "meanings_list":  dict.meanings(),
            "synonyms_list":  dict.synonyms(),
            "antonyms_list": dict.antonyms(),
        }
        print(data)
    else:
        data = {}
    return render(request, 'result.html', data)
