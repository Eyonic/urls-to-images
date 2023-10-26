#urls-to-images

Summary: I received a large list of URLs and downloaded all the images in JPG format, creating 200x200 thumbnails for each of them. 
Additionally, I also converted the images to WebP format for my website. 

so if you run the python script you will get folders called:jpg,thumbs-jpg,thumbs-webp,webp <br>
<br>
jpg:              image_name.jpg <br>
thumbs-jpg:       image_name.jpg <br>
thumbs-webp:      image_name.webp <br>
webp:             image_name.webp<br>

<br>
Note that this works for images of various sizes like 400x400, 600x600, 800x800, and so on.<br>


1.Makes an HTTP GET request to each URL to fetch image data.<br>

2.Converts the image data into both JPG and WebP formats.<br>

3.Creates 200x200 pixel thumbnails in both JPG and WebP formats.<br>

4.Saves the images and thumbnails in specified directories.<br>

5.Handles errors, including failed HTTP requests and exceptions during the process.<br><br>

Example usage is provided with a list of URLs, and directories for storing the images and thumbnails are created if they don't already exist. The program automates the process of downloading, converting, and saving images, making it easy to work with image data from URLs.<br>

<a href="https://www.buymeacoffee.com/Eyonic" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>