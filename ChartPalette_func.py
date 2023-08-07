#!/usr/bin/env python3
'''
@subject: Chart Palette
@date: 11/08/2023
@author: Luca Sanfilippo
@pythonVers: 3.9.6
'''

import seaborn as sns

def Chart_palette():
    '''
    This function sets the seaborn palette with the chosen colors
    '''
    colors = {
        # Primary palette
        
        'Chart_Green' : "#86BC25",
        'Green_2' : "#C4D600",
        'Green_4' : "#43B02A",
        'Green_6' : "#046A38",
        'Green_7' : "#2C5234",
        'Teal_5' : "#0097A9",
        'Blue_2' : "#62B5E5",
        'Blue_3' : "#00A3E0",
        'Blue_4' : "#0076A8",
        'Blue_6' : "#012169",
        'Cool_Gray_2' : "#D0D0CE",
        'Cool_Gray_4' : "#BBBCBC",
        'Cool_Gray_7' : "#97999B",
        'Cool_Gray_9' : "#75787B",
        'Cool_Gray_11' : "#53565A",
        'Black' : "#000000",

        # Secondary palette
        'Teal_1' : "#DDEFE8",
        'Teal_6' : "#007680",
        'Blue_7' : "#041E42",
        'Green_5' : "#009A44",
        'Teal_4' : "#00ABAB",
        'Blue_5' : "#005587",
        'Teal_2' : "#9DD4CF",
        'Teal_7' : "#004F59",
        'Cool_Gray_6' : "#A7A8AA",
        'Green_1' : "#E3E48D",
        'Teal_3' : "#6FC2B4",
        'Blue_1' : "#A0DCFF",
        'Cool_Gray_10' : "#63666A",
        
        # Additional functional colors (not to be used)
        # "Red": "#DA291C",
        # "Orange": "#ED8B00",
        # "Yellow": "#FFCD00"
    }
    Chart_colours = list(colors.values())
    ChartPalette = sns.set_palette(sns.color_palette(Chart_colours))


#%% Test:
# Chart_palette() # Just call the function to get the palette







