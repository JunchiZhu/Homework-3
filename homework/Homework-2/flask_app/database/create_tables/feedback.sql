CREATE TABLE IF NOT EXISTS `feedback` (
`comment_id`     int(11)       NOT NULL AUTO_INCREMENT,
`name`           varchar(100)  NOT NULL,
`email`          varchar(100)  DEFAULT NULL,
`comment`        varchar(100)  DEFAULT NULL,
PRIMARY KEY  (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;