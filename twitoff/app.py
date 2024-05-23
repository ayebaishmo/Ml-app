from flask import Flask, render_template
from .models import DB, User, Tweet


# create flask factory
def create_app():
    app = Flask(__name__)

    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register our database with the app
    DB.init_app(app)

    my_var = "Twittoff App"

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template("base.html", title="Home")

    @app.route ('/bananas')
    def bananas():
        return render_template("base.html", title="Banana")
    
    @app.route('/reset')
    def reset():
        # Drop all database tables
        DB.drop_all()

        DB.create_all()
        return "Database has been reset"

        # Recreate all database tables according to
        # indicates schema in models.py

    @app.route('/populate')
    def populate():
        # create two fake users
        Ishmo = User(id=1, username='Ishmo')
        DB.session.add(Ishmo)
        Julian = User(id=2, username='Julian')
        DB.session.add(Julian)

        #create two fake tweets on the DB
        tweet1 = Tweet(id=1, text='Ishmos text', user=Ishmo)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text='Julians text', user=Julian)
        DB.session.add(tweet2)

        # save the changes we just made to the database
        # "commit" the database changes
        DB.session.commit()

        return "Database has been populated"
    return app