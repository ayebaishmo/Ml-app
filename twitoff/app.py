from flask import Flask, render_template

# create flask factory
def create_app():

    app = Flask(__name__)
    my_var = "Twittoff App"

    @app.route('/')
    def root():
        return render_template("base.html", title="Home")

    @app.route ('/bananas')
    def bananas():
        return render_template("base.html", title="Banana")
    
    return app