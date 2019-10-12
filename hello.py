from flask import Flask
from fakekit.fake import fake

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! ' + str(fake(3, 5))

if __name__ == '__main__':
    app.run()
