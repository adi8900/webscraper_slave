from flask import Flask, request, jsonify
import worker

app = Flask(__name__)

@app.route('/task', methods=['POST'])
def handle_task():
    task = request.get_json()
    url = task.get('url')
    data_types = task.get('data_types',['all'])
    result = worker.run_multiprocessing_task(url,data_types)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
