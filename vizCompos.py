"""
vizCompos.py

SHSH <herho@terpmail.umd.edu>
01/16/23
"""

# import libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp

plt.rcParams["figure.dpi"] = 400
plt.style.use('ggplot')

# data wrangling
df = pd.read_csv("./processed_data/muna_low_pass_stack.csv")

# plot
plt.plot(df["year"], df["median"], color="green");
plt.fill_between(df["year"], df["lower"], df["upper"], alpha=.25, color='green')
plt.xlabel('time (year)', size=16);
plt.ylabel('$\delta^{18}$O anomaly', size=16);
plt.tight_layout();
plt.savefig('./figs/munaStack.png');

# KS test
df = df.set_index("year")
pre = df.loc["1680":"1850"]["median"].dropna().to_numpy()
post = df.loc["1850":]["median"].dropna().to_numpy()

test = ks_2samp(pre, post)

print("Dmax = ", round(test[0],3))
print("\n")
print("p-value = ", round(test[1], 3))

## sort data
x1 = np.sort(pre)
x2 = np.sort(post)

## calculate CDF values
y1 = 1. * np.arange(len(pre)) / (len(pre) - 1)
y2 = 1. * np.arange(len(post)) / (len(post) - 1)

## plot CDFs
plt.plot(x1, y1, label= 'pre-industrial');
plt.plot(x2,y2, label='post-industrial');
plt.ylabel('CDFs', fontsize='16');
plt.xlabel(r'$\delta^{18}{O_c}$ anomaly', fontsize=16);
plt.legend();
plt.savefig('./figs/cdfs.png')