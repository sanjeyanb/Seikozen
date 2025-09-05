import cv2
import numpy as np
from scipy import signal

def chebyshev_filter(img, cutoff, ripple, order):
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    u = np.arange(rows) - crow
    v = np.arange(cols) - ccol
    u, v = np.meshgrid(u, v)
    D = np.sqrt(u ** 2 + v ** 2)
    D_normalized = D / (rows / 2)
    b, a = signal.iirfilter(order, cutoff, rp=ripple, btype='low', analog=False, ftype='cheby1', fs=1)
    H = signal.filtfilt(b, a, D_normalized.flatten())
    H = H.reshape((rows, cols))
    img_dft = np.fft.fft2(img)
    img_dft_shift = np.fft.fftshift(img_dft)
    filtered_dft_shift = img_dft_shift * H
    filtered_img_dft = np.fft.ifftshift(filtered_dft_shift)
    filtered_img = np.fft.ifft2(filtered_img_dft)
    filtered_img = np.abs(filtered_img)
    return np.uint8(filtered_img)

cap = cv2.VideoCapture(0)
min_contour_area = 1500

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 240])
    upper_white = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    white_regions = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(white_regions, cv2.COLOR_BGR2GRAY)
    cutoff = 0.1
    ripple = 5
    order = 4
    chebyshev_filtered = chebyshev_filter(gray, cutoff, ripple, order)
    blurred = cv2.GaussianBlur(chebyshev_filtered, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    kernel = np.ones((3, 3), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)
    contours, _ = cv2.findContours(edges_dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_shapes = []
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) >= 4:
                detected_shapes.append(approx)
    for shape in detected_shapes:
        cv2.drawContours(frame, [shape], -1, (0, 255, 0), 3)
        for point in shape:
            x, y = point[0]
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
        for i in range(len(shape)):
            start_point = tuple(shape[i][0])
            end_point = tuple(shape[(i + 1) % len(shape)][0])
            cv2.line(frame, start_point, end_point, (255, 0, 0), 2)
    cv2.imshow('Shape Detection with Enhanced Filtering', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
