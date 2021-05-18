from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return '<h3> zou het dan toch lukken ? <h3>'




def main():
    app.run()

    return

if __name__ == '__main__':
    main()
