from flask import Flask, render_template, request, jsonify
#import h5py
import os
import scipy.io as io
import PIL.Image as Image
import numpy as np
#import os
#import glob
from matplotlib import pyplot as plt
import scipy
import re
#import json
from matplotlib import cm as c
from model import CSRNet
import torch
from torchvision import datasets, transforms

transform=transforms.Compose([
                      transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225]),
                  ])

#creating model
model = CSRNet()
model.cpu()
#loading the trained weights
checkpoint = torch.load('0model_best.pth.tar', map_location=lambda storage, location: storage)
model.load_state_dict(checkpoint['state_dict'])
#valid image types
valid_types = ['image/jpeg', '/image/png']

#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'static/img'
@app.route('/')
def index():
	#render out pre-built HTML file right on the index page
        return render_template('index.html')
	#return "<!DOCTYPE html><html><head><title>Crowd Counting App</title></head><body><p>this is a test page</p></body></html>"

@app.route('/predict/', methods=['GET','POST'])
def predict():
# 	if not 'file' in request.files:
#             return jsonify({'error': 'no file'}), 400
#         # Image info
#         img_file = request.files.get('file')
#         img_name = img_file.filename
#         mimetype = img_file.content_type
#         # Return an error if not a valid mimetype
#         if not mimetype in valid_types:
#             return jsonify({'error': 'bad-type'})

	img = request.get_data()
	#print(img)
	#convertImage(img)
	#img = Image.open('output.png')
	#img = img.resize((1000,450),Image.ANTIALIAS)
	#img = transform(img.convert('RGB')).cpu()
	#output = model(img.unsqueeze(0))
	#output = int(output.detach().cpu().sum().numpy()))
	#temp = np.asarray(output.detach().cpu().reshape(output.detach().cpu().shape[2],output.detach().cpu().shape[3]))
	#plt.imshow(temp,cmap = c.jet)
	#plt.show()
	return img


	
	
#if __name__=='___main__':
port = int(os.environ.get('PORT', 8080))
app.run(host='127.0.0.1', port=port)
