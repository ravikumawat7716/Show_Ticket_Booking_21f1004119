from utils.configuration import create_app
import api.authentication
import api.venues
from utils.mail import send_email
# from instance.app import app

app = create_app()


@app.route('/')
def index():
    return 'Backend Server is running.'

@app.route('/test')
def test():
    send_email()
    return 'Testing email'
    

if __name__=='__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     print(data)
#     username = data['username']
#     password = data['password']
#     if username == 'ravi' and password == 'admin':
#         return {"token": '1234', "username": 'ravi', "role" : "user"},200
#     if username == 'nikhil' and password == 'admin123':
#         return {"token": '12343', "username": 'nikhil', "role" : "admin"},200
#     return 'Invalid credentials.', 401

# @app.route('/userdata', methods=['GET'])
# def userdata():
#     token = request.headers.get('Authorization')
#     if token == '1234':
#         return {"name": 'Ravi', "email": '21f1004119@ds.study.iitm.ac.in'},200
#     else :
#         return {"message" : 'Unauthorized'}, 200

# @app.route('/admin', methods=['GET'])
# def admindata():
#     token = request.headers.get('Authorization')
#     if token == '12343':
#         return jsonify([{"name": 'Ravi', "email":"ravi@iitm.ac.in"},{ "name": 'Nikhil', "email": "nikhil@bits.ac.in"},{
#             "name": 'Andrew', "email": 'andrew@ee.iitm.ac.in'
#         }]) ,200
#     else :
#         return {"message" : 'Unauthorized'}, 401


