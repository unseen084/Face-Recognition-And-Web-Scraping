# Face-Recognition-And-Web_Scraping
## Machine Learning on Face Recognition

For analyzing visual imagery, Convolutional Neural Network or CNN which is a class of feed forward artificial neural network has been successfully used. It can be used also in video analysis, natural language processing etc. Here we’ll talk about Machine Learning on Face Recognition.
Our goal is to identify a person’s face through deep neural network’s output. So, we have to train our model to identify features, patterns from a face. If we pass different images of a person, neural network should give output similar. But, if we pass totally different image, or new person’s image it will give “Unknown” as output.

### Facial Recognition


To apply machine learning on face recognition we can use a library named “face_recog”, which is mostly used for face recognition. It is python’s library, which uses dlib within it self. There are three major steps:
-	Detection 	  : Detect faces in frame/image
-	Landmark   : Finding features/patterns in frame/image
-	Comparison: Identification of faces in pictures through comparison
 
### Steps of recognition


First step is to prepare the image. We’ve to prepare or process the image first. Then we can get all necessary features from it.





![image1](https://user-images.githubusercontent.com/29349058/74098696-5474f880-4b45-11ea-8027-7970905e1a78.png)

Fig: Preparing image

After preparing the image, we’ll manipulate the image to get necessary information. For that, we need to get locations or outlines of a person’s mouth, eye, ear etc.

![image2](https://user-images.githubusercontent.com/29349058/74098709-72daf400-4b45-11ea-8f08-a5375c3ceefc.png) Input	
![image3](https://user-images.githubusercontent.com/29349058/74098715-7d958900-4b45-11ea-9871-ae6a6505865d.png) Output
										
			Fig: Extracting important features From image


After that, we analyze the features. Then we identify the image/face.

![image4](https://user-images.githubusercontent.com/29349058/74098726-956d0d00-4b45-11ea-87bc-011375c71080.png)
  
				Fig: Successful Identification
This is how we identify a face. This process or technique can be used for multiple faces in a single frame/photo/image. For that the list of inputs will be of  N, and the outputs will be of  N as well.

Basically by doing simple approach we can recognize who is in the image. Detection, Manipulation, Identification are the approaches. This clearly shows, how machine learning is taking over the world of artificial intelligence.

## Information Extraction


### Overview


After training the model we recognize face, but some faces can remain unrecognized. Because, those are new to our system. We label them as “Unknown”. Now, to recognize these Unknown faces, we can extract information about them from the “Internet”. Basically we do a google image search from our system.

### Image Search


Google has no API(Application Program Interface) regarding image search. So, we have done it manually.  
![image5](https://user-images.githubusercontent.com/29349058/74098743-c64d4200-4b45-11ea-97cc-7223b33903de.png)

					Fig: Google image search

### Using URL to Search


We have used URL(Uniform Resource Locator) of the image, to search on google. For that we have option to capture still image, then use that image to search on google. We couldn’t upload image directly to google image search, because google blocks it.

### Upload Image to Online Site


To use the URL, we have to create one. So, we uploaded the still image to a site called “Imgur”. It’s a image sharing site, where we can upload image. By this we get a link or URL of the image we want to search.

## Search on Google


We concat two links together, the google image search link and the image link. Then we make a request call through python’s ‘urllib’ module. 

url = 'http://www.images.google.com/searchbyimage?image_url=' + imagepath

Now we take this link and send request.
req = urllib.request.Request(googlepath, headers=headers)
resp = urllib.request.urlopen(req)
respData = resp.read()

To read the response data, we used resp.read() .


### Data Extraction


We got the response data, now we all need to do is extract our useful information. To do that, we need Web scraping tool. We have used Beautiful Soup to extract our useful information.

## Web Scraping


Web scraping is actually data extraction from web sites. Web scraping software uses Hypertext transfer protocol to access world wide web. We’ve used Web scraping tool, Beautiful Soup which is a package of python.

### Beautiful Soup


Beautiful soup is a package of python, which is used for parsing HTML and XML documents as we mentioned. From the parsed pages it creates a parse tree that extracts data from HTML. This is used for Web Scraping.
soup = BeautifulSoup(respData, "html.parser")
The response data we got previously is being parsed here by beautiful soup.

Now that we’ve parsed the data, we can find our necessary information.
![image6](https://user-images.githubusercontent.com/29349058/74098750-d2d19a80-4b45-11ea-8845-eb82daaf68fa.png)

				Fig: Google Image search result page
Here we’ve sent a request for a famous youtuber called Pewdiepie. Google sends us response, this page to be exact. So, from this page we need to extract our important information. When we search in google, google shows us the best guessed result. We need that information from there. To do that, we’ve to inspect that page to get our necessary information.
![image7](https://user-images.githubusercontent.com/29349058/74098772-07dded00-4b46-11ea-9558-0b900696ada8.png)
 
A division class named “r5a77d” has the information we need.
container = soup.find('div',class_='r5a77d')
We find that class through beautiful soup, and get our necessary information. For additional information, in similar way we find a division classed named “wwUB2c kno-fb-ctx” which has the information we need.
container = soup.find('div', class_='wwUB2c kno-fb-ctx')
This is how we get our necessary information through web scraping.

