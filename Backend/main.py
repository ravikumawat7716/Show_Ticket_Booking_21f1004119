from flask import Flask
print("test1")

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server is running.'

if __name__=='__main__':
    app.run()