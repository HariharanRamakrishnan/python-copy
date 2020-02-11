
import os
import shutil
src='E:\hari\photos'
dst='E:\hari\songs1'
shutil.rmtree(dst)
os.mkdir(dst)
shutil.rmtree(dst)
shutil.copytree(src,dst)