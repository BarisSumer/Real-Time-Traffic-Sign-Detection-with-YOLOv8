import cv2
from ultralytics import YOLO

# Eğitilen modeli yükle (Dosya yolunun doğru olduğundan emin ol)
model = YOLO('best.pt')

# Webcam başlat
cap = cv2.VideoCapture(0)

# Kamera ayarları (İsteğe bağlı - çözünürlük artırma)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("🚀 Traffic Sign Detection System Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Tahmin yap (Confidence threshold: 0.5)
    results = model.predict(source=frame, conf=0.5, save=False, show=False, verbose=False)

    # Sonuçları kare üzerine çiz
    res_plotted = results[0].plot()

    # Görüntüyü göster
    cv2.imshow('YOLOv8 Traffic Sign Detection', res_plotted)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()