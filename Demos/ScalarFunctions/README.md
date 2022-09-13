# Functions demo 
```
-- String Functions

select title, 
	INITCAP(title) as capitalized_title  -- Capitalizes the First Letter of Every Word 
from film; 

select 
	first_name || ' ' || last_name as name
from customer; 

-- Mathematical Functions
select film_id, 
		title,
		 release_year, 
		 rental_duration*24 as rental_duration_hour,
		 rental_rate, 
		 round(rental_rate) as rounded_rental_rate
	 from film; 

-- Date/Time Functions
select  film_id, 
		title, 
		current_date, 
		last_update, 
		current_date - last_update as days_since_last_update
from film; 


-- Data Type Formatting
select rental_id, rental_date, inventory_id, customer_id, staff_id::text as staff_id from rental; 


-- System Information Functions
select current_database();
select version(); 

```