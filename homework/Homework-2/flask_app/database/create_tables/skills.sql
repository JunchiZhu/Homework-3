CREATE TABLE IF NOT EXISTS `skills` (
`skill_id`          int(11)       NOT NULL AUTO_INCREMENT,
`experience_id`     int(11)       NOT NULL,
`name`              varchar(100)  NOT NULL,
`skill_level`       int(11)       NOT NULL,

PRIMARY KEY (`skill_id`),
FOREIGN KEY (experience_id) REFERENCES experiences(experience_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;