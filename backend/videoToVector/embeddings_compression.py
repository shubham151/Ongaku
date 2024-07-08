import torch
import torch.nn as nn
from .video_encoder import encoder

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.decoder = nn.Sequential(
            nn.Linear(768, 300),
            nn.ReLU(),
            nn.Linear(300, 80),
            nn.ReLU(),
            nn.Linear(80, 12)
        )
        self.decoder_op1 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op2 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op3 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op4 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op5 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op6 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op7 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op8 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.decoder_op9 = nn.Sequential(
            nn.Linear(12,1)
        )
        self.encoder = nn.Sequential(
            nn.Linear(9, 80),
            nn.ReLU(),
            nn.Linear(80, 300),
            nn.ReLU(),
            nn.Linear(300, 768)
        )

    def forward(self, x):
        encoder_output = self.encoder(x)
        decoder_output = self.decoder(encoder_output)
        op1 = self.decoder_op1(decoder_output)
        op2 = self.decoder_op2(decoder_output)
        op3 = self.decoder_op3(decoder_output)
        op4 = self.decoder_op4(decoder_output)
        op5 = self.decoder_op5(decoder_output)
        op6 = self.decoder_op6(decoder_output)
        op7 = self.decoder_op7(decoder_output)
        op8 = self.decoder_op8(decoder_output)
        op9 = self.decoder_op9(decoder_output)
        return encoder_output, decoder_output, op1, op2, op3, op4, op5, op6, op7, op8, op9
    
def final_vector(file):
    model = Autoencoder()
    model.load_state_dict(torch.load("models/autoencoder_model_retrained.pth", map_location=torch.device('cpu')))
    model.eval()

    higher_dimensional_embedding = encoder(file)

    lower_dimensional_encoding = []

    with torch.no_grad():
        lower_dimensional_encoding.append(model.decoder_op1(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op2(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op3(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op4(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op5(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op6(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op7(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op8(model.decoder(higher_dimensional_embedding)))
        lower_dimensional_encoding.append(model.decoder_op9(model.decoder(higher_dimensional_embedding)))

    return lower_dimensional_encoding
