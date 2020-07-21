"""Core Flask app routes"""
from flask import render_template, redirect, url_for
from flask import current_app as app
import pandas as pd
from . import db
from . import queries

@app.route('/pitches')
def get_pitches():
    q = queries.pitcher_pitchType
    df = pd.read_sql(
        q,con=db.engine).\
        sort_values('avg_endSpeed',ascending=False).\
        groupby('pitchType')['avg_startSpeed'].mean()
    result = pd.read_sql(
        #'select * from pitches limit 15',
        q,
        db.engine.connect()
    )
    return {
        'pitches':df.reset_index().to_dict(orient='records')
    }
