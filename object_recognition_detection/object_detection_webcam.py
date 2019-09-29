

import numpy as np
import os
import six.moves.urllib as urllib
#import sys
import tarfile
import tensorflow as tf
#import zipfile

#from collections import defaultdict
#from io import StringIO
#from matplotlib import pyplot as plt
#from PIL import Image
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util
import pyscreenshot as ImageGrab
import time

# # Model preparation 
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_CKPT` to point to a new .pb file.  
# By default we use an "SSD with Mobilenet" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.

# What model to download.
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90


### Download Model
if not os.path.exists(MODEL_NAME + '/frozen_inference_graph.pb'):
	print ('Downloading the model')
	opener = urllib.request.URLopener()
	opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
	tar_file = tarfile.open(MODEL_FILE)
	for file in tar_file.getmembers():
	  file_name = os.path.basename(file.name)
	  if 'frozen_inference_graph.pb' in file_name:
	    tar_file.extract(file, os.getcwd()) 
	print ('Download complete')
else:
	print ('Model already exists')

# ## Load a (frozen) Tensorflow model into memory.

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')


# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)



# Running the tensorflow session
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
   last_time = time.time()
   n=0
   while (True):
      image_np = np.array(ImageGrab.grab(bbox=(0,150,800,740)))
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
      image_np_expanded = np.expand_dims(image_np, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      # Each box represents a part of the image where a particular object was detected.
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      # Each score represent how level of confidence for each of the objects.
      # Score is shown on the result image, together with the class label.
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')
      # Actual detection.
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})
      # Visualization of the results of a detection.
      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)

      #for i in category_index:
          #print(category_index[i]["name"])
      #print("\n\n")
      
      
      
      listaDistanciasinicial = []
      for i,b in enumerate(boxes[0]):
          objName = classes[0][i]
          
          if objName == 1  or objName == 28 or objName == 31  or objName == 44 or objName == 47 or objName == 62 or objName == 64 or objName == 65 or objName == 65 or objName == 67 or objName == 72 or objName == 64 or objName == 73 or objName == 78 or objName == 82  :
              if scores[0][i] >= 0.5:
                mid_x = (boxes[0][i][1]+boxes[0][i][3])/2
                mid_y = (boxes[0][i][0]+boxes[0][i][2])/2
                apx_distance = round(((1 - (boxes[0][i][3] - boxes[0][i][1]))**4),1)
                cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x*800),int(mid_y*450)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    
                if apx_distance <=0.5:
                  if mid_x > 0.3 and mid_x < 0.7:
                    cv2.putText(image_np, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)
                listaDistanciasinicial.append(apx_distance)
      
        
        
      #toma la lista con todas las distancias de los objetos actualesy=
      #y crea una nueva lista con las 2 distancias menores
      listaDistancias=listaDistanciasinicial  
      lista2Menores=[]
      if len(listaDistancias)<=2:
          lista2Menores=listaDistancias
      
      else:
          tmplista=[]        
          
          menor = listaDistancias[0]
          flag=0
          while flag<2: 
              for valor in listaDistancias:
                  if valor < menor:
                      menor = valor
                  else:
                      tmplista.append(valor)
              listaDistancias=tmplista
              tmplista=[]
              lista2Menores.append(menor)
              menor = listaDistancias[0]
              flag+=1
      cont=0
      for i in lista2Menores:
          lista2Menores[cont]=int(i*30)
          cont+=1
        
      if len(lista2Menores) == 0:
          lista2Menores.append(30)
          lista2Menores.append(30)
      if len(lista2Menores) == 1:
          lista2Menores.append(30)
      print(lista2Menores)
      print(listaDistanciasinicial,"\n")
      
      #Crear Txt con las dos distancias menores
      file = open("testfile.txt","w") 
      stringlist=str(lista2Menores)
      file.write(stringlist.replace(' ', '')) 
      file.close() 
      
      
      #print('loop took {} seconds'.format(time.time()-last_time))
      last_time = time.time()
      cv2.imshow('window',cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
      if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          #cap.release()
          break


