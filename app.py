from flask import Flask, render_template
import requests

app = Flask(__name__)

# check if a string is convertible to integer
def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>')
def pokemon(query):
    # receive data from API
    url = "https://www.pokeapi.co/api/v2/pokemon/" + query
    pokemon_data = requests.get(url).json()
    name = pokemon_data.get("forms")[0].get("name")
    number = pokemon_data.get("game_indices")[0].get("game_index")
    
    # if pokemon id is searched
    if is_int(query):
        return '<h1>The pokemon with id ' + str(number) + ' is ' + name + ' </h1>'
    
    # if pokemon name is searched
    else:
        return '<h1>' + name + ' has id ' + str(number) + '</h1>'

if __name__ == '__main__':
    app.run()
