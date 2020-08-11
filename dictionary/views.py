from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
import requests


@api_view(['GET'])
def define(request):
    """Returns word's definitions and its examples of usage
     from dictionary.com"""
    params = list(request.query_params.values())
    if len(params) == 0:
        return Response({'msg': 'No word detected in parameters'}, status=400)

    word = params[0]
    if len(word.split()) > 1:
        return Response({'msg': 'Word must be only a single element'}, status=400)

    try:
        html = _get_html(f"https://www.dictionary.com/browse/{word}")

        meanings = html.findAll(attrs={"class": "css-1o58fj8"})
        definitions = []
        for mean in meanings:
            for x in mean:
                definitions.append(x.get_text())

        exs = html.findAll(attrs={"class": "one-click-content css-a8m74p e15kc6du6"})
        examples = []
        for x in exs:
            examples.append(x.get_text())

    except Exception as e:
        print("Error: The Following Error occurred: %s" % e)
    return Response({"definitions": definitions, "examples": examples}, status=200)


def _get_html(url, parser="html.parser"):
    """Returns html content of the page by url"""
    return BeautifulSoup(requests.get(url).text, parser)
