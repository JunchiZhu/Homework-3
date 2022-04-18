CREATE TABLE IF NOT EXISTS `experiences` (
`experience_id`     int(11)       NOT NULL AUTO_INCREMENT,
`position_id`       int(11)       NOT NULL,
`name`              varchar(100)  NOT NULL,
`description`       varchar(100)  NOT NULL,
`hyperlink`         varchar(100)  NOT NULL,
`start_date`        date          NOT NULL,
`end_date`          date          DEFAULT NULL,
PRIMARY KEY (`experience_id`),
FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

