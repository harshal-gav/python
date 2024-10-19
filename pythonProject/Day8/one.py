import matplotlib.pyplot as plt
import numpy as np
over=np.array([5,10,15,20])
runs_scored=np.array([34,23,78,8])

plt.plot(over,runs_scored,c='r',marker='o',linestyle='dashed')
plt.xlabel('Overs')
plt.ylabel('Runs Scored')
plt.title('Total Runs Scored at the End of Each Over')

plt.show()