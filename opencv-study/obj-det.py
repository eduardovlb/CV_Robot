import cv2 as cv

classNames = []
classFile = 'coco.names'

# Abre o arquivo com as classes coloca as classes na lista classNames
with open (classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split()

configPath = 'ssd_mobilenet_v1_1_metadata_1.tflite'

print(classNames)