from flask import Flask
import os
app= Flask(__name__)
workers=int(os.environ.get('GUNICORN_PROCESSES','3'))
threads=int(os.environ.get('GUNICORN_ThREADS','1'))
@app.route('/')
def index():
    return '<h3> zou het dan toch lukken ? <h3>'




def main():
    app.run()

    return

if __name__ == '__main__':
    main()
