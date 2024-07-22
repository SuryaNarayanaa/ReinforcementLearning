import math
from tensorboardX import SummaryWriter


writer = SummaryWriter()
funcs = {"sin": math.sin, "cos": math.cos, "tan": math.tan}


for angle in range(-360 , 360):
    angle_rad  = angle*math.pi/180
    for name , func in funcs.items() :
        val = fun(angle_rad)
        writer.add_scaler(name , val , angle)
writer.close()