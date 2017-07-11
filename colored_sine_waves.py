from bokeh.io import output_file
from bokeh.plotting import figure, show
import numpy as np

output_file(__file__.replace('.py', '.html'))
fig = figure()

t = np.linspace(0, 2 * np.pi, 1000)
A = np.linspace(0, 2 * np.pi, 100)

# generate circular colormap
rgb_phase = np.linspace(0, 2 * np.pi, 3, endpoint=False)


def rgb(angle):
    r, g, b = (255 * (np.cos(angle + rgb_phase) + 1) / 2).astype(int)
    return r, g, b


for a in A:

    x = a * np.sin(t)

    # create a circular colormap
    fig.line(t, x, color=rgb(a))

show(fig)
