
# Title
import numpy as np
import idx2numpy
import matplotlib.pyplot as plt


X3d = idx2numpy.convert_from_file (
   "E:\Courses\LocalRepo\Digit_Recogniser\\t10k-images-idx3-ubyte"
)
y = idx2numpy.convert_from_file (
   "E:\Courses\LocalRepo\Digit_Recogniser\\t10k-labels-idx1-ubyte"
)


#reshape 3d matrix to 2d
# e.g: [10, 3, 3] --> [10, 9]
X_u = X3d.reshape(len(X3d), -1)
# each pixel is in range of 0-255 --> 0-1
X = X_u/255 #data normalisation

#random initial weights
W = InitRandWeights(X.shape[1], 25, y.max()+1)
accuracy = []
loss = []
#learning rate
alpha = 7
i=0

#main loop
print("Training ... ")
while(i < 60): 
   
	W, AllCost = NN_Model(X, y, W, 10, alpha)
	prd = Predict(X, W)
	accuracy.append(np.mean(prd==y))
	loss.append(np.mean(AllCost))
 
	print("Accuracy: ", accuracy[-1])
	print("Loss:     ", loss[-1])
 
	if accuracy[-1] > np.float(0.95):
		break
	elif accuracy[-1] > np.float(0.90):
		alpha = 1
	elif accuracy[-1] > np.float(0.80):
		alpha = 2
	elif accuracy[-1] > np.float(0.75):
		alpha = 2.5
	elif accuracy[-1] > np.float(0.65):
		alpha = 3
	elif accuracy[-1] >= np.float(0.5):
		alpha = 4
	i+=1
	
#plot accuracy and loss values with each iteration
fig = plt.figure()
for i in range(1, len(loss)):
  plt.plot([i-1, i], [accuracy[i-1], accuracy[i]], color='blue',
           label='Accuracy'
          )
  plt.plot([i-1, i], [loss[i-1], loss[i]], color='red', label='Loss')
  plt.pause(0.1)
  plt.legend(['Accuracy', 'Loss'])
plt.show()

