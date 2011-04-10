# -*- coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '英语', 'EN', '', 1, 1, now());
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '法语', 'FR', '', 2, 1, now());
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '西班牙语', 'ES', '', 3, 1, now());
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '德语', 'DE', '', 4, 1, now());
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '意大利语', 'IT', '', 5, 1, now());
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('language', '中文', 'ZH-CN', '', 6, 1, now());

	"""], sql_down=["""
	DELETE FROM parameter where parameter_code='language';
	"""])