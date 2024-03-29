import requests
from PIL import Image
from sklearn.cluster import KMeans
import io
import numpy as np

# Credit to https://github.com/davidkrantz/Colorfy/blob/master/spotify_background_color.py#L131, thank you!
# adapted to remove histogram and plot and get image from url
# given the album cover, it will return the most dominant color in #hex
# this to recreate spotify app function, where every album page has a different background color, given the album cover
# color selected is seen on the 'library/<album id>' header background on the webapp

def best_color(url):
    
    try:
        def rgb_to_hex(r,g,b):
            hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b).upper()
            return hex_color

        def colorfulness(r, g, b):
            rg = np.absolute(r - g)
            yb = np.absolute(0.5 * (r + g) - b)
            rg_mean, rg_std = (np.mean(rg), np.std(rg))
            yb_mean, yb_std = (np.mean(yb), np.std(yb))
            std_root = np.sqrt((rg_std ** 2) + (yb_std ** 2))
            mean_root = np.sqrt((rg_mean ** 2) + (yb_mean ** 2))
            return std_root + (0.3 * mean_root)
        
        color_tol = 10 
        response = requests.get(url) 
        img = Image.open(io.BytesIO(response.content))
        img = img.resize((100, 100))
        pixels = list(img.getdata())
        clt = KMeans(n_clusters=8)
        clt.fit(pixels)
        centroids = clt.cluster_centers_
        colorfulness = [colorfulness(color[0], color[1], color[2]) for color in centroids]
        max_colorful = np.max(colorfulness)

        if max_colorful < color_tol:        
            best_color = [230, 230, 230]
        else:        
            best_color = centroids[np.argmax(colorfulness)]
    
    except Exception as e:
        return rgb_to_hex(230, 230, 230)     
    else:
        final_color = [int(best_color[0]), int(best_color[1]), int(best_color[2])]       
        return rgb_to_hex(final_color[0], final_color[1], final_color[2])
    

    