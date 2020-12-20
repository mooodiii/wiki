from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from . import util

import markdown

import random

page = ""
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    md = markdown.Markdown()
    title = util.get_entry(name)
    global page
    page = name
    return render(request, "encyclopedia/title.html",{
        "title": md.convert(title),
        "t": name
    })
    
    
def search(request):
    if request.method == "POST":
        data = request.POST.get('q')
        print(data)
        if util.get_entry(data) :
            md = markdown.Markdown()
            return render(request, "encyclopedia/title.html", {
                "title": md.convert(util.get_entry(data)),
                "t": data
            })
        else:
            entries = []
            titles = util.list_entries()
            for title in titles:
                title = title.lower()
                if (title.find(data.lower()) != -1):
                    entries.append(title)
            return render(request, "encyclopedia/search.html", {
                "entries": entries
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
                    
def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title):
            return HttpResponse("<h1>Content exist.</h1>")
        else:
            md = markdown.Markdown()
            util.save_entry(title, content)
            return render(request, "encyclopedia/title.html", {
                "title": md.convert(util.get_entry(title)),
                "t": title
            })
    return render(request, "encyclopedia/add.html")


def edit(request):
    global page
    name = page
    if request.method == "POST":
        md = markdown.Markdown()
        content = request.POST.get('content')
        util.save_entry(name, content)
        return render(request, "encyclopedia/title.html", {
            "title": md.convert(util.get_entry(name)),
            "t": name
        })
    return render(request, "encyclopedia/edit.html", {
        "title": util.get_entry(name),
        "t": title
    })

def rand(request):
    md = markdown.Markdown()
    entries = util.list_entries()
    entry = random.choice(entries)
    return render(request, "encyclopedia/title.html", {
        "title": md.convert(util.get_entry(entry)),
        "t": entry
    })
