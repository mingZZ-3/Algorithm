SELECT 
    A.ANIMAL_ID, A.NAME
from ANIMAL_OUTS A
inner join ANIMAL_INS C
on A.animal_id = C.animal_id
where A.datetime < C.datetime
order by C.datetime
