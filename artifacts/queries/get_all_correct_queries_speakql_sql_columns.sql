WITH tpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, sum(atst.planning_time) as tot_pt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
	where ats.idparticipant >= 1 and ats.idparticipant <= 20
	group by ats.idparticipant, ats.idsession, ats.idstep
)
SELECT 
	sp.idparticipant, sp.idsession, sp.idattemptsubmission, sp.idquery,
    sp.tt_speakql, sp.rt_speakql, sp.pt_speakql, sp.tpt_speakql, sp.step as step_speakql, sp.attemptnum_speakql, correct_speakql,
    sq.tt_sql, sq.rt_sql, sq.pt_sql, tpt_sql, sq.step as step_sql, sq.attemptnum_sql, correct_sql,
    sp.idsequence, sp.speakql_first, sp.ispractice,
    q.complexity, q.normalized, q.is_complex, q.num_mods, q.num_joins, q.num_funcs, q.num_proj, q.num_tables
FROM (
    SELECT 
        ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, attemptnum as attemptnum_speakql,
        total_time as tt_speakql, recording_time as rt_speakql, planning_time as pt_speakql, tot_pt as tpt_speakql, s.idsequence, 
        step, speakql_first, language, ispractice, atc.iscorrect as correct_speakql
    FROM speakql_study.attemptscommitted atc
    NATURAL JOIN speakql_study.attemptsubmissions ats
    NATURAL JOIN speakql_study.attemptsubmissiontimes atst
    NATURAL JOIN session s
    JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
    JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
    WHERE 
		(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3)) 
        and ats.idparticipant >= 1 
        and ats.idparticipant <= 20 
        and language = 'speakql'
        and transcript <> "SKIP"
    ORDER BY ats.idstep, ats.attemptnum
) as sp JOIN (
    SELECT 
		ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, ats.attemptnum as attemptnum_sql,
		total_time as tt_sql, recording_time as rt_sql, planning_time as pt_sql, tot_pt as tpt_sql, s.idsequence, 
		step, speakql_first, language, ispractice, atc.iscorrect as correct_sql
    FROM speakql_study.attemptscommitted atc
    NATURAL JOIN speakql_study.attemptsubmissions ats
    NATURAL JOIN speakql_study.attemptsubmissiontimes atst
    NATURAL JOIN session s
	JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
    JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
    WHERE 
		(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3))
        and ats.idparticipant >= 1 
        and ats.idparticipant <= 20 
        and language = 'sql'
        and transcript <> "SKIP"
    ORDER BY ats.idstep, ats.attemptnum
) as sq ON 
    sp.idparticipant = sq.idparticipant 
    AND sp.idsession = sq.idsession
    AND sp.idquery = sq.idquery
JOIN queries AS q ON sq.idquery = q.idquery
WHERE attemptnum_speakql <= 3 and attemptnum_sql <= 3