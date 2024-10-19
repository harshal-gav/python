import matplotlib.pyplot as plt
import numpy as np
lang=np.array(['java','c++','python','c','c#'])
per=np.array([34,56,78,12,23])
plt.pie(per,labels=lang,autopct='%0.1f%%')
plt.title('Popularity of Programming Languages')

plt.axis('equal')
plt.legend()
plt.show()