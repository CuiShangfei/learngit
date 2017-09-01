import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# 200为响应成功
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# 研究有关仓库的信息
repo_dicts = response_dict['items']
print('Number of items:', len(repo_dicts))

names, stars, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

# 可视化
# 改变默认主题颜色，偏蓝色
my_style = LS('#333366', base_style=LCS)
# 配置
my_config = pygal.Config()
# x轴的文字旋转45度
my_config.x_label_rotation = -45
# 隐藏左上角的图例
my_config.show_legend = False
# 标题字体大小
my_config.title_font_size = 24
# 副标签，包括x轴和y轴大部分
my_config.label_font_size = 14
# 主标签是y轴某数倍数，相当于一个特殊的刻度，让关键数据点更醒目
my_config.major_label_font_size = 18
# 限制字符为15个，超出的以...显示
my_config.truncate_label = 15
# 不显示y参考虚线
my_config.show_y_guides = False
# 图表宽度
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
