import numpy as np
import matplotlib.pyplot as plt

xorFunction = [[1,1,1,0],
               [1,0,1,1],
               [0,1,1,1],
               [0,0,1,0]]
               
def net(weights,inputs):
    net = weights[0] * inputs[0] + weights[1] * inputs[1] + weights[2] * inputs[2]
    return net

def act(x):
    if x >= 0:
        return 1
    else:
        return 0

weight1 = [1.1,-.6,-1]
weight2 = [-.6,1.1,-1]
weight3 = [1,1,-1]

for j in range(4):
    inputs = xorFunction[j]
    h1out = act(net(weight1,inputs))
    h2out = act(net(weight2,inputs))
    print h1out,h2out
    out = h1out * weight3[0] + h2out * weight3[1] + weight3[2]
    print(act(out))

g1 = np.arange(-6,7,1)
g2 = np.arange(-6,7,1)

print g1
print g2

for x in g1:
    for y in g2:
        inputs = [g1[x],g2[y],1]
        h1out = act(net(weight1,inputs))
        h2out = act(net(weight2,inputs))
        out = h1out * weight3[0] + h2out * weight3[1] + weight3[2]
        if act(out) == 1:
            plt.plot(g1[x],g2[y],'bo',ms=10)
        else:
            plt.plot(g1[x],g2[y],'ro',ms=10)
            
plt.xlim(-7,7)
plt.ylim(-7,7)
plt.title("Results")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
