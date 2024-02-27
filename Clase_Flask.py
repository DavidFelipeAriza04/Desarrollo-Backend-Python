from flask import Flask, request
import requests

app = Flask("__name__")


@app.route("/")
def hello_world():
    print(request)
    user = request.headers.get("user")
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()

    print(response)
    if user == None:
        return f"""
        <img src = {data['icon_url']}></img>
        <p>{data['value']}</p>
        <h1>Hola Mundo</h1>
        """
    else:
        return f"""
        <h1>Hola {user}</h1>
        <img src = {data['icon_url']}></img>
        <p>{data['value']}</p>
        <h1>Hola Mundo</h1>
        
        """


if __name__ == "__main__":
    app.run(debug=True)
