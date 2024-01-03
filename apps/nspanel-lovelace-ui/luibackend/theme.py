
from helper import rgb_dec565

import apis

default_screensaver_color_mapping = {
    #"item":            "color in decimal RGB565 (0-65535)"
    "background":       "0",
    "time":             "65535",
    "timeAMPM":         "65535",
    "date":             "65535",
    "tMainText":        "65535",
    "tForecast1":       "65535",
    "tForecast2":       "65535",
    "tForecast3":       "65535",
    "tForecast4":       "65535",
    "tForecast1Val":    "65535",
    "tForecast2Val":    "65535",
    "tForecast3Val":    "65535",
    "tForecast4Val":    "65535",
    "bar":              "65535",
    "tMainTextAlt2":    "65535",
    "tTimeAdd":         "65535"
}

def get_screensaver_color_output(theme, state=None):
    color_output = "color"
    for key in default_screensaver_color_mapping:
        color_output += f"~{map_color(key=key, theme=theme)}"
    return color_output

def map_color(key, theme):
    config_color = default_screensaver_color_mapping[key]
    # Use theme color if set and is a string
    if key in theme:
        theme_value = theme[key]
        if isinstance(theme_value, str):
            # Get the state and split it into an array of three numbers
            state_value = apis.ha_api.get_state(theme_value)
            apis.ha_api.log(state_value)
            theme_value = [int(x) for x in state_value.split(',')]
        apis.ha_api.log(theme_value)
        config_color = rgb_dec565(theme_value)
    return config_color
