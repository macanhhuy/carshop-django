# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('customer_status_code', '正常', '1', '', 1, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('customer_status_code', '异常', '2', '', 2, 1, now());
	"""], sql_down=["""
	DELETE FROM parameter WHERE parameter_code='customer_status_code';
	"""])
