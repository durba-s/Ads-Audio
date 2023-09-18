import torch
from transformers import BarkModel, AutoProcessor
import scipy
import argparse
from datasets import load_dataset
from bark import SAMPLE_RATE, generate_audio, preload_models
#from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
#from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
'''
Parse the command line options
* -file : FileName", help (Input Text file name) : Default "example.txt"
* -ofile : FileNameOutput (Output Audio file name) : Default "audio_sample.wav"
'''
def parse_arguments(args):

    filename = "example.txt"
    if args.FileName:
        filename = args.FileName

    outputFile = "audio_sample.wav"
    if args.FileNameOutput:
        outputFile = args.FileNameOutput
    return filename, outputFile

def read_text_file(filename):
    try:
        with open(filename,"r") as f:
            text = f.read()
    except FileNotFoundError:
            msg = "Sorry, the file "+ filename + "does not exist, using default text"
            print(msg) 
            text = "This is a sample text."
    return text
'''
converting text to audio
'''
def text_to_audio_file(text, device, filename = "audio_sample.wav"):

    model = BarkModel.from_pretrained("suno/bark").to(device)
    processor = AutoProcessor.from_pretrained("suno/bark")
    inputs = processor(text, voice_preset="v2/en_speaker_9")
    model = model.to(device)
    speech_output = model.generate(**inputs.to(device))
    sampling_rate = model.generation_config.sample_rate   
    scipy.io.wavfile.write(filename, rate=sampling_rate, data=speech_output[0].cpu().numpy())
    
    '''
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

    inputs = processor(text=text, return_tensors="pt")

    # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    scipy.io.wavfile.write(filename, rate=16000, data=speech.numpy())

    '''
    '''
    preload_models()
    #, history_prompt="v2/en_speaker_9"
    audio_array = generate_audio(text)
    scipy.io.wavfile.write(filename,  SAMPLE_RATE, audio_array)
    '''

    print('done')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", "--FileName", help = "Text file name")
    parser.add_argument("-ofile", "--FileNameOutput", help = "Audio file name")
    
    args = parser.parse_args()       
    filename, outputFile = parse_arguments(args)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(device)
    file_text = read_text_file(filename)
    print("Summary: ", file_text)
    #summary_text[0]['summary_text']
    text_to_audio_file(text = file_text,device = device,filename = outputFile)



if __name__ == '__main__':
    main()
