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
	('product_top_type', (select p.id from parameter AS p where p.parameter_code='product_type_root' limit 0,1), 'Custom Seat Covers', '', '<p style="text-align: justify;">Custom seat covers made at Coverking and marketed by Covers4auto are designed to shield the original parts of the vehicle from damage, conceal any existing wear and tear&nbsp; caused previously, and also provide a truly customized and unique look to the interior of the vehicle.</p>

<p style="text-align: justify;">Coverking is the only custom seat cover manufacturer that has been quality certified with QS-9000 and TS16949. These deal in areas is not touched upon by any other custom seat cover manufacturer. Our custom seat covers are designed to fit any upholstery like a second skin. It difficult to decipher that the interior has been covered. We deal in customized seat covers for reclining, folding and removable chairs. Our custom seat covers are designed pertaining to features like headrests, armrests, and map pockets. Custom seat covers are also available for rear seats for quite a few numbers of vehicles, along with providing console covers for split bench seats and for side airbags. Available in an extensive variety of colors and patterns, Covers4auto also offers seat covers embroidered with personalized GM logos like Silverado, Corvette, Chevy and plenty of others. We take the term custom seat covers in all its earnestness and offer our customers a plethora of patterns and colors to choose from. Our covers are designed and patterned in a way that people mistake them for the original!</p>
<p style="text-align: justify;">No one seat cover material has been proved to be effective to safeguard your vehicle from all possible sorts of damages. That is why Coverking deals in all the possible types of materials that are minutely checked for quality. We strictly stay away from &ldquo;seconds&rdquo; and &ldquo;re-use&rdquo;. The materials used at Coverking are stringently and successfully tested in harsh conditions. They are available in a variety of colors and features. The Custom Seat Covers at Coverking do not interfere the functioning of the features that come with the seats. We also stay away from hidden and extra costs as far as we can and with the products as reasonable as we can with the use of automation and technology.</p>', 1, 1, now(), (select l.id from parameter AS l where l.parameter_value='EN' and l.parameter_code='language'));
	
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
