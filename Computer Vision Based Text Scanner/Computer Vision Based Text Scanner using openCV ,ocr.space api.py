#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[3]:


# Import the libraries 
import cv2
import numpy as np
import requests
import io
import json
from tkinter.filedialog import *

# select img from directory
a=Tk()
filename = askopenfilename()
a.mainloop()
img = cv2.imread(filename)
height, width, _ = img.shape

# Cutting image
# roi = img[0: height, 400: width]
roi = img

# Ocr (Optical Character Recognition )
url_api = "https://api.ocr.space/parse/image" #The Free OCR API S
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

#The function is going to send the image to the server and in return we’re going to get the response from the server.
result = requests.post(url_api,
              files = {filename: file_bytes},
              data = {"apikey": "helloworld",
                      "language": "eng"})
# Read result
#  extract the content of result, then we convert the content into a dictionary.
result = result.content.decode()
result = json.loads(result)    #Result contains the text read from the OCR engine 
#from the result let’s extract only the text 
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)

cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




