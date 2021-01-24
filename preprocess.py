import json

def read_json(path):
    data = ''
    with open(path,'r',encoding='UTF-8') as f:
        for line in f:
            data += line
    s = json.loads(data)
    return s

def process_data(data_list):
    intent_dict = {'sent':[],'label':[]}
    slot_dict = {'sent':[],'label':[]}
    idx = 0
    for data in data_list:
        turns = data['turns']
        #print(turns)
        sent = ''
        intent_label = []
        for turn in turns:
            role = turn['role']
            if role == 'usr':
                utterance = turn['utterance'].replace(' ','').replace('\t','').replace('\n','')
                dialog_act = turn['dialog_act']
                intent_label = []
                slot_label = [''] * len(utterance)
                slot_signal = {}
                for act in dialog_act:
                    intent_label.append('+'.join(act))
                    slot_key = '+'.join(act[:-1])
                    if len(act[-1]) > 0 and act[-1] != 'none':
                        if act[-1] not in utterance:
                            idx += 1
                            continue
                        index = utterance.index(act[-1])
                        for i in range(len(act[-1])):
                            slot_label[index + i] = ('B+' + slot_key) if i == 0 else ('I+' + slot_key)
                for i in range(len(slot_label)):
                    if len(slot_label[i]) == 0:
                        slot_label[i] = 'O'
                intent_dict['sent'].append(utterance)
                intent_dict['label'].append(intent_label)
                slot_dict['sent'].append(utterance)
                slot_dict['label'].append(slot_label)
    #print(len(data_list))
    #print(idx)
    return intent_dict,slot_dict

def write_to_file(data,file_name):
    with open(file_name,'w',encoding='utf-8') as f:
        for item in data:
            f.write(' '.join(item) + '\n')

def preprocess():
    train_path = 'data/readabe_train_data.json'
    test_path = 'data/readabe_test_data.json'
    val_path = 'data/readabe_val_data.json'
    train_list = read_json(train_path)
    test_list = read_json(test_path)
    val_list = read_json(val_path)
    train_intent_dict, train_slot_dict = process_data(train_list)
    test_intent_dict, test_slot_dict = process_data(test_list)
    val_intent_dict, val_slot_dict = process_data(val_list)
    print(len(train_intent_dict['sent']))
    print(len(train_intent_dict['label']))
    print(len(train_slot_dict['label']))
    print(len(test_intent_dict['sent']))
    print(len(test_intent_dict['label']))
    print(len(test_slot_dict['label']))
    print(len(val_intent_dict['sent']))
    print(len(val_intent_dict['label']))
    print(len(val_slot_dict['label']))
    write_to_file(train_intent_dict['sent'],'data/train/train_data.txt')
    write_to_file(train_intent_dict['label'],'data/train/train_intent_label.txt')
    write_to_file(train_slot_dict['label'],'data/train/train_slot_label.txt')
    write_to_file(test_intent_dict['sent'],'data/test/test_data.txt')
    write_to_file(test_intent_dict['label'],'data/test/test_intent_label.txt')
    write_to_file(test_slot_dict['label'],'data/test/test_slot_label.txt')
    write_to_file(val_intent_dict['sent'],'data/val/val_data.txt')
    write_to_file(val_intent_dict['label'],'data/val/val_intent_label.txt')
    write_to_file(val_slot_dict['label'],'data/val/val_slot_label.txt')


preprocess()