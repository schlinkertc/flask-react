"""Core Flask app routes"""
from flask import render_template, redirect, url_for
from flask import current_app as app
import pandas as pd
from . import db

@app.route('/pitches')
def get_pitches():
    result = pd.read_sql(
        'select * from pitches limit 10',
        db.engine.connect()
    )
    return {
        'pitches':result[
            ['gamePk','pitchData_endSpeed']].to_dict(orient='records')
    }
