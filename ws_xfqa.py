from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import flask
import json
import datetime
import logging

app = flask.Flask(__name__)

logger = logging.getLogger("xfqa")
import xfqa_utils
import optparse, sys

@app.route("/query", methods=['GET', 'POST'])
#   query by xfqa    
#     input: 
#         q: user's sentence...
#     return: json, xf answer
def query():
    question = flask.request.values.get('q')
    if not question:
        return flask.make_response("tell me something", 200)
    
    t0 = datetime.datetime.now()      

    answer = xfqa_utils.QA(question)
    
    t1 = datetime.datetime.now()
    rtime = str((t1 - t0)) 
    logger.info(question + " query takes:" + rtime)
    sys.stdout.flush()
    
    ret = {}
    ret['ret'] = True;
    ret['input'] = question
    ret['hello'] = "This is the response by dananlp[xfqa]..."
    ret['answer'] = answer
    ret['rtime'] = rtime
    
    return flask.make_response(json.dumps(ret, indent=4, ensure_ascii=False), 200, {'Content-Type': 'text/json; charset=utf-8'})


if __name__ == "__main__":
#     program = os.path.basename(sys.argv[0])
#     logger = logging.getLogger(program)

    logging.basicConfig(filename='log.txt' ,format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
#     logger.setLevel(logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    
    logger.info ("start...")

    """
    Parse command line options and start the server.
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-p', '--port',
        help="which port to serve content on",
        type='int', default=5040)
    
    opts, args = parser.parse_args()
    app.run(debug=False, processes=1, host='0.0.0.0', port=opts.port)
else:
#     test.find_keys_test()
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info ("start...")
