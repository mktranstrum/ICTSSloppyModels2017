import numpy as np
import pylab

sqrt = np.sqrt

fig_width = 8.0                         # inches  
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_height = fig_width*golden_mean      # height in inches
dpi = 600.0                             # Convert inch to pt

fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 24,
          'axes.titlesize': 24,
          'text.fontsize': 24,
          'legend.fontsize': 24,
          'xtick.labelsize': 24,
          'ytick.labelsize': 24,
          'text.usetex': False,
          'figure.figsize': fig_size}

pylab.rcParams.update(params)


pylab.figure(1)
pylab.clf()
leftmargin = 0.15
bottommargin = 0.175
rightmargin = 0.05
topmargin = 0.1
pylab.axes([leftmargin,bottommargin,1.0 - rightmargin-leftmargin,1.0 - topmargin-bottommargin])

## Generate Data & Make Plot


x = np.linspace(0,1,15)
np.random.seed(0)
y = x + np.random.randn(15)*0.1

pylab.errorbar(x, y, np.ones(15)*0.1, fmt="ro")
m = np.dot(x, y)/np.dot(x,x)
pylab.plot(x, m*x, "b-", linewidth = 2)
pylab.xlabel("x")
pylab.ylabel("y")
# pylab.subplots_adjust(wspace = 0.4, right = 1.0 - rightmargin, left = leftmargin, top = 1.0 - topmargin, bottom = bottommargin)

# Display or Save Plot

import sys
if len(sys.argv) > 1:
    pylab.savefig(sys.argv[1], dpi = dpi)
else:
    pylab.show()
