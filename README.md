## Audio Generation from Ads
To convert the ads to audio, we first obtained a textual representation of the ads.
#### Source 1: Using Ad Image
The image associated with the ad was converted to a text which summarises product-centric information from the image with 
minimum repetition of information contained in the product title. We currently used cdex prompts to generate this caption. We can fine tune
existing image captioning models with bing ads data and the prompt label as a scalable approach
> The prompt used:
> ```
> sample prompt
> ```
