import os
import random
import logging

import torch
import numpy as np
from seqeval.metrics import precision_score,recall_score,f1_score

from transformers import BertConfig
from transformers import BertTokenizer

from model import JointBERT

BERT_CLASSES = (BertConfig,JointBERT,BertTokenizer)
MODEL_PATH_MAP = 'bert_chinese_base'

def get_intent_labels(args):
    return [label.strip() for label in open('data/train/train_intent_label.txt','r',encoding='utf-8')]

def get_intent_labels(args):
    return [label.strip() for label in open('data/train/train_slot_label.txt','r',encoding='utf-8')]

