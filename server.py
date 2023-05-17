from multiprocessing import Process

from flask import Flask, request
import runpy
import sys

app = Flask(__name__)


# Define a function to run runpy in a separate process
def run_module(module):
    runpy.run_module(module, run_name='__main__')


@app.route('/start', methods=['POST'])
def start_script():
    # Get the arguments from the request
    interceptor_base_url = request.args.get('interceptor_base_url')
    dataset_filename = request.json.get('dataset_filename')
    buffer_size = request.json.get('buffer_size')
    should_normalize = request.json.get('normalize')
    module = request.json.get('module')

    sys.argv = ['', interceptor_base_url, dataset_filename, buffer_size, should_normalize]

    # Start the process and return an empty response to the client
    process = Process(target=run_module, args=(module,))
    process.start()
    return {}


if __name__ == '__main__':
    app.run(debug=True)
