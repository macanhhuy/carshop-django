# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('英语', 'EN', 1);
	
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('法语', 'FR', 2);
	
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('西班牙语', 'ES', 3);
	
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('德语', 'DE', 4);
	
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('意大利语', 'IT', 5);
	
	INSERT INTO language
	(`language_name`, `language_code`, `language_sequence`)
VALUES
	('中文', 'ZH-CN', 6);

	"""], sql_down=["""
	DELETE FROM language;
	"""])