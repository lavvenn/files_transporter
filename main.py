import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="books"
)

tamplate = Jinja2Templates(directory="templates")

def get_all_books():
    return os.listdir("books")


@app.get("/", response_class=FileResponse)
def get_main(request: Request):
    book_list = get_all_books()
    return tamplate.TemplateResponse(request=request,name="base.html", context={"books": book_list})


@app.get("/test")
def get_test():
    return get_all_books()


@app.get("/book/{book_name}", response_class=FileResponse)
def get_main(book_name):
    return FileResponse(f"books/{book_name}")



