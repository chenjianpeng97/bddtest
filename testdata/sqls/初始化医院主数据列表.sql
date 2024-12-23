-- 插入医院集团数据
INSERT INTO `hospital_group` (`hospital_group_name`, `group_type`, `del_flag`) VALUES
('华东医院集团', '公立', 0),
('仁爱医院集团', '私立', 0),
('安康医疗集团', '公立', 0),
('阳光医院集团', '私立', 0);

-- 插入医院数据
INSERT INTO `hospital` (`hospital_code`, `hospital_name`, `province`, `city`, `address`, `level`, `grade`, `hospital_type`, `hospital_group_id`, `del_flag`) VALUES
('H001', '上海市第一人民医院', '上海', '上海', '上海市黄浦区人民大道1号', '三级甲等', '甲等', '公立', 1, 0),
('H002', '南京市中心医院', '江苏', '南京', '南京市中山路1号', '三级乙等', '乙等', '公立', 1, 0),
('H003', '深圳市人民医院', '广东', '深圳', '深圳市福田区深南大道2号', '三级甲等', '甲等', '公立', 1, 0),
('H004', '广州中医药大学附属医院', '广东', '广州', '广州市天河路5号', '三级甲等', '甲等', '公立', 1, 0),
('H005', '北京私立医院', '北京', '北京', '北京市朝阳区建国路3号', '二级甲等', '甲等', '私立', 2, 0),
('H006', '仁爱妇产医院', '深圳', '深圳', '深圳市南山区科技园北区4号', '二级乙等', '乙等', '私立', 2, 0),
('H007', '昌平医院', '北京', '北京', '北京市昌平区建设路23号', '二级甲等', '甲等', '公立', 3, 0),
('H008', '尊医医院', '上海', '上海', '上海市浦东新区绿地大道6号', '二级乙等', '乙等', '私立', 4, 0),
('H009', '西安交通大学医院', '陕西', '西安', '西安市长安南路3号', '三级甲等', '甲等', '公立', 3, 0),
('H010', '福州儿童医院', '福建', '福州', '福州市鼓楼区东街口1号', '三级甲等', '甲等', '公立', 4, 0);
