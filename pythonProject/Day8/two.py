import matplotlib.pyplot as plt
import numpy as np
movies=np.array(["Action","Romance","Comedy" ,"Drama"])
people=np.array([23,45,67,89])
plt.bar(movies,people)
plt.xlabel('Movie Genres')
plt.ylabel('Number of People')
plt.title('People\'s Preference for Different Movie Genres')
plt.show()