## AWS Ubuntu에서 Yolo v5 세팅하기



### -1. 자주쓰는 linux 명령어

tab : 자동완성

pwd : 현재경로출력

cd ~ : home

cd / : root

cd .. : 상위 디렉터리로 이동

cd . : 현재경로로 이동

cd [디렉터리명] : 해당 디렉터리로 들어가기

ls : 현재 디렉터리 내 파일/폴더 정보

ll : 상세

mkdir [폴더명] : 폴더생성

top : 프로세스 보기

nvidia-smi : GPU 모니터링

who : user 보기

mv : 파일 이동

cp : 파일 복사

zip : 압축

unzip : 압축풀기

wget [URL] : 해당 URL에 있는 파일 다운로드

rm [file명] : 파일 영구삭제

rm -rf [폴더명] : 폴더 영구삭제 (*오타 주의)



### 0.AWS

https://multi-k3.signin.aws.amazon.com/console

d-lab32 로그인 후

서버명 d-team06 - 인스턴스 시작



### 1. putty 접속(권한)

putty.exe 켜고 ubuntu 계정으로 들어감(어느정도 권한 있는 계정,)

`home/ubuntu/` 경로에서 시작! (ubuntu 계정 디렉터리)



### 2. 가상환경 세팅

아래와 같이 yolov5 가상환경 clone한 뒤 (최초 1회)

activate

```
conda create -n yolov5 --clone python3
conda activate yolov5
```



### 3. yolo v5 클론

/home/ubuntu/ 경로에서 깃허브에 있는 yolov5를 clone

```
git clone https://github.com/ultralytics/yolov5.git
sudo chmod 777 -R ~/yolov5
```



### 4. 디렉터리 및 파일 세팅

```
mkdir dataset
```

현재위치 home/ubuntu



.yaml 카피

```
cp ./yolov5/data/coco128.yaml ./dataset/data.yaml
```

현재위치 home/ubuntu



```
mkdir images
mkdir labels
```

현재위치 home/ubuntu/dataset



- 디렉터리 구조

  /home/ubuntu/

  yolov5

  ​		└ requirements.txt

  ​		└ train.py

  ​		└ detect.py

  ​		└ runs

  ​				└ detect

  ​				└ train

  ​						└ weight



​	dataset

​			└ data.yaml

​			└ images

​					└ .jpg

​			└ labels

​					└ .txt



### 4. 모듈 설치

#### 4.0 pip upgrade

```
pip3 install --upgrade pip
```



#### 4.1. requirements.txt

yolov5 framework에서 필요로 하는 라이브러리 모듈 등을 일괄적으로 설치

```
pip3 install -r requirements.txt
```

현재경로 /home/ubuntu/yolov5



#### 4.2 zip(optional)

압축이 필요하면 설치(첨에 안 깔려있음)

```
sudo apt install zip
```



### 5. GPU 세팅 (CUDA 버전 설정)

현재 연결되어있는 cuda 버전 확인

```
cd /
ll /usr/local
```

버전이 낮다면 cuda 버전을 11.1로 설정

```
sudo ln -sfT /usr/local/cuda-11.1/ /usr/local/cuda
```



### 6. Jupyter notebook 서버

/home/ubuntu/에 workspace 디렉터리 생성하고 거기서 jupyter notebook 서버 생성

```
cd ~
mkdir workspace
nohup jupyter-notebook --ip=0.0.0.0 --no-browser --port=8932 &
```

/home/ubuntu/workspace/nohup.out 이 생성되었다면 정상



local에서 chrome창을 띄워 jupyter notebook 서버 사용

(putty 종료해도 jupyter notebook 사용 가능)

```
http://35.75.55.16:8932/
```

password 입력



### 7. Yolo v5 학습

home/ubuntu/dataset/images/

home/ubuntu/dataset/labels/

안에다가 각각 .jpg, .txt 형태의 이미지/레이블링 파일 넣어놓고

Jupyter notebook에서 코드 돌리면 됨



### 8. Local에 있는 파일을 AWS서버에 업로드

#### 8.1. chrome에서 jupyter notebook 켠다음 업로드 버튼 이용

putty.exe로 옮기고, 쓰고 하면 됨

#### 8.2. FileZilla 이용

편함

