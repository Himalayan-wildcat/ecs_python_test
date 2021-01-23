from flask import Flask, render_template
from logging import INFO, ERROR, Formatter, StreamHandler, getLogger


app = Flask(__name__)
app.logger.disalbed = True
werkzeug_logger = getLogger('werkzeug')
werkzeug_logger.disabled = True

logger = getLogger(__name__)
formatter = Formatter(
    '[%(levelname)s] %(asctime)s %(message)s', '%Y-%m-%d %H:%M:%S')
handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(formatter)
logger.setLevel(INFO)
logger.addHandler(handler)


@app.route('/healthz')
def healhtz():
    return 'healthcheck ok'

@app.route('/info')
def info():
    logger.info('This is s stdout')
    return 'STDOUT/This is version4.'

@app.route('/error')
def error():
    logger.fatal("This is a stderr")
    return 'STDERR/This is version4.'

@app.route('/')
def index():
    logger.info("Rendering index.html ...")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
