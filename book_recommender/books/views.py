import pandas as pd
from django.shortcuts import render
from tqdm import tqdm

from .models import Book


# Create your views here.
def update_DB(request):
    df = pd.read_csv("./raw_data_merged.csv")

    for i in tqdm(df.index):
        if len(Book.objects.filter(title=df.loc[i, "title"])) == 0:
            Book.objects.create(
                title=df.loc[i, "title"],
                summary=df.loc[i, "summary"],
                category=df.loc[i, "category"],
                author=df.loc[i, "author"],
            )
    return render(request, "books/update.html")


def index(request):
    return render(request, "books/index.html")
