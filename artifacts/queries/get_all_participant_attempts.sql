WITH tpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, sum(atst.planning_time) as tot_pt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
	where ats.idparticipant >= 1 and ats.idparticipant <= 20
	group by ats.idparticipant, ats.idsession, ats.idstep
)

SELECT 
	ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, attemptnum as attemptnum_speakql,
	total_time, recording_time, planning_time, tot_pt, s.idsequence as groupnum, 
	step, speakql_first, language, ispractice, atc.iscorrect as correct_speakql, ats.usedspeakql,
    q.complexity, q.normalized, q.is_complex, q.num_mods, q.num_joins, q.num_funcs, q.num_proj, q.num_tables
FROM speakql_study.attemptscommitted atc
NATURAL JOIN speakql_study.attemptsubmissions ats
NATURAL JOIN speakql_study.attemptsubmissiontimes atst
NATURAL JOIN session s
JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
JOIN queries AS q ON ats.idquery = q.idquery
WHERE 
	(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3)) 
	and ats.idparticipant >= 1 
	and ats.idparticipant <= 20 
	and transcript <> "SKIP"
    and attemptnum <= 3
ORDER BY ats.idstep, ats.attemptnum