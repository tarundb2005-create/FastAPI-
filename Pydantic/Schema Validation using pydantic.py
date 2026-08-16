from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title : str
    content : str

#order is important same as first come first serve

@app.get("/")
def test():
    return "Succesfully my api runs"

@app.post("/createpost")
def create_post(new_post : Post):
    print(new_post.title)
    return {
       
        "data": "new_post"
    }


#using postman api testing results :
#{
#    "title" : "doomsday",
#    "content" : "avengers"
#}

