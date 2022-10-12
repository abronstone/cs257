SELECT noc,team FROM nocs ORDER BY noc;
select concat(surname,', ',firstname) FROM athletes WHERE noc='JAM' ORDER BY surname;
SELECT athletes.surname,athletes.firstname,games.name,sports.event,results.medal FROM athletes,games,sports,results WHERE athletes.id=results.athlete_id AND sports.id=results.event_id AND games.id=results.games_id and athletes.firstname LIKE '%Greg%' AND athletes.surname LIKE '%Louganis%' AND medal='Gold'; 
SELECT athletes.noc,count(medal) AS golds FROM athletes,results WHERE athletes.id=results.athlete_id AND medal='Gold' GROUP BY athletes.noc ORDER BY golds desc;