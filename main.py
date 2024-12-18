from flask import Flask, render_template, request, redirect, url_for

from data import data
# from data.tours_to_db import data_to_db
from data.base import Session, create_db
from data.models import Tour, User
# 

app = Flask(__name__)


@app.context_processor
def glob_data():
    return dict(departures=data.departures)



@app.route('/')
def index():
    with Session() as session:
        tours = session.query(Tour).all()
        return render_template("index.html",   tours=tours)


@app.route('/tour/<int:index>')
def tour(index):
    with Session() as session:
        tour = session.query(Tour).where(Tour.id == index).first()
    return render_template("tour.html",   tour=tour)


@app.route('/departure/<dep>/')
def departure(dep):
    with Session() as session:
        tours = session.query(Tour).where(Tour.departure == dep).all       
    return render_template("departure.html",   tours=tours)


if __name__ == "__main__":
    app.run(debug=True)
    create_db()
    # data_to_db()