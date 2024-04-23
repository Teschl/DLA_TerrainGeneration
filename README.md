# Terrain generation using Diffusion Limited Aggregation (DLA)

## functionality

### Diffusion Limited Aggregation

1. generate random crisp image
2. upscale crisp image
3. create blurry copy of upscaled image
4. add crisp version onto blurry image
5. repeat on generated crisp and blurry image

### random Aggregation

1. place pixel in middle of matrix
2. generate set amout of pixels:
    - place random pixel
    - move pixel util it touches another placed pixel

### "crisp" upscaling

1. keep track of which pixels got connected to which pixels
2. upscale by redrawing connections on bigger image

### add weights to each pixel

1. assign each pixel different weight
    - outside pixels get value 1
    - weight of pixel = max weight of a pixel downstream + 1
    - to avoid peaks that are too high, use 1-1/(1+h)

### linear interpolation (smooth upscaling)

1. find equivalent position in original image
2. find distance to 4 nearest pixels
3. new pixel value = sum of near pixels, weighted by distance

### convolution (blurring)

1. create empty image of same size
2. each pixel gets average of 4 sorrounding pixels

### sum crisp and blurry image

1. add crisp image onto blurry image
2. keep crisp version for further dla steps
3. blur blurry image further and upscale it
