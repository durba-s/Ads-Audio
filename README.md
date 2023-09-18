# Voice for Bing Ad Images

## Conversion to text
To convert the ads to audio, we first obtained a textual representation of the ads.
#### Source 1: Using Ad Image
The image associated with the ad was converted to a text which summarises product-centric information from the image with 
combined with the information contained in the product title. We currently used cdex prompts to generate this caption. We can fine tune
existing image captioning models with bing ads images data and the prompt caption as a scalable approach
> Cdex:
> GPTV prompt
> ```
>CONFIG:temperature:0.1|max_tokens:150|top_p:0.8|frequency_penalty:1|presence_penalty:1|auto_expand:false|token_list:|stop_list:|
>PROMPT: IMAGE:#Image#
> Write a 3-line summary of the image describing product attributes by combining details in the title #Title#. Describe only the product in the title #Title# > and not other objects in the image. Extract new information from the image about the product.
> Provide your answer inside <Summary></Summary> tag.
>----------------------------------------------------------------------------------------------------
> #D1#
> $Extract "Summary" => Summary
>----------------------------------------------------------------------------------------------------
> ```
#### Source 2: Using Ad Description
We summarised the ads description present associated with the offer in the ads corpus. We currently used cdex prompts to generate this caption. We can fine tune existing text summarising models to generate product-centric summaries with bing ads data and the prompt summary as a scalable approach.
> Cdex:
> GPTV prompt
> ```
>CONFIG:temperature:0.1|max_tokens:200|top_p:0.8|frequency_penalty:1|presence_penalty:1|auto_expand:false|token_list:|stop_list:|
>PROMPT: Given the product description #description# generate summarized text in 3 lines.
> Provide your answer inside <Summary></Summary> tag.
>----------------------------------------------------------------------------------------------------
> #D1#
> $Extract "Summary" => Summary
>----------------------------------------------------------------------------------------------------
> ```
#### Source 3: Using the Description in the landing page
We summarised the ads description present in the landing page of the ad (under the product details/ product description section the page). We currently used cdex prompts to generate this caption. We can fine tune existing text summarising models to generate product-centric summaries with bing ads data and the prompt summary as a scalable approach.
> Cdex:
> GPTV prompt
> ```
>CONFIG:temperature:0.1|max_tokens:200|top_p:0.8|frequency_penalty:1|presence_penalty:1|auto_expand:false|token_list:|stop_list:|
>PROMPT: Given the product description #description# generate summarized text in 3 lines.
> Provide your answer inside <Summary></Summary> tag.
>----------------------------------------------------------------------------------------------------
> #D1#
> $Extract "Summary" => Summary
>----------------------------------------------------------------------------------------------------
> ```

## Text to speech
We used the [bark text to speech model](https://github.com/suno-ai/bark) to generate audio from the text.
```py
python  text-to-speech.py -file "input-file.txt" -ofile "output-file.wav"
```
* -file: specify input file name (the text file containing text to be converted to audio)
* -ofile: specify the name of the audio output file

## Demo
The project can be integrated with the screen reader to provide the audio experience to the user. In order to simulate the experience, we embedded the audio files in the search results html page.
