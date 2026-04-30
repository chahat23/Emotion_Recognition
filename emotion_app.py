import cv2
from deepface import DeepFace
import speech_recognition as sr

# ---------------- VOICE TRIGGER ----------------
def wait_for_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say 'start' to capture emotion...")
        r.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio).lower()
                print("You said:", text)

                if "start" in text:
                    print("✅ Trigger detected!")
                    return True

            except:
                print("❌ Could not understand, try again...")

# ---------------- EMOTION DETECTION ----------------
def detect_emotion():
    cap = cv2.VideoCapture(0)

    print("📸 Capturing emotion... Press ESC to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            emotion = result[0]['dominant_emotion']

            cv2.putText(frame, f"Emotion: {emotion}",
                        (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        except Exception as e:
            cv2.putText(frame, "Detecting...",
                        (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    wait_for_voice()   # wait until user says "start"
    detect_emotion()