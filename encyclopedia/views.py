from django.shortcuts import render
from numpy import uint

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "util": util
    })


def title(request, **callback_kwargs):
    title = callback_kwargs['title']
    entrie = util.get_entry(title)

    if entrie is not None:
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "entrie": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/error_page.html")

