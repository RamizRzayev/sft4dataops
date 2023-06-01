drop view if EXISTS info_v2;

create or replace view info_v2 
as 
select 
d.name as dept_name ,
e.name as emp_name 
from 
dept d join emp e on (d.id=e.deptid);

