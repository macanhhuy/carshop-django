# coding: utf-8

from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Afghanistan', 'AFG', 1, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Albania', 'ALB', 2, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Algeria', 'ALG', 3, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Andorra', 'AND', 4, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Angola', 'ANG', 5, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Antigua and Barbuda', 'ANT', 6, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Argentina', 'ARG', 7, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Armenia', 'ARM', 8, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Australia', 'AUS', 9, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Austria', 'AUT', 10, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Azerbaijan', 'AZE', 11, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bahamas', 'BAH', 12, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bangladesh', 'BAN', 13, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Barbados', 'BAR', 14, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Belgium', 'BEL', 15, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Benin', 'BEN', 16, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Burundi', 'BDI', 17, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bhutan', 'BHU', 18, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bosnia and Herzegovina', 'BIH', 19, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Belize', 'BIZ', 20, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Belarus', 'BLR', 21, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bolivia', 'BOL', 22, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Botswana', 'BOT', 23, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Brazil', 'BRA', 24, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bahrain', 'BRN', 25, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Brunei', 'BRU', 26, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Bulgaria', 'BUL', 27, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Burkina Faso', 'BUR', 28, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Central African Republic', 'CAF', 29, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cambodia', 'CAM', 30, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Canada', 'CAN', 31, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Chad', 'CHA', 32, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Congo', 'CGO', 33, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Chile', 'CHI', 34, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'China', 'CHN', 35, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cote d Ivoire', 'CIV', 36, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cameroon', 'CMR', 37, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Congo Congo Kinshasa', 'COD', 38, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Colombia', 'COL', 39, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Comoros', 'COM', 40, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cape Verde', 'CPV', 41, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Costa Rica', 'CRC', 42, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Croatia', 'CRO', 43, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cuba', 'CUB', 44, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Cyprus', 'CYP', 45, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Czech', 'CZE', 46, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Denmark', 'DEN', 47, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Djibouti', 'DJI', 48, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Dominica', 'DMA', 49, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Dominican Republic', 'DOM', 50, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Ecuador', 'ECU', 51, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Egypt', 'EGY', 52, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Eritrea', 'ERI', 53, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'El Salvador', 'ESA', 54, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Spain', 'ESP', 55, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Estonia', 'EST', 56, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Ethiopia', 'ETH', 57, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Fiji', 'FIJ', 58, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Finland', 'FIN', 59, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Micronesia', 'FSM', 60, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'France', 'FRA', 61, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Gabon', 'GAB', 62, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Gambia', 'GAM', 63, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'United Kingdom', 'GBR', 64, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Georgia', 'GEO', 65, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Equatorial Guinea', 'GEQ', 66, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Germany', 'GER', 67, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Ghana', 'GHA', 68, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Guinea Bissau', 'GNB', 69, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Greece', 'GRE', 70, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Grenada', 'GRN', 71, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Guatemala', 'GUA', 72, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Guinea', 'GUI', 73, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Guyana', 'GUY', 74, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Haiti', 'HAI', 75, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Honduras', 'HON', 76, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Hungary', 'HUN', 77, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'India', 'IND', 78, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Indonesia', 'INA', 79, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Iran', 'IRI', 80, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Ireland', 'IRL', 81, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Iraq', 'IRQ', 82, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Iceland', 'ISL', 83, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Israel', 'ISR', 84, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Italy', 'ITA', 85, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Jamaica', 'JAM', 86, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Jordan', 'JOR', 87, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Japan', 'JPN', 88, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Kazakhstan', 'KAZ', 89, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Kenya', 'KEN', 90, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Kyrgyzstan', 'KGZ', 91, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Kiribati', 'KIR', 92, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Korea', 'KOR', 93, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Saudi Arabia', 'KSA', 94, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Kuwait', 'KUW', 95, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Laos', 'LAO', 96, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Latvia', 'LAT', 97, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Libya', 'LBA', 98, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Liberia', 'LBR', 99, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Saint Lucia', 'LCA', 100, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Lesotho', 'LES', 101, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Lebanon', 'LIB', 102, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Liechtenstein', 'LIE', 103, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Lithuania', 'LTU', 104, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Luxembourg', 'LUX', 105, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Madagascar', 'MAD', 106, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Morocco', 'MAR', 107, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Malaysia', 'MAS', 108, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Malawi', 'MAW', 109, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Moldova', 'MDA', 110, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Maldives', 'MDV', 111, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mexico', 'MEX', 112, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mongolia', 'MGL', 113, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Macedonia', 'MKD', 114, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mali', 'MLI', 115, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Malta', 'MLT', 116, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Monaco', 'MON', 117, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mozambique', 'MOZ', 118, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mauritius', 'MRI', 119, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Mauritania', 'MTN', 120, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Myanmar', 'MYA', 121, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Namibia', 'NAM', 122, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Nepal', 'NEP', 123, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Nicaragua', 'NCA', 124, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Netherlands', 'NED', 125, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Nigeria', 'NGR', 126, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Niger', 'NIG', 127, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Norway', 'NOR', 128, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Nauru', 'NRU', 129, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'New Zealand', 'NZL', 130, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Oman', 'OMA', 131, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Pakistan', 'PAK', 132, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Panama', 'PAN', 133, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Paraguay', 'PAR', 134, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Peru', 'PER', 135, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Philippines', 'PHI', 136, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Palestine', 'PLE', 137, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Palau', 'PLW', 138, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Papua New Guinea', 'PNG', 139, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Poland', 'POL', 140, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Portugal', 'POR', 141, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Korea', 'PRK', 142, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Qatar', 'QAT', 143, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Marshall Islands', 'RMI', 144, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Romania', 'ROM', 145, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'South Africa', 'RSA', 146, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Russia', 'RUS', 147, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Rwanda', 'RWA', 148, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Samoa', 'SAM', 149, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Serbia Montenegro', 'SCG', 150, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Senegal', 'SEN', 151, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Seychelles', 'SEY', 152, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Singapore', 'SIN', 153, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Saint Kitts Nevis', 'SKN', 154, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Sierra Leone', 'SLE', 155, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Slovenia', 'SLO', 156, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'San Marino', 'SMR', 157, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Solomon Islands', 'SOL', 158, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Somalia', 'SOM', 159, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Sri Lanka', 'SRI', 160, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Sao Tome and Principe', 'STP', 161, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Sudan', 'SUD', 162, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Switzerland', 'SUI', 163, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Suriname', 'SUR', 164, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Slovakia', 'SVK', 165, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Swaziland', 'SWZ', 166, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Sweden', 'SWE', 167, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Syria', 'SYR', 168, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Tanzania', 'TAN', 169, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Tonga', 'TGA', 170, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Thailand', 'THA', 171, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Tajikistan', 'TJK', 172, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Turkmenistan', 'TKM', 173, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'East Timor', 'TLS', 174, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Togo', 'TOG', 175, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Trinidad and Tobago', 'TRI', 176, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Tunisia', 'TUN', 177, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Turkey', 'TUR', 178, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Tuvalu', 'TUV', 179, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'United Arab Emirates', 'UAE', 180, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Uganda', 'UGA', 181, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Ukraine', 'UKR', 182, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Uruguay', 'URU', 183, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'United States of America USA', 'USA', 184, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Uzbekistan', 'UZB', 185, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Vanuatu', 'VAN', 186, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Vatican City', 'VAT', 187, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Venezuela', 'VEN', 188, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Vietnam', 'VIE', 189, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Saint Vincent and the Grenadines', 'VIN', 190, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Yemen', 'YEM', 191, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Zambia', 'ZAM', 192, 1, now());

INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', 'Zimbabwe', 'ZIM', 193, 1, now());

	"""], sql_down=["""
	DELETE FROM parameter WHERE parameter_code='country';
	"""])