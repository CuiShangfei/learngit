from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """
    根据国家名返回两位国别码
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家就返回None
    return None

# print(get_country_code('China'))
# print(get_country_code('china'))
