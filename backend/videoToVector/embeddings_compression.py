import torch
import torch.nn as nn
from video_encoder import encoder

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.decoder = nn.Sequential(
            nn.Linear(768, 300),
            nn.ReLU(),
            nn.Linear(300, 80),
            nn.ReLU(),
            nn.Linear(80, 9)  # Latent space
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
        return encoder_output, decoder_output

model = Autoencoder()
model.load_state_dict(torch.load("models\\autoencoder_model_new.pth", map_location=torch.device('cpu')))
model.eval()

higher_dimensional_embedding = encoder("..\\dataset\\sample5.mp4")

with torch.no_grad():
    lower_dimensional_encoding = model.decoder(higher_dimensional_embedding)

print(lower_dimensional_encoding)

