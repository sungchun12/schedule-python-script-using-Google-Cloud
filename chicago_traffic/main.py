#Use this script to call the append_data.py script. The main script calls the 
#script which runs the commands/programs you want. 

from __future__ import print_function, absolute_import #package to smooth over python 2 and 3 differences
from datetime import datetime, timedelta
import logging
from flask import Flask, request
from google.cloud import bigquery
import function.append_data as append_data #the subfolder structure for calling the script

app = Flask(__name__)

@app.route('/chicago-traffic/append-data') #make up memorable URL-will be used in cron job syntax
def start_traffic_append_data(): #make up memorable function name for cron job
    is_cron = request.headers.get('X-Appengine-Cron', False)
    if not is_cron:
        return 'Bad Request', 400

    try:
        append_data.run() #the actual name of the script/function you want to run contained in the subfolder
        return "Pipeline started", 200
    except Exception as e:
        logging.exception(e)
        return "Error: <pre>{}</pre>".format(e), 500
        
@app.errorhandler(500) #error handling script for troubleshooting
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__': #hosting administration syntax
    app.run(host='127.0.0.1', port=8080, debug=True)