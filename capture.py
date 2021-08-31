import cv2

# print(cv2.__version__)
capture = cv2.VideoCapture(0)
# 비디오 출력 클래스, 내장 또는 외장 카메라에서 정보 가져오는 기능
# 보통 노트북의 경우 내장카메라, 장치번호는 보통 0
# 외장은 1~n 순차적 할당
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 카메라 속성 세팅 메서드

while cv2.waitKey(33) < 0:
    # 반복문을 통해 카메라에서 프레임 지속적으로 가져온다.
    # waitkey로 키입력 대기 33은 지연시간(delay)
    # !=ord('q')로 사용시 q입력될때 while문 종료
    ret, frame = capture.read()
    # ret은 카메라 상태 저장, 정상 작동시 True 반환
    # frame현재 시점 프레임 저장
    cv2.imshow("VideoFrame", frame)
    # 윈도우 창의 제목, 이미지 할당

capture.release()
# 카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows()
# 모든 윈도우 창 제거 함수
# cv2.destroyWindow(winname) 사용시 특정 윈도우 창만 제거
