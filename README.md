# SwapPy
Auto Swap streams from multiple camera inputs.
Inspired from Bleed AI's Youtube Video: [Creating an AI Director for Automating a Multi-Camera Setup](https://www.youtube.com/watch?v=dfkgV7ZQA9g). 
Do consider to check for his latest course on Buliding Cutting Edge Computer Vision Applications [https://bit.ly/3dNwXvV](https://bit.ly/3dNwXvV)

Requirements:
1. OpenCV-Python
2. 3 WebCams
--- 
Running the code:
1. Install the packages in the requirements file with ``` pip install -r requirements.txt ```
2. Run the main.py code with ``` python main.py ```
--- 
Improvements:
- [ ] GUI for complete Application.
- [ ] Option for selecting number of Camera Inputs
- [ ] Selecting Primary camera
- [ ] Stream to OBS Studio or other 3rd party services(Zoom, Microsoft Teams, Google Meet, etc.)
- [ ] Adding Pinch-To-Zoom on face
- [ ] Stream Enhancement with Pre-Processing brightness and contrast to make potato webcams on laptops usable.
--- 
## NOTE
This code currently supports 3 cameras and will fail when run if number of cameras is less than 3 or greater.
