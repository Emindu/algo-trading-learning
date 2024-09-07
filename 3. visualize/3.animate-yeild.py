import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from openbb import obb
obb.user.preferences.output_type = "dataframe"


maturities = ["3m", "6m", "1y", "2y", "3y", "5y", "7y", "10y", "30y"]

data = obb.fixedincome.government.treasury_rates(
    start_date="1985-01-01",
    provider="federal_reserve",
).dropna(how="all").drop(columns=["month_1", "year_20"])
data.columns = maturities

data["inverted"] = data["30y"] < data["3m"]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot([], [])

ax.set_xlim(0, 8)
ax.set_ylim(0, 20)

ax.set_xticks(range(9))
ax.set_yticks([2, 4, 6, 8, 10, 12, 14, 16, 18])

ax.set_xticklabels(maturities)
ax.set_yticklabels([2, 4, 6, 8, 10, 12, 14, 16, 18])

ax.yaxis.set_label_position("left")

ax.yaxis.tick_left()
plt.ylabel("Yield (%)")
plt.xlabel("Time to maturity")
plt.title("U.S. Treasury Bond Yield Curve")

def init_func():
    line.set_data([], [])
    return line,

def animate(i):
    x = range(0, len(maturities))
    y = data[maturities].iloc[i]*100
    dt_ = data.index[i].strftime("%Y-%m-%d")
    if data.inverted.iloc[i]:
        line.set_color("r")
    else:
        line.set_color("y")
    line.set_data(x, y)
    plt.title(f"U.S. Treasury Bond Yield Curve ({dt_})")
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    init_func=init_func,
    frames=len(data.index),
    interval=250,
    blit=True
)

plt.show()
