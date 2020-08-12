from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
import requests


@api_view(['GET'])
def define(request, word):
    """Returns word's definitions and its examples of usage
     from dictionary.com"""
    if len(word.split()) > 1:
        return Response({'msg': 'Word must be only a single element'}, status=400)

    html = _get_html(f"https://www.dictionary.com/browse/{word}")

    definitions = _get_definitions(html)

    examples = _get_examples(html)

    return Response({"definitions": definitions, "examples": examples}, status=200)


def _get_html(url, parser="html.parser"):
    """Returns html content of the page by url"""
    return BeautifulSoup(requests.get(url).text, parser)


def _get_definitions(html):
    """Returns list of word's definitions
     find on html content of the page"""
    definitions_html = html.findAll(attrs={"class": "e1q3nk1v3"})
    defs = []
    for definitions in definitions_html:
        defs.append(definitions.get_text())
    return defs


def _get_examples(html):
    """Returns list of word's usage examples
     find on html content of the page"""
    return [example.get_text() for example in
            html.findAll(attrs={"class": "one-click-content css-a8m74p e15kc6du6"})]
