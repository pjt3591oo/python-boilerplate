# python boilerplate

파이썬 프로젝트 보일러플레이트이며 
패키지와 utils에 테스트 파일이 포함되어 있으며 tests에는 이를 테스트 하는 코드가 작성되어 있습니다.

해당 프로젝트를 본 프로젝트에 적용하기 위해서는 기존의 예시 코드를 지우시면 됩니다

## directory

* config
* docs
* packages
* tests
* utils

* app.py
* README.md
* requirements.txt
* setup.py
* makefile

## config

해당 프로젝트의 각종 설정파일을 가지고 있는다.

## docs

해당 프로젝트의 여러 문서를 작성한다.

## app.py
 
프로젝트 실행 파일

## ./tests/

테스트 코드가 들어있다

## ./tests/text.py

테스트 코드 실행

## ./packages/

패키지가 들어있다 패키지는 디렉토리 단위로 생성을 하며 __init__.py 파일을 정의한다.
__init__.py에는 해당 패키지의 정보를 관리한다.

## requirements.txt

해당 프로젝트의 의존성 모듈을 관리하다.

## setup.py

setuptools를 이용하여 테스트, 빌드, 배포과정을 쉽게 관리해주는 코드를 작성한다.

setuptools를 활용한 프로젝트는 파이썬에 의해 실행되는 CLI의 프로그램의 역할을 하기도 한다.


> 매번 프로젝트를 생성할 때마다 구성하기 귀찮아서 만들어 둠.....