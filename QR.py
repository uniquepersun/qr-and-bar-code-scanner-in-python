import cv2
import pyzbar.pyzbar as pyzbar

def decode(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  barcodes = pyzbar.decode(gray)

  for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    barcode_type = barcode.type

    (x, y, w, h) = barcode.rect

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    text = f"{barcode_type}: {data}"
    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

  return img

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()

  if ret:
    frame = decode(frame)

    cv2.imshow('frame', frame)
  else:
    print("failed to get frame.")

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()