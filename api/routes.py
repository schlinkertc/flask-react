"""Core Flask app routes"""
from flask import render_template, redirect, url_for
from flask import current_app as app
import pandas as pd
from . import db

@app.route('/pitches')
def get_pitches():
    q = """
        SELECT
        	m.pitcher_id,
        	p.details_type_description as pitchType,
        	avg(p.pitchData_breaks_spinRate) as average_spinRate,
        	avg(p.pitchData_endSpeed) as avg_endSpeed,
        	count(distinct(p.gamePk)) as games_pitched,
        	count(pitcher_id) as count
        FROM
        	pitches p
        INNER JOIN
        	matchups m
        	ON
        		m.gamePk=p.gamePk
        		and
        		m.atBatIndex=p.atBatIndex
        		and
        		m.playEndTime=p.playEndTime
        WHERE
        	details_type_description not in ('Automatic Ball','Knuckle Ball', 'Eephus','Forkball')
        	and
        	details_type_description is not null
        group by
        	m.pitcher_id, p.details_type_description
        having
        	games_pitched > 5;
            """
    result = pd.read_sql(
        #'select * from pitches limit 10',
        q,
        db.engine.connect()
    )
    return {
        'pitches':result.reset_index().to_dict(orient='records')
    }
