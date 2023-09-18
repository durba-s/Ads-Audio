# Audio Generation from Ads
## Conversion to text
To convert the ads to audio, we first obtained a textual representation of the ads.
#### Source 1: Using Ad Image
The image associated with the ad was converted to a text which summarises product-centric information from the image with 
minimum repetition of information contained in the product title. We currently used cdex prompts to generate this caption. We can fine tune
existing image captioning models with bing ads images data and the prompt caption as a scalable approach
> The cdex prompt used was:
> ```
> sample prompt
> ```
#### Source 2: Using the Description in the landing page
We summarised the ads description present in the landing page of the ad. We currently used cdex prompts to generate this caption. We can fine tune
existing text summarising models to generate product-centric summaries with bing ads data and the prompt summary as a scalable approach.
> The cdex prompt used was:
> ```
> sample prompt
> ```
#### Source 3: Using Ad Description
We summarised the ads description present associated with the ad in our corpus. We currently used cdex prompts to generate this caption. We can fine tune
existing text summarising models to generate product-centric summaries with bing ads data and the prompt summary as a scalable approach.
> The cdex prompt used was:
> ```
> sample prompt
> ```

## Text to speech
We used the [bark text to speech model](https://github.com/suno-ai/bark) to generate audio from the text.
