import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def embeddings_generator(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, 
                       truncation=True, padding='max_length')
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    embeddings = outputs.last_hidden_state[:,0,:]

    return embeddings
