# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

/**********  **********/

	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('product_menu_root', 'Product Menu Root', '1', '菜单跟目录', 1, 1, now());
	
/**********  **********/

	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Custom Seat Covers', 'url', '', 1, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Custom Car Covers', 'url', '', 2, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Custom Dash Covers', 'url', '', 3, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Custom Floormats', 'url', '', 4, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Custom Sunshield', 'url', '', 5, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Universal Vehicle Covers', 'url', '', 6, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Universal Floormats', 'url', '', 7, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Motorcycle ATV Covers', 'url', '', 8, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_first_menu', (select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1), 'Misc Auto Accessories', 'url', '', 9, 1, now(), (select l.id from language AS l where l.language_code='en'));
	
	"""], sql_down=["""
	CREATE TABLE TMPXXXXX AS select p.id from parameter AS p where p.parameter_code='product_menu_root' limit 0,1;
	DELETE  FROM parameter WHERE parameter.parameter_parent_id in (select id from TMPXXXXX);
	DROP TABLE TMPXXXXX;
	
	DELETE FROM parameter WHERE parameter_code='product_menu_root';
	"""])
