from matplotlib import pyplot as plt
labels=['Python','Java','C++','Ruby','PHP','JavaScript']
data=[95,85,65,80,95,90]
explode=[0.0,0.0,0.1,0.0,0.0,0.0]
plt.pie(data,labels=labels,explode=explode)
plt.show()