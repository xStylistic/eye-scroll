import cv2
import mediapipe as mp

class EyeTracker:
    def __init__(self):
        # Initialize Mediapipe Face Mesh
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            min_detection_confidence=0.7,  # Adjust confidence threshold
            min_tracking_confidence=0.7
        )

    def process_frame(self, frame):
        print("Processing frame...")  # Debugging
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            print("Face landmarks detected.")  # Debugging
            for landmarks in results.multi_face_landmarks:
                # Extract eye landmarks
                left_eye_top = landmarks.landmark[386].y
                left_eye_bottom = landmarks.landmark[374].y
                right_eye_top = landmarks.landmark[159].y
                right_eye_bottom = landmarks.landmark[145].y

                # Use absolute values for ratios to avoid negative results
                left_eye_ratio = abs(left_eye_top - left_eye_bottom)
                right_eye_ratio = abs(right_eye_top - right_eye_bottom)

                print(
                    f"Left Eye Ratio: {left_eye_ratio}, Right Eye Ratio: {right_eye_ratio}")  # Debugging

                # Check if eyes are open (adjust thresholds if needed)
                eyes_open = left_eye_ratio > 0.005 and right_eye_ratio > 0.005
                print(f"Eyes Open: {eyes_open}")  # Debugging output
                return eyes_open

        print("No face landmarks detected.")  # Debugging
        return False
