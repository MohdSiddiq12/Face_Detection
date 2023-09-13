<!DOCTYPE html>
<html>

<head>
  <style>
    h1 {
      font-size: 32px;
    }

    h2 {
      font-size: 24px;
    }

    h3 {
      font-size: 20px;
    }
  </style>
</head>

<body>
  <h1>Face Detection using OpenCV</h1>

  <h2>🛠️ Description</h2>
  <p>This project demonstrates face detection using the OpenCV library. It provides installation instructions, necessary imports, and version details.</p>

  <h2>⚙️ Installation</h2>
  <ol>
    <li><h3>Install Python:</h3> Ensure you have Python installed on your system. You can download it from the official Python website: <a href="https://www.python.org">python.org</a>.</li>
    <li><h3>Install OpenCV:</h3> OpenCV can be installed using pip, the Python package installer. Open your command prompt or terminal and run the following command:
      <pre>pip install opencv-python</pre>
      This command will install the latest version of OpenCV and its dependencies.
    </li>
  </ol>

  <h2>📦 Imports</h2>
  <p>To use this project's face detection functionality, import the following module in your Python code:</p>
  <pre><code>import cv2</code></pre>

  <h2>🚀 Usage</h2>
  <ol>
    <li><h3>Clone or Download the Source Code:</h3> Obtain the project source code by cloning the repository or downloading it to your local machine.</li>
    <li><h3>Create a New Python File:</h3> In your preferred Python IDE or text editor, create a new Python file for your face detection project.</li>
    <li><h3>Import the Necessary Module:</h3>
      <pre><code>import cv2</code></pre>
    </li>
    <li><h3>Load the Pre-trained Face Detection Model:</h3>
      <pre><code>face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')</code></pre>
    </li>
    <li><h3>Capture Video Frames:</h3>
      <pre><code>cap = cv2.VideoCapture(0)</code></pre>
    </li>
    <li><h3>Detect Faces:</h3>
      <pre><code>faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)</code></pre>
    </li>
    <li><h3>Process Detected Faces as Needed.</h3></li>
    <li><h3>Display Video Frames:</h3>
      <pre><code>cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()</code></pre>
    </li>
  </ol>

  <h2>📊 Versions</h2>
  <p>This project was developed using the following versions:</p>
  <ul>
    <li><h3>OpenCV version:</h3> 4.8.0.76</li>
    <li><h3>Python version:</h3> 3.9.13</li>
  </ul>

  <h2>🤖 Author</h2>
  <p>Mohammed Siddiq</p>
</body>

</html>
