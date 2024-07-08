import io
import numpy as np
from PIL import Image
from moviepy.editor import VideoFileClip
from .image_caption import image_caption_genrator
from .bert_tokenizer import embeddings_generator

def image_to_base64(pil_image):
        byte_arr = io.BytesIO()
        pil_image.save(byte_arr, format='PNG')
        byte_arr = byte_arr.getvalue()
        return byte_arr

def encoder(video_file):
    clip = VideoFileClip(video_file)
    video = clip.without_audio()
    video_data = np.array(list(video.iter_frames()))

    blackness_percentage = lambda x: (np.sum(x <= 20) / (x.shape[0]*x.shape[1]*x.shape[2]))*100

    video_description = ""

    for frame_index in range(0, video_data.shape[0], 30):
        frame = video_data[frame_index]
        if(blackness_percentage(frame)>60):
            continue
        
        base64_image = image_to_base64(Image.fromarray(frame))
        result = image_caption_genrator(base64_image)
        
        try:
            video_description+=(result[0]['generated_text']+" ")
        except:
            continue

    embeddings = embeddings_generator(video_description)[0]
    
    return embeddings
         


    