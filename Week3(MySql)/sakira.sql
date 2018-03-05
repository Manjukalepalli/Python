use sakila;

#1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, 
#last name, email, and address.

select cu.first_name,cu.last_name,cu.email,a.address from customer as cu
join address as a on a.address_id=cu.address_id
where city_id=312;

#2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating,
# special features, and genre (category).

select f.title,f.description,f.release_year,f.rating,f.special_features,c.name from film as f
join film_category fc on f.film_id=fc.film_id
join category c on c.category_id=fc.category_id
where c.name='comedy';

#3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, 
#film title, description, and release year.

select a.actor_id,a.first_name,a.last_name,f.title,f.description,f.release_year from film f 
join film_actor fc on f.film_id=fc.film_id
join actor a on a.actor_id=fc.actor_id
where a.actor_id=5;


#4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)?
# Your query should return customer first name, last name, email, and address.

SELECT 
    s.store_id, first_name, last_name, email, address, a.city_id
FROM
    customer c
        JOIN
    store s ON c.store_id = s.store_id
        JOIN
    address a ON a.address_id = c.address_id
WHERE
    s.store_id = 1
        AND a.city_id IN (1 , 42, 312, 459)
ORDER BY first_name;

#5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
#Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the
# 'behind the scenes' part.

select title,description,release_year,rating,special_features from film f 
join film_actor fa on f.film_id=fa.film_id
join actor a on fa.actor_id=a.actor_id where rating='g' and a.actor_id=15 and special_features='behind the scenes';


#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, 
#and actor_name.


select f.film_id,title,a.actor_id from film f 
join film_actor fa on f.film_id=fa.film_id
join actor a on fa.actor_id=a.actor_id where f.film_id=369;

#7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, 
#rating, special features, and genre (category).

select title,description,release_year,rating,special_features,name from film f 
join film_category fa on f.film_id=fa.film_id
join category c on fa.category_id=c.category_id where  rental_rate=2.99 and name='drama';


#8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, 
#description, release year, rating, special features, genre (category), and actor's first name and last name.

select * from film  f
join film_actor fa on f.film_id=fa.film_id
join actor a on a.actor_id=fa.actor_id
join film_category fc on f.film_id=fc.film_id
where a.first_name='SANDRA KILMER'
 