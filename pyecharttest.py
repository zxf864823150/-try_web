from pyecharts.charts import Geo,Map
#old pyecharts is more easy,here is 1.0
# Geo.add_coordinate(geo,119.21,22.4)
# indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安',
#           '郑州', '重庆', '长沙','某地']
# values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1,
#           1.31, 3.92, 4.47, 2.40, 3.60,4.99]
# map = Map("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
#           background_color='#40a59')
geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#40a59')
geo.add_coordinate("某地",112.0,45.66)
geo.add_coordinate_json("my_json")
indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安',
          '郑州', '重庆', '长沙','某地','金陵学校大门']
values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1,
          1.31, 3.92, 4.47, 2.40, 3.60,4.99,5.88]
# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("空气质量评分", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[0, 5],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
# map.add("空气质量评分", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[0, 5],
#         visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./data/04-05空气质量评分.png")
# map.render(path="./data/04-06空气质量评分.html")