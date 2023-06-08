/* Write your PL/SQL query statement below */
select name from salesperson
minus
select s.name
from SalesPerson s,Company c, Orders o
where o.com_id=c.com_id and  o.sales_id=s.sales_id and c.name='RED';