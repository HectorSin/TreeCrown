# Rescue Crew

해당 코드는 제주테크노파크에서 주관하는 [2023년도 제주 위성데이터 활용 경진대회](https://aifactory.space/task/2700/overview) 출품작 RESCUE CREW 코드입니다.

- 주최 : 제주특별자치도
- 주관 : 제주테크노파크
- 운영 : 인공지능팩토리 



## 1. 주제



## 2. 배경



## 3. 파일 설명 [Files]

1. data
   1. final_image (5) 이전 단계에서 만들어진 이미지들을 원래 형태대로 다시 합친 이미지를 저장한 폴더입니다. 결과적으로 최종 이미지는 해당 폴더에 저장됩니다.
   2. image_data - (2) input_image의 사진을 더 세부적인 학습을 위해 나눈 이미지입니다.
   3. input_image - (1) 처음 학습을 진행하기 위해 인공위성 사진을 넣는 폴더입니다. 
   4. model_data - (*) 사전 학습한 모델을 넣어두는 폴더입니다.
   5. predictions - (3) 학습이 진행되면서 나무의 좌표들이 저장되는 파일입니다.
   6. result_pic - (4) 3에서의 좌표들을 반영해 나무 수와 나무 위치를 사진위에 그려 저장된 이미지들을 저장한 폴더입니다.
2. model
   1. _create_xml.py - XML 데이터를 조작하고 생성하는 역할.
   2. pic_crop.py - 학습에 맞는 형태로 사진을 조작하는 코드들이 들어간 파일입니다.
   3. predict_to_result.py - 학습을 진행하는 주요 모델 코드들이 들어간 파일입니다.
   4. run1.py - 첫번째 실행 코드
   5. run2.py - 두번재 실행 코드
   6. run3.py - 세번째 실행 코드
   7. xml_2_csv.py
3. static - 웹의 각 디자인 요소들을 담당하는 css 및 기타 파일들을 담은 폴더입니다.
4. templates - 웹의 각 페이지를 담당하는 html 파일들을 포함한 템플릿 폴더입니다.
5. app.py - Flask 웹 실행 파일입니다.
6. environment.yaml - conda 가상 환경 세팅값입니다.

## 4. Packages



## 5. Requirements



## 6. Reference

1. [Individual Tree-Crown Detection and Species Identification in Heterogeneous Forests Using Aerial RGB Imagery and Deep Learning](https://www.mdpi.com/2072-4292/15/5/1463)
2. [Automated Individual Tree Detection and Crown Delineation Using High Spatial Resolution RGB Aerial Imagery](https://www.researchgate.net/publication/264179857_Automated_Individual_Tree_Detection_and_Crown_Delineation_Using_High_Spatial_Resolution_RGB_Aerial_Imagery)
3. [Tree Crown Detection and Delineation in a Temperate Deciduous Forest from UAV RGB Imagery Using Deep Learning Approaches: Effects of Spatial Resolution and Species Characteristics](https://www.mdpi.com/2072-4292/15/3/778)
4. [Individual Tree Crown Segmentation and Crown Width Extraction From a Heightmap Derived From Aerial Laser Scanning Data Using a Deep Learning Framework](https://www.frontiersin.org/articles/10.3389/fpls.2022.914974/full)
5. [Accurate delineation of individual tree crowns in tropical forests from aerial RGB imagery using Mask R-CNN](https://zslpublications.onlinelibrary.wiley.com/doi/full/10.1002/rse2.332)
6. [Automated Individual Tree Detection and Crown Delineation Using High Spatial Resolution RGB Aerial Imagery](https://koreascience.kr/article/JAKO201113036232016.page)
7. [Cross-site learning in deep learning RGB tree crown detection](https://www.sciencedirect.com/science/article/pii/S157495412030011X)





