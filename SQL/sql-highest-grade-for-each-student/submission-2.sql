select t1.student_id, min(t1.exam_id) AS exam_id, t1.score 
from exam_results t1 
inner join 
    (select student_id, max(score) AS max_score from exam_results group by student_id) j1 
    on t1.student_id = j1.student_id and t1.score = j1.max_score 
group by t1.student_id, t1.score 
order by t1.student_id;