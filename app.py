from flask import Flask, jsonify, request
from requester import get_currency


app = Flask(__name__)

client = app.test_client()


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