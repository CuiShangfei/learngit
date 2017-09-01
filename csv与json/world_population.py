import json

from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World

# 颜色相关
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle


def get_country_code(country_name):
    """
    根据国家名返回两位国别码
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


filename = 'population.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2015':
        country_name = pop_dict['Country Name']

        # 有些值是小数，先转为float再转为int
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 为了使颜色分层更加明显
cc_populations_1, cc_populations_2, cc_populations_3 = {}, {}, {}
for cc, population in cc_populations.items():
    if population < 10000000:
        cc_populations_1[cc] = population
    elif population < 1000000000:
        cc_populations_2[cc] = population
    else:
        cc_populations_3[cc] = population

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world = World(style=wm_style)
world.title = 'World Populations in 2015, By Country'
world.add('0-10m', cc_populations_1)
world.add('10m-1bn', cc_populations_2)
world.add('>1bn', cc_populations_3)
world.render_to_file('world_population_2015.svg')