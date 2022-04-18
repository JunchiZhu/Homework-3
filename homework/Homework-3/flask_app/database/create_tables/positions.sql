CREATE TABLE IF NOT EXISTS `positions` (
`position_id`        int(11)       NOT NULL AUTO_INCREMENT,
`inst_id`            int(11)       NOT NULL,
`title`              varchar(100)  NOT NULL,
`responsibilities`   varchar(500)  NOT NULL,
`start_date`         date          NOT NULL,
`end_date`           date          DEFAULT NULL,
PRIMARY KEY (`position_id`),
FOREIGN KEY (inst_id) REFERENCES institutions(inst_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;