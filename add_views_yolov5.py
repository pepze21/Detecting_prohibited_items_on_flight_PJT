# views.py와 같은 경로(django project directory)에 yolov5 clone
# git clone https://github.com/ultralytics/yolov5.git
# sudo chmod 777 -R ~/yolov5

from yolov5 import detect

def post(self, *args, **kwargs):
    img_id = kwargs.get("id")
    image_qs = ImageFile.objects.get(id=img_id)
    detect.run(source=image_qs.image.path,
               line_thickness=1,
               project="/절대경로/", # ->  '/절대경로/exp1~.../_.jpg'에 detect결과(이미지) 저장
               imgsz=384,
               conf_thres=0.1,
               # best.pt(학습된 모델의 파라미터가 저장된 파일)를 django 프로젝트 폴더에 넣고
               weights='[django프로젝트path]/yolov5/best.pt'
               )

# 일단 이렇게 detect.py 원본으로 돌려봐서 작동하면
# 커스텀한 detect.py으로도 동작하는지 다시 테스팅