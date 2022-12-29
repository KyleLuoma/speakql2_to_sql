SELECT * FROM speakql_study.attemptscommitted atc
NATURAL JOIN speakql_study.attemptsubmissions ats
NATURAL JOIN speakql_study.attemptsubmissiontimes atst
NATURAL JOIN session s
JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
WHERE idparticipant = 22
ORDER BY idstep, attemptnum
;


