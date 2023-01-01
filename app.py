from flask import Flask, jsonify, request
from requester import get_currency
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)

client = app.test_client()

docs = FlaskApiSpec()
docs.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='currency',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()]
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

@app.route('/api/rates', methods=['GET'])
def get_list():
    data = {
        'from': request.args.get('from'),
        'to': request.args.get('to'),
        'value': request.args.get('value')
    }
    try:
        value = float(data['value'])
        currency = get_currency(data['from'].upper(), data['to'].upper(), value)
    except Exception as ex:
        print(ex)
        return {'message': str(ex)}, 400
    result = {'result': currency}
    return jsonify(result)



if __name__ == '__main__':
    app.run()