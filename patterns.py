BLOCK = [
    [1, 1],
    [1, 1]
]

BEEHIVE = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

BLINKER = [
    [1, 1, 1]
]

TOAD = [
    [0, 1, 1, 1],
    [1, 1, 1, 0],
]

GLIDER = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

LWSPACESHIP = [
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1]
]

DOUBLE_LWSPACESHIP = [
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1]
]

DOUBLE_GLIDER = [
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1]
]



PATTERNS = {
    'block':BLOCK,
    'beehive':BEEHIVE,
    'blinker':BLINKER,
    'toad':TOAD,
    'glider':GLIDER,
    'lwspaceship':LWSPACESHIP,
    'double glider':DOUBLE_GLIDER,
    'double lwspaceship':DOUBLE_LWSPACESHIP
}