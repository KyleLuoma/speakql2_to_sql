select * from attemptsubmissions 
where 
	idattemptsubmission not in (select idattemptsubmission from attemptscommitted)
	and idsession = 40
