import cv2
import mediapipe as mp

class EyeTracker:
    """
    up_threshold -> increase for smaller eyes
    down_threshold -> decrease for smaller eyes
    """
    def __init__(self, up_threshold=0.42, down_threshold=0.56):
        # Initialize MediaPipe Face Mesh with iris refinement enabled.
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
            refine_landmarks=True  # Iris landmarks
        )
        # Set thresholds for determining gaze direction.
        self.up_threshold = up_threshold
        self.down_threshold = down_threshold

    def process_frame(self, frame):
        print("Processing frame...")  # Debug
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                # Get eyelid landmarks for left and right eyes.
                left_eye_top = landmarks.landmark[386].y
                left_eye_bottom = landmarks.landmark[374].y
                right_eye_top = landmarks.landmark[159].y
                right_eye_bottom = landmarks.landmark[145].y

                # Check if eyes are open.
                left_eye_ratio = abs(left_eye_top - left_eye_bottom)
                right_eye_ratio = abs(right_eye_top - right_eye_bottom)
                eyes_open = left_eye_ratio > 0.005 and right_eye_ratio > 0.005
                if not eyes_open:
                    print("Eyes appear to be closed.")
                    return "none"

                # Calculate iris centers.
                right_iris_points = [landmarks.landmark[i] for i in range(468, 473)]
                right_iris_center_y = sum(pt.y for pt in right_iris_points) / len(right_iris_points)
                left_iris_points = [landmarks.landmark[i] for i in range(473, 478)]
                left_iris_center_y = sum(pt.y for pt in left_iris_points) / len(left_iris_points)

                # Calculate ratios for each eye.
                left_ratio = (left_iris_center_y - left_eye_top) / (left_eye_bottom - left_eye_top)
                right_ratio = (right_iris_center_y - right_eye_top) / (right_eye_bottom - right_eye_top)
                avg_ratio = (left_ratio + right_ratio) / 2

                print(f"Left ratio: {left_ratio:.3f}, Right ratio: {right_ratio:.3f}, Avg ratio: {avg_ratio:.3f}")

                # Determine gaze direction based on adjusted thresholds.
                if avg_ratio < self.up_threshold:
                    print("Detected gaze: down")
                    return "down"
                elif avg_ratio > self.down_threshold:
                    print("Detected gaze: up")
                    return "up"
                else:
                    print("Detected gaze: neutral")
                    return "none"

        print("No face landmarks detected.")
        return "none"
