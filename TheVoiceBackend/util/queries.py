GET_CURRENT_USER = "SELECT first_name, last_name, username, a.id, ur.name as role FROM auth_user a, authentication_userprofile ap, authentication_userrole ur WHERE a.id=ap.user_id AND a.username=%s AND ap.role_id=ur.uuid"

GET_MENTOR_CANDIDATES = "SELECT first_name||' '||last_name as candidate_name,  username, a.id as candidate_id FROM  auth_user a, authentication_candidatementer ac WHERE ac.candidate_id = a.id AND ac.mentor_id=%s"

GET_TEAM_CANDIDATES = "SELECT (SELECT first_name||' '||last_name FROM auth_user WHERE id=ac.candidate_id) as candidate_name, ac.candidate_id, (SELECT first_name||' '||last_name FROM auth_user WHERE id=ac.mentor_id) as mentor_name, ac.mentor_id, ROUND(AVG(score)) as score FROM  auth_user a, authentication_userprofile ap, authentication_userrole ur, authentication_candidatementer ac,  performance_performancescore ps, performance_performance p WHERE a.id=ap.user_id  AND ac.candidate_id = a.id AND ap.role_id=ur.uuid AND p.candidate_id = ac.candidate_id AND p.uuid = ps.performance_id AND ur.name != 'admin' GROUP BY ac.candidate_id"

GET_CANDIDATE_SCORE = "SELECT(SELECT first_name||' '||last_name FROM auth_user WHERE id=ps.mentor_id) as mentor_name, score, event_date, song_name FROM performance_performancescore ps,performance_performance p WHERE  p.uuid = ps.performance_id AND p.candidate_id = %s"

GET_MENTOR_CANDIDATE_SCORE = "SELECT(SELECT first_name||' '||last_name FROM auth_user WHERE id=ps.mentor_id) as mentor_name, ROUND(AVG(score)) as score, event_date, song_name FROM performance_performancescore ps,performance_performance p  WHERE  p.uuid = ps.performance_id AND p.candidate_id = %s GROUP BY p.candidate_id"

GET_MENTOR_AVG_SCORE = "SELECT ROUND(AVG(score)) as score FROM performance_performancescore WHERE mentor_id = %s GROUP BY mentor_id"