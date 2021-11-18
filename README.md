# sw_jungle_week_03
## 폴더 구조 
- 각각 {ID}로 브랜치를 만들고 {ID}로 폴더를 만들고 그 안에서 {백준 문제번호}.py로 만들어 주시면 됩니다. 

## git 설정하기
### .gitignore
- 저장소에 올리지 않을 특정 파일 목록
- git에서 추적하지 않도록 만들어 주는 설정 파일 
- https://www.toptal.com/developers/gitignore 사이트를 이용하면 손쉽게 만들수 있어요!
- 지금 저장소에 있는 `.gitignore`파일의 경우 `python`, `mac OS`, `Windows`, `venv`키워드를 넣어서 생성한 파일입니다.
### Windows & macOS 개행문자 설정하기 
- 설정 이유: 엔터키를 쳐서 행간의 개행이 발생하였을때 내부적으로 들어가는 문자가 운영체제에 따라 달라진다. 
- 관련 내용:
    - 해당 용어(`CR`, `LF`)와 이 용어들의 조합(`CRLF`)은 새로운 줄 (New line) 으로 바꾸는 방식을 의미한다. `CR` 과 `LF` 는 타자기 시절 부터 줄바꿈을 위해 사용하던 방식인데 각각의 의미는 다음과 같다.  

    - `CR` : 현재 커서를 줄 올림 없이 가장 앞으로 옮기는 동작(`\r`)
    - `LF` : 커서는 그 자리에 그대로 둔 상황에서 종이만 한 줄 올려 줄을 바꾸는 동작(`\n`)
    
    - 이 방식(`CR` + `LF`)은 타자기 이후 컴퓨터에서도 줄바꿈을 의미할 때도 사용되었으나, 줄바꿈을 할 때 굳이 2 byte 를 사용할 필요가 없기에 메모리/Storage 절약을 위해 `CR` 혹은 `LF` 만 사용하기도 하였다.
**[출처]**: https://technote.kr/300 [TechNote.kr]
- 서로 다른 운영체제에서 협업을 위해서 이를 맞춰주기 위해 아래와 같이 설정한다. 
    - Windows:
    `git config --global core.autocrlf true`
    - MacOS:
    `git config --global core.autocrlf input`