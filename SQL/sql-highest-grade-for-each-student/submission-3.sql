select er1.student_id, er1.exam_id, er1.score
from exam_results er1
left join exam_results er2
    on er2.student_id = er1.student_id
    and (er2.score > er1.score or (er2.score = er1.score and er2.exam_id < er1.exam_id))
where er2.student_id is null
order by er1.student_id;