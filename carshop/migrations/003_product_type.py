# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

/*********** custom seat covers **********/
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Neoprene Seat Covers', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Genuine Leather Seat Covers', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Ballistic Seat Covers', 'url', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Poly Cotton Seat Covers', 'url', '', 4, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Saddle Blanket Seat Covers', 'url', '', 5, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Spacer Mesh Seat Covers', 'url', '', 6, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Tweed Seat Covers', 'url', '', 7, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Velour Seat Covers', 'url', '', 8, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'NeoSupreme Seat Covers', 'url', '', 9, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Leatherette Seat Covers', 'url', '', 10, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='1' limit 0,1), (select l.id from language AS l where l.language_code='en'));
	
/*********** customer car covers **********/
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Stormproof Car Covers', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Stretch Satin Car Covers', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Autobody Armor Car Covers', 'url', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Silverguard Car Covers', 'url', '', 4, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Silverguard Plus Car Covers', 'url', '', 5, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Coverbond-4 Car Covers', 'url', '', 6, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Triguard Car Covers', 'url', '', 7, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Mosom Plus Car Covers', 'url', '', 8, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='2' limit 0,1), (select l.id from language AS l where l.language_code='en'));

/********** custom dash covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Poly Carpet Dashboard Covers', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='3' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Velour Dashboard Covers', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='3' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Molded Carpet Dashboard Covers', 'url', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='3' limit 0,1), (select l.id from language AS l where l.language_code='en'));

/********** custom floormat **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Nylon Carpet Floor Mats', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='4' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Clear Nibbed Floor Mats', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='4' limit 0,1), (select l.id from language AS l where l.language_code='en'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Carpet-70 Ounce Floor Mats', 'url', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='4' limit 0,1), (select l.id from language AS l where l.language_code='en'));	
	
/********** custom sunshield **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_sunshield', 'Reflective Mylar Foam Sunshield', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='5' limit 0,1), (select l.id from language AS l where l.language_code='en')); 

/********** universal vehicle covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('universal_vehicle_cover', 'Universal Car Covers', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='6' limit 0,1), (select l.id from language AS l where l.language_code='en')); 

/********** universal floormats **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('universal_floormat', 'Universal Floormats', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='7' limit 0,1), (select l.id from language AS l where l.language_code='en')); 

/********** motorcycle ATV covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('motorcayle_atv_cover', 'Motorcycle Covers', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='8' limit 0,1), (select l.id from language AS l where l.language_code='en')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('motorcayle_atv_cover', 'ATV Covers', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='8' limit 0,1), (select l.id from language AS l where l.language_code='en')); 
	
/********** misc auto accessories **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Custom Masks Hood Protectors', 'url', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='9' limit 0,1), (select l.id from language AS l where l.language_code='en')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Car Cover Storage Bags', 'url', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='9' limit 0,1), (select l.id from language AS l where l.language_code='en')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Interior Accessories', 'url', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_first_menu' and p.parameter_sequence='9' limit 0,1), (select l.id from language AS l where l.language_code='en')); 

	"""], sql_down=["""
	delete from parameter where parameter_code='custom_seat_cover';
	delete from parameter where parameter_code='custom_seat_cover';
	delete from parameter where parameter_code='custom_car_cover';
	delete from parameter where parameter_code='custom_dash_cover';
	delete from parameter where parameter_code='custom_floormat';
	delete from parameter where parameter_code='custom_sunshield';
	delete from parameter where parameter_code='universal_vehicle_cover';
	delete from parameter where parameter_code='universal_floormat';
	delete from parameter where parameter_code='motorcayle_atv_cover';
	delete from parameter where parameter_code='misc_auto_accessory';

/*
	CREATE TABLE TMPXXXXX AS select p.id from parameter AS p where p.parameter_code='product_first_menu' limit 0,1;
	DELETE  FROM parameter WHERE parameter.parameter_parent_id in (select id from TMPXXXXX);
	DROP TABLE TMPXXXXX;
*/
	"""])
