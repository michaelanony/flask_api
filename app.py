from flask import Flask,Request
from flask_restful import Api,Resource
app = Flask(__name__)
api=Api(app)

class api_show(Resource):
    def get(self):
        return {"ss":"ss"}

api.add_resource(api_show,"/api/v1/")
if __name__ == '__main__':
    app.run()
