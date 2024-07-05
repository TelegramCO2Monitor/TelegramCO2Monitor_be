INSERT INTO public.users(
	id, name, admin, active, phone, registration_date, total_messages_weight, email)
	VALUES (1, 'luca' , 'true' , 'true' , '333445566' , '2024-07-05' , 0 , 'luca@gmail.com' );    

INSERT INTO public.users(
	id, name, admin, active, phone, registration_date, total_messages_weight, email)
	VALUES (2, 'paolo' , 'true' , 'true' , '333445566' , '2024-07-05' , 0 , 'paolo@gmail.com' );    

INSERT INTO public.users(
	id, name, admin, active, phone, registration_date, total_messages_weight, email)
	VALUES (3, 'federico' , 'true' , 'true' , '333445566' , '2024-07-05' , 0 , 'fede@gmail.com' );    

INSERT INTO public.users(
	id, name, admin, active, phone, registration_date, total_messages_weight, email)
	VALUES (4, 'andrea' , 'true' , 'true' , '333445566' , '2024-07-05' , 0 , 'andre@gmail.com' );    

INSERT INTO public.users(
	id, name, admin, active, phone, registration_date, total_messages_weight, email)
	VALUES (5, 'lucia' , 'true' , 'true' , '333445566' , '2024-07-05' , 0 , 'lucy@gmail.com' );    



INSERT INTO public.messages(
	id, type, weight, date, user_id)
	VALUES (1, 'text', 100 , '2024-05-07' , 1 ); 

INSERT INTO public.messages(
	id, type, weight, date, user_id)
	VALUES (2, 'text', 500 , '2024-05-07' , 1 );  

INSERT INTO public.messages(
	id, type, weight, date, user_id)
	VALUES (3, 'text', 300 , '2024-05-07' , 3 ); 

INSERT INTO public.messages(
	id, type, weight, date, user_id)
	VALUES (4, 'text', 500 , '2024-05-07' , 4 ); 

INSERT INTO public.messages(
	id, type, weight, date, user_id)
	VALUES (5, 'text', 200 , '2024-05-07' , 2 ); 
