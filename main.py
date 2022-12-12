from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from PIL import Image
import imagehash

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# @app.post("/")
# async def root():
#     return {"message": "K190212 K191328 K190240"}

@app.get("/", response_class=HTMLResponse)
async def get_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})

@app.post("/")
async def post_image(request:Request, image_url:str = Form(), image_url2:str = Form()):
    hash1 = imagehash.phash(Image.open(f'\\Users\\mhammad\\\Desktop\\IS_Project\\images\\{image_url}'))
    hash2 = imagehash.phash(Image.open(f'\\Users\\mhammad\\Desktop\\IS_Project\\images\\{image_url2}'))
    print(hash1-hash2)
    return templates.TemplateResponse("item.html", {"request": request, "hash_result": "forgery detected" if abs(hash1-hash2) < 10 else "both are relatively different"})
