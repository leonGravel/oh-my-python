CREATE TABLE `water_notice` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT 'id主键',
  `notice_title` varchar(255) DEFAULT NULL COMMENT '标题',
  `notice_time` datetime DEFAULT NULL COMMENT '发布时间',
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;