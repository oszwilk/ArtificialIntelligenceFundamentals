import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf 
from PIL import Image
import os 
from sklearn.model_selection import train_test_split 
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout

data = []
labels = []
cur_path = os.path.join(os.getcwd(), 'data')
classes = len( os.listdir(os.path.join(cur_path, 'train')) )  #43 
imgSize = 30
for i in range(classes):
    path = os.path.join(cur_path,'train', str(i)) 
    images = os.listdir(path) 
    for a in images:
        try: 
            image = Image.open(path + "\\"+ a) 
            image = image.resize((imgSize,imgSize)) 
            image = np.array(image) 
            data.append(image) 
            labels.append(i) 
        except:
            print("Error loading image") 
            
data = np.array(data)
labels = np.array(labels)

print(data.shape, labels.shape)
#Splitting training and testing dataset
X_t1, X_t2, y_t1, y_t2 = train_test_split(data, labels, test_size=0.2, random_state=42)
print(X_t1.shape, X_t2.shape, y_t1.shape, y_t2.shape)

#Converting the labels into one hot encoding
y_t1 = to_categorical(y_t1, classes)
y_t2 = to_categorical(y_t2, classes)

#Building the model
model = Sequential() # sequelntial otrzymuje dane kiedy wywołujemy funkcję celu na niej
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=X_t1.shape[1:]))   #X_train.shape[1:]))
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.25))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(classes, activation='softmax'))
#Compilation of the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()
eps = 2#15
anc = model.fit(X_t1, y_t1, batch_size=32, epochs=eps, validation_data=(X_t2, y_t2))

#plotting graphs for accuracy
plt.figure(0)
plt.plot(anc.history['accuracy'], label='training accuracy')
plt.plot(anc.history['val_accuracy'], label='val accuracy')
plt.title('Accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()
plt.figure(1)
plt.plot(anc.history['loss'], label='training loss')
plt.plot(anc.history['val_loss'], label='val loss')
plt.title('Loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

model.save('traffic_classifier.h5')


#testing accuracy on test dataset
from sklearn.metrics import accuracy_score
y_test = pd.read_csv('data//labels.csv')
labels = y_test["ClassId"].values
imgs = y_test["ClassId"].values
data=[]

path = os. path.join(cur_path,'test', str(i)) 

# for img in imgs:
#    #image = Image.open(img)
#    image = Image.open(path + "\\"+ img) 
#    image = image.resize((imgSize,imgSize))
#    data.append(np.array(image))
   
   
labels2 = []
for i in range(classes):
    path = os. path.join(cur_path,'test', str(i)) 
    images = os.listdir(path) 
    imageName = os.listdir(path)[0]
    
    image = Image.open(path + "\\"+ imageName) 
    image = image.resize((imgSize,imgSize)) 
    image = np.array(image) 
    data.append(image)

    # for a in images:
    #     try: 
    #         image = Image.open(path + "\\"+ a) 
    #         image = image.resize((imgSize,imgSize)) 
    #         image = np.array(image) 
    #         data.append(image)
    #         labels2.append(i)
    #     except:
    #         print("Error loading image") 
   
   
X_test=np.array(data)
pred = model.predict_classes(X_test)
#pred = (model.predict(X_test) > 0.5).astype("int32") #tensorflow 2.5++

#Accuracy with the test data
from sklearn.metrics import accuracy_score
print(accuracy_score(list(range(0, classes)), pred))

#https://www.analyticsvidhya.com/blog/2021/12/traffic-signs-recognition-using-cnn-and-keras-in-python/