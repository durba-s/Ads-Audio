import torch
from transformers import AutoProcessor, pipeline
import scipy
import argparse
'''
Parse the command line options
* -lmax : SummaryMaxLength (Max summary length) : Default 100
* -lmin : SummaryMinLength (Min summary length) : Default 30
* -file : FileName", help (Input Text file name) : Default "example.txt"
* -ofile : FileNameOutput (Output Audio file name) : Default "summarised_text.wav"
'''
def parse_arguments(args):
    min_length = 30
    max_length = 100

    if args.SummaryMaxLength:
        max_length = int(args.SummaryMaxLength)
    if args.SummaryMinLength:
        min_length = int(args.SummaryMinLength)

    filename = "example.txt"
    if args.FileName:
        filename = args.FileName

    outputFile = "summarised_text.wav"
    if args.FileNameOutput:
        outputFile = args.FileNameOutput
    return filename, outputFile, min_length, max_length

'''
summarise the text file
'''
def summarise_text_file(filename, min_length, max_length):
    try:
        with open(filename,"r") as f:
            text = f.read()
    except FileNotFoundError:
            msg = "Sorry, the file "+ filename + "does not exist, using default text"
            print(msg) 
            text = "This is a sample text to be summarised."
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary_text = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary_text

'''
convert text to audio
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
main
'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lmax", "--SummaryMaxLength", help = "Max summary length")
    parser.add_argument("-lmin", "--SummaryMinLength", help = "Min summary length")
    parser.add_argument("-file", "--FileName", help = "Text file name")
    parser.add_argument("-ofile", "--FileNameOutput", help = "Audio file name")
    
    args = parser.parse_args()       
    filename, outputFile, min_length, max_length = parse_arguments(args)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(device)

    summary_text = summarise_text_file(filename, min_length, max_length)
    print("Summary: ", summary_text)

    text_to_audio_file(summary_text[0]['summary_text'],device, outputFile)



if __name__ == '__main__':
    main()

