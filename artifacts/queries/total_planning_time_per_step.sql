select idparticipant, idsession, idstep, sum(atst.planning_time) as tpt
from attemptsubmissiontimes atst
natural join attemptsubmissions at
where idparticipant >= 1 and idparticipant <= 20
group by idparticipant, idsession, idstep
having tpt > 0
