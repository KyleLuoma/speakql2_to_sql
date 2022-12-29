select qs.*, 
	asub.idattemptsubmission, 
    asub.idparticipant,
    asub.idsession,
    asub.transcript,
    asub.audiofilename,
    asub.time_taken,
    asub.attemptnum,
    ac.idattemptcommitted,
    ac.iscorrect
from query_sequences as qs
left join (select * from attemptsubmissions where idsession = 40) as asub
	on asub.idstep = qs.step
    and asub.idquery = qs.idquery
left join attemptscommitted ac on asub.idattemptsubmission = ac.idattemptsubmission
where qs.idsequence = 'group1'
order by qs.step, asub.idattemptsubmission
;

