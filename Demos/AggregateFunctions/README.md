```
-- Aggregate functions

select c.name, round(avg(f.rental_rate), 2) as average_rate 
from film f
join film_category fc on f.film_id  = fc.film_id 
join category c  on fc.category_id = c.category_id 
group by c.name; 


select c.name, sum(f.rental_rate) as total_value 
from film f
join film_category fc on f.film_id  = fc.film_id 
join category c  on fc.category_id = c.category_id 
group by c.name; 


select count(customer) from customer; 
```