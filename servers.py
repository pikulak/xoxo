import logging
import _thread

from flask import Flask, render_template

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class WebServer:
    app = Flask(__name__)
    app.secret_key = "some_secret"
    running = False
    render_kwargs = {}

    @app.route("/")
    def main():
        return render_template("main.html", **WebServer.render_kwargs)

    def run():
        if not WebServer.running:
            _thread.start_new_thread(WebServer.app.run, ())
            WebServer.running = True




