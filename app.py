from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger_config = {
	"headers":[],
	"specs":[
		{
			"endpoint":"docs",
			"route":'/docs.json',
		}
	],
	"static_url_path": "/flasgger_static",
	"swagger_ui":True,
	"specs_route": "/docs/"
}

swagger = Swagger(app, config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
	json_response={
		'status_code': 200,
		'description':"Hello World",
		'data': 'Hellowww World'
	}

	response_data = jsonify(json_response)
	return response_data

if __name__ == "__main__":
	app.run()