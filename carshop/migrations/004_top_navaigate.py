# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
/********* 英语 导航 **********/
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Home', 'url', '', 1, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'View All Make', 'url', '', 2, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Best Sellers', 'url', '', 3, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Clearance Sale', 'url', '', 4, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'New Arrivals', 'url', '', 5, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Products', 'url', '', 6, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Gift Certificate', 'url', '', 7, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'FAQ\\'S', 'url', '', 8, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'Contact', 'url', '', 9, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));

/********* 中文 导航 *********/

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '首页', 'url', '', 1, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '制造商', 'url', '', 2, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '畅销产品', 'url', '', 3, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '清仓甩卖', 'url', '', 4, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '最新上架', 'url', '', 5, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '所有产品', 'url', '', 6, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '礼券', 'url', '', 7, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', 'FAQ\\'S', 'url', '', 8, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));
	
	INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_desc`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`, `parameter_language_id`)
VALUES
	('top_navigate', '联系我们', 'url', '', 9, 1, now(), (select l.id from parameter AS l where l.parameter_value='ZH-CN' and l.parameter_code='language'));	

	"""], sql_down=["""
	DELETE FROM parameter WHERE parameter_code='top_navigate';
	"""])