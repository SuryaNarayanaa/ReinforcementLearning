import torch
import torch.nn as nn
class OurModule(nn.Module):
    def __init__(self , no_of_inps , no_of_classes , dropout_probability  =0.3) -> None:
        super(OurModule ,self).__init__()
        self.pipe = nn.Sequential(
            nn.Linear(no_of_inps ,5),
            nn.ReLU(),
            nn.Linear(5,20),
            nn.ReLU(),
            nn.Linear(20,no_of_classes),
            nn.Dropout(p = dropout_probability),
            nn.Softmax(dim =1 )
        )
    def forward(self  ,x):
        return self.pipe(x)
    
net = OurModule(no_of_inps=2, no_of_classes=3)
v = torch.FloatTensor([[2,4]])
out  = net(v)
print(net)
print(out)
if torch.cuda.is_available():
        print("Data from cuda: %s" % out.to('cuda'))