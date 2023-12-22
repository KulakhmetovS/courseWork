def ColorsInit(colors, spectral, size):
    for i in range(0, size):
        if colors[i] == 0:
            spectral[i] = 'white'
        elif colors[i] == 1:
            spectral[i] = 'red'
        elif colors[i] == 2:
            spectral[i] = 'yellow'
        elif colors[i] == 3:
            spectral[i] = 'green'
        elif colors[i] == 4:
            spectral[i] = 'blue'
        elif colors[i] == 5:
            spectral[i] = 'orange'
        elif colors[i] == 6:
            spectral[i] = 'magenta'
        elif colors[i] == 7:
            spectral[i] = 'cyan'
        elif colors[i] == 8:
            spectral[i] = 'pink'
        elif colors[i] == 9:
            spectral[i] = 'gray'
