-- 医院主数据表
CREATE TABLE hospital (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_code VARCHAR(60) DEFAULT NULL,  -- 医院编码
    hospital_name VARCHAR(60) DEFAULT NULL,  -- 医院名称
    province VARCHAR(150) DEFAULT NULL,       -- 省份
    city VARCHAR(150) DEFAULT NULL,           -- 城市
    address VARCHAR(100) DEFAULT NULL,        -- 地址
    level VARCHAR(30) DEFAULT NULL,           -- 医院级别
    grade VARCHAR(30) DEFAULT NULL,           -- 甲等这些
    hospital_type VARCHAR(50) DEFAULT NULL,   -- 公立，私立这些
    hospital_group_id INTEGER DEFAULT NULL,   -- 集团医院id
    del_flag INTEGER DEFAULT 0                 -- 0 未删除，1已删除
);

-- 集团医院
CREATE TABLE hospital_group (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_group_name VARCHAR(50) DEFAULT NULL,  -- 医院集团名称
    group_type VARCHAR(50) DEFAULT NULL,             -- 集团类别
    del_flag INTEGER DEFAULT 0                         -- 0 未删除，1已删除
);
