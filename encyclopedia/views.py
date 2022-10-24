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


def searh(request):
    query = request.GET.get("q")
    entries = util.get_coincidence_entries(query)
    if entries is not None and len(entries) == 1 and entries[0].lower() == query.lower():
        return render(request, "encyclopedia/title.html", {
            "title": query,
            "entrie": util.get_entry(query)
        })
    elif len(entries) >= 1:
        return render(request, "encyclopedia/search_results.html", {
            "entries": entries
        })
    else:
        return render(request, "encyclopedia/error_search.html")
