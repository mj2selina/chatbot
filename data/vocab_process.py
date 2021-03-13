import os 
'''
def vocab_process(input_file_path,out_file_path):
    train_label = set()
    #vocab = set()
    with open(input_file_path,'r') as f:
        for line in f:
            line = line.strip().replace(' ','').replace('\n','').replace('\t','')
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
    
    

vocab_process('./data/all_intent_label.txt','./data/intent_label.txt')
vocab_process('./data/all_slot_label.txt','./data/slot_label.txt')'''
intent_label_list = []
slot_label_list = []

def read_file(path,label,intent_flag=True):
    with open(path,'r') as f:
        for line in f:
            line = line.strip().replace('\n','')
            line = line.replace(' - ','-')
            print(line)
            if ' ' in line:
                lbl = line.split(' ')
                lbl = [l.replace(' ','') for l in lbl]
                for l in lbl:
                    if l == 'O':
                        continue
                    else:
                        label.append(l)
                #label.extend(lbl)
                #lbl = ['+'.join(l.split('+')[:-1]) if intent_flag is True else l for l in lbl]
                #for l in lbl:
                #    label.append(l)
                #label.extend(lbl)
            else:
                label.append(line.replace('\n',''))
            #break
    return label
print(os.getcwd())
#l = read_file('data/train/intent_label.txt',intent_label_list)
#print(l[:3])
#intent_label_list.extend(read_file('data/train/intent_label.txt',intent_label_list))
#intent_label_list.extend(read_file('data/test/intent_label.txt',intent_label_list))
#intent_label_list.extend(read_file('data/dev/intent_label.txt',intent_label_list))
slot_label_list.extend(read_file('data/train/slot_label.txt',slot_label_list))
slot_label_list.extend(read_file('data/test/slot_label.txt',slot_label_list))
slot_label_list.extend(read_file('data/dev/slot_label.txt',slot_label_list))
#intent_label_list = list(set(intent_label_list))
slot_label_list = list(set(slot_label_list))
#with open('data/all_intent_label.txt','w') as f:
#    f.write('\n'.join(intent_label_list))
with open('data/all_slot_label.txt','w') as f:
    f.write('\n'.join(slot_label_list))
#intent_duplic = []
#intent = []
'''
with open('data/all_intent_label.txt','r') as f:
    for line in f:
        intent.append(line.replace('\n',''))
print(len(intent))
print(len(list(set(intent))))
with open('data/all_intent_label.txt','w') as f:
    f.write('\n'.join(list(set(intent))))'''