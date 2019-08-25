from sanic import Sanic
from sanic import response
from food import Food
import os

app = Sanic()
dir_path = os.path.dirname(os.path.realpath(__file__))
app.config.filefolder = dir_path + "/uploads"
app.static('/photo', './uploads')
foods = []


@app.route("/", methods=['GET'])
async def on_food_list(request):
    return response.json(foods)


@app.route("/food", methods=['POST'])
async def on_food_create(request):
    food_id = len(foods) + 1


    if not os.path.exists(app.config.filefolder):
        os.makedirs(app.config.filefolder)

    first_upload_file = request.files["photo"][0]
    filename, file_extension = os.path.splitext(first_upload_file.name)

    f = open(f"{app.config.filefolder}/{food_id}{file_extension}", "wb")
    f.write(first_upload_file.body)
    f.close()

    food = Food(food_id, request.form["name"][0], request.form["rating"][0], f"{food_id}{file_extension}")
    foods.append(food)

    return response.json(True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)