import os
from PIL import Image

print(os.getcwd())

CLASS_NAME = #A dictionary of class Names
# create a dictionary to map the class num to class name

folder_name = #Folder where the custom test images and the bounding boxes(In YOLO format) are present

for entry in os.scandir(folder_name):
  if entry.name.endswith("jpg"):

    # generate names for each file
    img_name = entry.name
    file_name = img_name[:-4]
    txt_name = file_name + ".txt"
    xml_name = file_name + ".xml"

    # get the size of the image
    im = Image.open(os.path.join(folder_name, img_name))
    img_size = im.size # (width, height)
    im.close()

    width = img_size[0]
    height = img_size[1]

    # create a list to store the info in .txt file
    # bbinfo = [[0,x,y,w,h], [...], ...[...]]
    bbinfo = []
    with open("folder_name/{0}".format(txt_name), 'r') as f:
      line = f.readline()
      while line != "":
        box = list(map(float, line.split()))
        box[0] = int(box[0])
        bbinfo.append(box)
        line = f.readline()

    # write the bbinfo to .xml file
    with open("/home/spc/darknet/Annotations/{0}".format(xml_name), 'a') as f: #The address for the Annotations Folder
      f.write("<annotation>\n")

      # write filename===========================================
      f.write("\t<filename>{0}</filename>\n".format(img_name))
      # =========================================================

      # write size===============================================
      f.write("\t<size>\n")
      #----------------------------------------------------------
      f.write("\t\t<width>{0}</width>\n".format(width))
      f.write("\t\t<height>{0}</height>\n".format(height))
      f.write("\t\t<depth>{0}</depth>\n".format(3))
      #----------------------------------------------------------
      f.write("\t</size>\n")
      #==========================================================

      # write object=============================================
      for box in bbinfo:
        f.write("\t<object>\n")
        # write bounding boxes-----------------------------------
        f.write("\t\t<name>{0}</name>\n".format(CLASS_NAME[box[0]]))
        f.write("\t\t<difficult>{0}</difficult>\n".format(0))
        f.write("\t\t<bndbox>\n")

        f.write("\t\t\t<xmin>{0}</xmin>\n".format(int((box[1]-0.5*box[3])*width)))
        f.write("\t\t\t<ymin>{0}</ymin>\n".format(int((box[2]-0.5*box[4])*height)))
        f.write("\t\t\t<xmax>{0}</xmax>\n".format(int((box[1]+0.5*box[3])*width)))
        f.write("\t\t\t<ymax>{0}</ymax>\n".format(int((box[2]+0.5*box[4])*height)))

        f.write("\t\t</bndbox>\n")
        #--------------------------------------------------------
        f.write("\t</object>\n")
      #==========================================================

      f.write("</annotation>")