import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pad = pd.read_csv('final dataset.csv', names = ['word', 'valence', 'arousal', 'dominance'], header = 0)
for i in pad.valence.values:
    i = round(i,2)
for i in pad.arousal.values:
    i = round(i,2)
for i in pad.dominance.values:
    i = round(i,2)
row_count = sum(1 for row in pad)

# You typically want your plot to be ~1.33x wider than tall.
# Common sizes: (10, 7.5) and (12, 9)
plt.figure(figsize=(10, 9))
plt.subplots_adjust(hspace = 0.6)
plt.style.use('seaborn')

# Remove the plot frame lines. They are unnecessary chartjunk.
ax1 = plt.subplot(311)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()


plt.xlabel("Average Valence of Title")
plt.ylabel("Matching Titles")

ax1.set_title("Movie Titles by Valence")


ax1.hist(list(pad.valence.values), color="#7B9E89", bins=100)


ax2 = plt.subplot(312)

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()


plt.xlabel("Average Arousal of Title")
plt.ylabel("Matching Titles")

ax2.set_title("Movie Titles by Arousal")

ax2.hist(list(pad.arousal.values), color="#23B5D3", bins=100)

ax3 = plt.subplot(313)

ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax3.get_xaxis().tick_bottom()
ax3.get_yaxis().tick_left()

plt.xlabel("Average Dominance of Title")
plt.ylabel("Matching Titles")

ax3.set_title("Movie Titles by Dominance")


# Plot the histogram. Note that all I'm passing here is a list of numbers.
# matplotlib automatically counts and bins the frequencies for us.
# "#3F5D7D" is the nice dark blue color.
# Make sure the data is sorted into enough bins so you can see the distribution.
ax3.hist(list(pad.dominance.values), color="#FF9F1C", bins=100)

plt.savefig("Movie_titles_by_vad.png", bbox_inches="tight");

plt.show()
