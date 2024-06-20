use students;

select name, max(age) from Students;

select name, max(age) from Teachers;

select t1.name, count(t2.teacher_id) as t_count
from Teachers t1
join Teachers2Competencies t2
on t1.id = t2.teacher_id
group by teacher_id;

select c.title, count(s.course_id)
from Courses c
join Students2Courses s
on c.id = s.course_id
group by s.course_id;

select c.name, count(s.student_id)
from Students c
join Students2Courses s
on c.id = s.student_id
group by s.student_id;
