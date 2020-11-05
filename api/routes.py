"""Core Flask app routes"""
from flask import render_template, redirect, url_for
from flask import current_app as app
import pandas as pd
from . import db
from . import queries

@app.route('/pitches')
def get_pitches():
    q = queries.pitcher_pitchType
    result = pd.read_sql(
        q,
        db.engine.connect()
    )
    return {
        'pitches':result.reset_index().to_dict(orient='records')
    }
