from django.shortcuts import render, redirect
from pyexpat.errors import messages
from trans import to_cyrillic, to_latin

def index(r):
    return render(r,'index.html')
def latin(r):
    return render(r,'lotin.html')


def kril(r):
    if r.method == "POST":
        kril = r.POST['kril']
        t = to_cyrillic(kril)
        return render(r, 'index.html',
        {'kril':kril,
         't':t,})
def lotin(r):
    if r.method == "POST":
        lotin = r.POST['lotin']
        t = to_latin(lotin)
        return render(r, 'lotin.html',
        {'lotin':lotin,
         't':t,})