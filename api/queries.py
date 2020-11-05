pitcher_pitchType ="""
    SELECT
        players.fullname,
    	p.details_type_description as pitchType,
        avg(p.pitchData_endSpeed) as avg_endSpeed,
        avg(p.pitchData_startSpeed) as avg_startSpeed,
        avg(p.pitchData_breaks_spinRate) as average_spinRate,
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
    INNER JOIN
        players
        ON
        players.id=m.pitcher_id
    WHERE
    	details_type_description not in ('Automatic Ball','Knuckle Ball', 'Eephus','Forkball')
    	and
    	details_type_description is not null
    group by
    	m.pitcher_id, p.details_type_description
    having
    	count(distinct(p.gamePk)) > 5
    limit
        6
    ;
        """
