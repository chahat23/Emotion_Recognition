# Intelligent Emotion Recognition System

A Python-based facial emotion recognition project that uses deep
learning and computer vision to classify emotions from facial images.
The repository also includes a webcam-based emotion detection script
with a voice trigger.

## Features

-   **Image-based emotion prediction:** Upload a facial image through a
    Streamlit interface.
-   **Deep learning inference:** Uses a trained Keras/TensorFlow model
    to predict an emotion.
-   **Webcam emotion detection:** Uses OpenCV and DeepFace to analyze
    facial expressions from a live camera feed.
-   **Voice trigger:** The webcam workflow waits for the user to say
    **"start"** before beginning emotion detection.
-   **Model training script:** Includes `train.py` for training the
    image-classification model.

## Technologies Used

-   Python
-   TensorFlow / Keras
-   Streamlit
-   OpenCV
-   NumPy
-   Pillow
-   DeepFace
-   SpeechRecognition

## Repository Structure

``` text
Emotion_Recognition/
├── app.py                 # Streamlit app for image upload and prediction
├── emotion_app.py         # Voice-triggered webcam emotion detection
├── train.py               # Model training script
├── emotion_model.h5       # Trained model file included in the repository
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

> **Model path note:** `app.py` currently loads
> `model/emotion_model.h5`, while the repository lists
> `emotion_model.h5` in the root directory. Either create a `model/`
> folder and place the model inside it, or update the load path in
> `app.py` to `load_model("emotion_model.h5")`.

## Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/chahat23/Emotion_Recognition.git
cd Emotion_Recognition
```

### 2. Create and activate a virtual environment (recommended)

**Windows (Command Prompt):**

``` bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

The repository's `requirements.txt` is currently empty, so install the
packages needed for the application:

``` bash
python -m pip install --upgrade pip
pip install streamlit tensorflow opencv-python numpy pillow deepface SpeechRecognition
```

The voice-triggered webcam script may also require an audio input
backend supported by your operating system (for example, PyAudio) and a
working microphone. TensorFlow and DeepFace dependencies can vary by
Python and operating-system version.

## How to Run

### Option 1: Predict emotion from an image

Run the Streamlit application:

``` bash
streamlit run app.py
```

Then open the local URL shown in the terminal, upload a JPG, JPEG, or
PNG facial image, and view the predicted emotion.

The current `app.py` defines these output labels:

-   Angry
-   Disgust
-   Fear
-   Happy
-   Sad
-   Surprise
-   Neutral

The model and labels must use the same class order for predictions to be
interpreted correctly.

### Option 2: Detect emotion using a webcam

Run:

``` bash
python emotion_app.py
```

When prompted, say **"start"**. The script then opens the webcam and
displays the dominant emotion detected by DeepFace. Press **Esc** to
close the webcam window.

This mode requires a working webcam and microphone, and speech
recognition may require internet access.

### Option 3: Train the model

The repository includes a training script:

``` bash
python train.py
```

Before running it, check `train.py` to confirm the expected dataset
directory, image format, training settings, and output model path.
Ensure the required dataset is available locally. Training output and
model filenames depend on the script's configuration.

## How It Works

1.  The application receives a facial image or webcam frame.
2.  The image-based Streamlit flow converts the uploaded image to
    grayscale, resizes it to **48 × 48** pixels, normalizes pixel
    values, and reshapes it for model input.
3.  The trained model produces class scores for the supported emotion
    labels.
4.  The application selects the class with the highest score and
    displays it.
5.  In the webcam workflow, DeepFace analyzes frames and overlays the
    dominant emotion on the video feed.

## Important Notes and Limitations

-   Emotion predictions are estimates from facial-expression patterns;
    they do **not** reliably establish a person's actual feelings,
    intentions, or mental state.
-   Results can be affected by lighting, pose, occlusion, image quality,
    and differences between training data and real-world images.
-   Make sure the model architecture, input preprocessing, and label
    order match the model used for training.
-   The model file is tracked in this repository. If you retrain the
    model, verify the new model's output path and update the application
    path if necessary.
-   Webcam and microphone access must be enabled on the machine running
    the application.

## Future Improvements

-   Add evaluation metrics such as accuracy, precision, recall, and a
    confusion matrix.
-   Display prediction confidence scores.
-   Improve error handling for missing models, unreadable images, and
    unavailable cameras.
-   Add example screenshots and a sample dataset setup guide.
-   Pin tested dependency versions in `requirements.txt` for more
    reproducible installation.

## Contributing

Contributions and suggestions are welcome. You can open an issue to
report a bug or propose an improvement, or submit a pull request.

## License

No license file was visible in the repository when this README was
prepared. Add a `LICENSE` file if you intend to specify how others may
use, modify, and distribute this project.

## Author

**Chahat Gupta**

GitHub: [@chahat23](https://github.com/chahat23)

## Project Repository

<https://github.com/chahat23/Emotion_Recognition>
