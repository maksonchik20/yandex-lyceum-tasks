# если вершина черная, то так
black = []
white = []
white.extend([black, black])
black.extend([white, white, white])
wb_tree = black
# Если вершина белая:
# white = []
# black = []
# black.extend([white, white])
# white.extend([black, black, black])
# wb_tree = white