import os 

def vocab_process(input_file_path,out_file_path):
    train_label  = set()
    #vocab = set()
    with open(input_file_path,'r') as f:
        for line in f:
            line = line.strip()
            line = line.replace('\n','')
            line = line.replace(' - ','-')
            if ' ' in line:
                lbl = line.split(' ')
                for l in lbl:
                    train_label.add(l)
            else:
                train_label.add(line.replace('\n',''))
    additional_tokens = ['UNK']
    for token in additional_tokens:
        train_label.add(token)
    train_label = sorted(list(train_label))
    with open(out_file_path,'w') as f:
        f.write('\n'.join(train_label))
    
    

vocab_process('./data/train/train_intent_label.txt','./data/intent_label.txt')
vocab_process('./data/train/train_slot_label.txt','./data/slot_label.txt')
    