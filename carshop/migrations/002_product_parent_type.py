# -*- coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

/**********  **********/

	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('product_type_root', 'Product Menu Root', '1', '菜单跟目录', 1, 1, now());
	
/**********  **********/

	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Seat Covers', '', '', 1, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Car Covers', '', '', 2, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Dash Covers', '', '', 3, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Floormats', '', '', 4, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Sunshield', '', '', 5, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Universal Vehicle Covers', '', '', 6, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Universal Floormats', '', '', 7, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Motorcycle ATV Covers', '', '', 8, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_parent_id`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Misc Auto Accessories', '', '', 9, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	"""], sql_down=["""
	CREATE TABLE TMPXXXXX AS select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1;
	DELETE  FROM parameter WHERE parameter.parameter_parent_id in (select id from TMPXXXXX);
	DROP TABLE TMPXXXXX;
	
	DELETE FROM parameter WHERE parameter_code='product_type_root';
	"""])
