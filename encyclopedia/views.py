from django.shortcuts import render
from numpy import uint

from encyclopedia.models import NewPageForm

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
        return render(request, "encyclopedia/error_page.html", {
            "error": "The request page was not found"
        })


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
        return render(request, "encyclopedia/error_page.html", {
            "error": "No result was found with that entry"
        })


def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })


def save_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            page_title = form.cleaned_data["title"]
            if util.entry_exist(page_title):
                return render(request, "encyclopedia/new_page.html", {
                    "error": "Page with that title already exists",
                    "form": form
                })
            else:
                page_content = form.cleaned_data["content"]
                util.save_entry(page_title, page_content)

                # Render the page after save it
                return render(request, "encyclopedia/title.html", {
                    "title": page_title,
                    "entrie": util.get_entry(page_title)
                })
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })


def edit_page(request, **callback_kwargs):
    title = callback_kwargs['title']
    entrie = util.get_entry(title)

    form_data = {'title': title, 'content': entrie}

    return render(request, "encyclopedia/edit_page.html", {
        "form": NewPageForm(form_data)
    })


def update_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            page_title = form.cleaned_data["title"]
            page_content = form.cleaned_data["content"]
            util.save_entry(page_title, page_content)

            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                "util": util
            })

        else:
            return render(request, "encyclopedia/new_page.html", {
                "error": "Error updating the page",
                "form": form
            })
