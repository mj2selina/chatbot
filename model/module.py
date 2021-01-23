import torch.nn as nn

def IntentClassifier(nn.Module):
    def __init__(self,input_dim,num_intent_labels,dropout_rate=0.0):
        super(IntentClassifier,self).__init__()
        self.dropout = nn.Dropout(dropout_rate)
        self.linear = nn.Linear(input_dim,num_intent_labels)
        self.softmax = nn.Softmax(dim=0)
    
    def forward(self,x):
        x = self.dropout(x)
        return self.linear(x)

def SlotClassifier(nn.Module):
    def __init__(self,input_dim,num_slot_labels,dropout_rate=0.0):
        super(SlotClassifier,self).__init__()
        self.dropout = nn.Dropout(dropout_rate)
        self.linear = nn.Linear(input_dim,num_slot_labels)
    
    def forward(self,x):
        x = self.dropout(x)
        return self.linear(x)