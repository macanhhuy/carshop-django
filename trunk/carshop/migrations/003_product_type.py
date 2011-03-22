# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

/*********** custom seat covers **********/
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Neoprene Seat Covers', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Genuine Leather Seat Covers', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Ballistic Seat Covers', '', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Poly Cotton Seat Covers', '', '', 4, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Saddle Blanket Seat Covers', '', '', 5, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Spacer Mesh Seat Covers', '', '', 6, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Tweed Seat Covers', '', '', 7, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Velour Seat Covers', '', '', 8, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'NeoSupreme Seat Covers', '', '', 9, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_seat_cover', 'Leatherette Seat Covers', '', '', 10, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='1' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
/*********** customer car covers **********/
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Stormproof Car Covers', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Stretch Satin Car Covers', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Autobody Armor Car Covers', '', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Silverguard Car Covers', '', '', 4, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Silverguard Plus Car Covers', '', '', 5, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Coverbond-4 Car Covers', '', '', 6, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Triguard Car Covers', '', '', 7, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_car_cover', 'Mosom Plus Car Covers', '', '', 8, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='2' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

/********** custom dash covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Poly Carpet Dashboard Covers', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='3' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Velour Dashboard Covers', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='3' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_dash_cover', 'Molded Carpet Dashboard Covers', '', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='3' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

/********** custom floormat **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Nylon Carpet Floor Mats', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='4' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Clear Nibbed Floor Mats', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='4' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_floormat', 'Carpet-70 Ounce Floor Mats', '', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='4' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));	
	
/********** custom sunshield **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('custom_sunshield', 'Reflective Mylar Foam Sunshield', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='5' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 

/********** universal vehicle covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('universal_vehicle_cover', 'Universal Car Covers', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='6' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 

/********** universal floormats **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('universal_floormat', 'Universal Floormats', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='7' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 

/********** motorcycle ATV covers **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('motorcayle_atv_cover', 'Motorcycle Covers', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='8' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('motorcayle_atv_cover', 'ATV Covers', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='8' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 
	
/********** misc auto accessories **********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Custom Masks Hood Protectors', '', '', 1, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='9' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Car Cover Storage Bags', '', '', 2, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='9' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 
	
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_parent_id`, `parameter_language_id`)
VALUES
	('misc_auto_accessory', 'Interior Accessories', '', '', 3, 1,  now(), (select p.id from parameter AS p where p.parameter_code='product_top_type' and p.parameter_sequence='9' limit 0,1), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language')); 

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
	CREATE TABLE TMPXXXXX AS select p.id from parameter AS p where p.parameter_code='product_top_type' limit 0,1;
	DELETE  FROM parameter WHERE parameter.parameter_parent_id in (select id from TMPXXXXX);
	DROP TABLE TMPXXXXX;
*/
	"""])
