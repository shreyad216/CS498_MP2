from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

seed = 0

#@app.route('/')
#def home():
 # return render_template('index.html', seed = seed)

@app.route('/',methods = ['POST', 'GET'])
def login():
    global seed
    #print(request.method)
    if request.method == 'POST':
        #seed = request.form['nm']
        seed = request.json.get('num')
        print("POST %s", seed)
       # return render_template('index.html', seed = 'updated')
        return "updated"
    else:
        return str(seed)


if __name__ == '__main__':
   app.run(debug = True)