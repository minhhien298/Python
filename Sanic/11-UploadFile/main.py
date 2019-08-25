from sanic import Sanic
from sanic import response
import os

app = Sanic()
dir_path = os.path.dirname(os.path.realpath(__file__))
app.config.filefolder = dir_path + "/uploads"


@app.route("/upload", methods=['GET'])
async def on_file_list(request):
    return response.json(
        [{
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
            }])


@app.route("/upload", methods=['POST'])
async def on_file_upload(request):
    if not os.path.exists(app.config.filefolder):
        os.makedirs(app.config.filefolder)
    print(app.config.filefolder + "/" + request.files["file"][0].name)
    f = open(app.config.filefolder + "/" + request.files["file"][0].name,"wb")
    f.write(request.files["file"][0].body)
    f.close()

    return response.json(True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)