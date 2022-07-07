select qs.*, asub.*, ac.* from query_sequences as qs
left join (select * from attemptsubmissions where idsession = 14) as asub
	on asub.idstep = qs.step
    and asub.idquery = qs.idquery
left join attemptscommitted ac on asub.idattemptsubmission = ac.idattemptsubmission
where qs.idsequence = 'a'
order by qs.step, asub.idattemptsubmission
;

