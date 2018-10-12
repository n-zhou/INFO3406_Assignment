import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pad = pd.read_csv('latest_query_with_gross.csv', names = ['word', 'gross', 'valence', 'arousal', 'dominance'], header = 0, encoding = "ISO-8859-1")
for i in pad.valence.values:
    i = round(i,2)
for i in pad.arousal.values:
    i = round(i,2)
for i in pad.dominance.values:
    i = round(i,2)
row_count = sum(1 for row in pad)

# You typically want your plot to be ~1.33x wider than tall.
# Common sizes: (10, 7  .5) and (12, 9)
plt.figure(figsize=(10, 50))
#plt.subplots_adjust(hspace = 0.6)
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
plt.ylabel("Gross Revenue in Billions")

ax1.set_title("Average Valence vs Revenue")


#ax1.hist(list(pad.valence.values), color="#7B9E89", bins=100)

plt.scatter(pad.valence.values, pad.gross.values, color="#7B9E89")

ax2 = plt.subplot(312)

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()


plt.xlabel("Average Arousal of Title")
plt.ylabel("Gross Revenue in Billions")

ax2.set_title("Average Arousal vs Revenue")

#ax2.hist(list(pad.arousal.values), color="#23B5D3", bins=100)
ax2.scatter(pad.arousal.values, pad.gross.values, color="#23B5D3")

ax3 = plt.subplot(313)

ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax3.get_xaxis().tick_bottom()
ax3.get_yaxis().tick_left()

plt.xlabel("Average Dominance of Title")
plt.ylabel("Gross Revenue in Billions")

ax3.set_title("Average Dominance vs Revenue")



#ax3.hist(list(pad.dominance.values), color="#FF9F1C", bins=100)

ax3.scatter(pad.dominance.values, pad.gross.values, color="#FF9F1C")

plt.savefig("vad_by_gross.png", bbox_inches="tight");

plt.show()
