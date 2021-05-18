from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return '<h3> zou het dan toch lukken ? <h3>'




def main():
    app.run(host='0.0.0.0', port=3001)

    return

if __name__ == '__main__':
    main()
