CREATE DATABASE `ihome` DEFAULT CHARACTER SET utf8;

use ihome;

CREATE TABLE ih_user_profile (
    up_user_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    up_name varchar(32) NOT NULL COMMENT '昵称',
    up_mobile char(11) NOT NULL COMMENT '手机号',
    up_passwd varchar(64) NOT NULL COMMENT '密码',
    up_real_name varchar(32) NULL COMMENT '真实姓名',
    up_id_card varchar(20) NULL COMMENT '身份证号',
    up_avatar varchar(128) NULL COMMENT '用户头像',
    up_admin tinyint NOT NULL DEFAULT '0' COMMENT '是否是管理员，0-不是，1-是',
    up_utime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    up_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (up_user_id),
    UNIQUE (up_name),
    UNIQUE (up_mobile)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8 COMMENT='用户信息表';