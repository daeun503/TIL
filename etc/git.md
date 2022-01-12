# Git

> Git은 분산 버전 관리 시스템(DVCS)이다. (*DVCS == Distributed Version Control System)
>
> 소스코드의 버전 및 이력을 관리할 수 있다. 



[toc]

## 준비하기

### git 설치

윈도우에서 git을 활욜하기 위해서는 [git bash](https://git-scm.com/)를 설치해야한다. 

git을 활용하는 방식으로 GUI툴인 `source tree`, `github desktop`등을 활용 할 수도 있다. 



초기 설치를 완료한 이후에 컴퓨터에 `author`정보를 입력한다.

```bash
git config --global user.name "유저 이름"
git config --global user.email "유저 이메일"

# 확인하기
git config --global user.name
> 출력 결과 : 유저 이름
git config --global user.email
> 출력 결과 : 유저 이메일
```



### 기초 bash 명령어들

> 터미널에서는 항상 자신의 위치를 확인하자

- 현재 위치 확인하기

```bash
pwd
```

- 현재 위치에 있는 파일 목록보기

```bash
ls
ls -a    # 숨긴 파일도 보여준다.
ls -al   # 숨긴 파일을 포함하여 자세한 정보를 보여준다.
```

- 현재 위치에서 이동하기

```bash
cd 경로(폴더명을 포함한 위치)  # e.g. $ cd ~/Desktop , $ cd Desktop/ssafy5/
cd ..                      # 한 단계 상위 폴더로 이동
cd -                       # 이전 경로로 이동
.                          # 현재 경로
```

- 파일 만들기

```bash
touch README.md
```

- 폴더(경로) 만들기

```bash
mkdir my_folder
```

- 파일 삭제 (조심)

```bash
rm README.md
```

- 폴더 삭제 (진짜 조심)

```bash
rm -rf my_folder
```

- 이동 or 이름 바꾸기 (많이 사용 X)

```bash
mv 경로 대상 
```



## 로컬 저장소 (repository) 활용하기

### 0. 저장소 초기화

- 해당 경로가 git으로 관리되지 않은 `초기 상태`일 때 딱 한 번 실행

```bash
git init
```

- 실행하고 나면 경로 끝에 `(master)`글자가 붙는다.

```bash
ls -al
# . git/ 이 생성되어 있는지 확인한다.
```

- `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
- `(master)`라는 글자는 `master branch`를 의미한다.



### 1. add 

> `working directory`, 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야한다. 

```bash
git add 특정경로/파일이름  # 특정 경로의 특정 파일
git add 특정 경로        # 특정 경로에 있는 모든 파일(변경 사항이 있는)
git add .               # 현재 경로에 있는 모든 파일(변경 사항이 있는)
```

- `add` 전 상태

```bash
git status   # 현재 git 상황 
```

- `add` 후 상태

```bash
git add .
git status
```



### 2. commit

> commit은 이력을 확정 짓는 명령어 입니다. 해당 시점의 스냅샷을 기록합니다. (staging area에 올라가 있는 파일들에 대한)
>
> 커밋 시에는 반드시 메시지를 작성해야하며, 메시지 변경 사항을 알 수 있도록 명확하게 작성하는 것이 좋다.

```bash
git commit -m '마크다운 정리'
git log       # 기록 확인. 빠져 나올 땐 :q
:q
```

- 커밋 기록은 해시값을 바탕으로 구분된다.





## 원격 저장소 (remote repository) 활용하기

### 0. 준비사항

- 원격 저장소가 필요하다. (lab.ssafy : New project)

- clone 버튼으로 HTTPS 주소를 복사한다.



### 1. 원격 저장소 주소 등록

- 주소를 등록한다.

```bash
git remote add origin 복사한 HTTPS주소

git remote -v               # 확인하기
git remote remove origin    # origin이라는 이름의 저장소 주소 삭제하기
```



### 2. Push하기

```bash
git push origin master
```

- origin : 등록된 저장소 이름
- master : branch 이름



**이후 변경 사항이 생길 때 마다, `add` `commit` `push`를 반복한다.**

- push를 하게 되면, 되돌리기가 힘들다.
  - push하기 전에 다시 보자.