from flask import Flask, render_template,request,redirect
from flask_pymongo import PyMongo,pymongo
app = Flask(__name__)

mongo = pymongo.MongoClient(
    host="localhost",
    port=27017,
    serverSelectionTimeoutMS = 1000
)
db = mongo.snehaport
mongo.server_info()
# app.config['MONGO_URI']='mongodb://localhost:27017/portfolio'

# mongo  = PyMongo(app)
@app.route('/')
def index():
    return render_template('dom.html')

@app.route('/check',methods = ['GET','POST'])
def check():
    data = request.form
    dbResponse = db.data.insert_one(dict(name=data['name'],email=data['email'],emailsub=data['emailsub'],phone=data['number'],message=data['message']))
    print(dbResponse)
    # mongo.db.record.insert(dict(name=data['name'],email=data['email'],phone=data['phone'],message=data['message']))
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
