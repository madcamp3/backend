
# 카이스트 몰입캠프 3주차 프로젝트

## 1. Project Description

카이스트 몰입캠프 3주차 프로젝트입니다. 

## 2. Project Structures

![img](https://user-images.githubusercontent.com/77768091/149932952-d0a71853-9f51-43d6-8399-b5fa15b3df7c.png)

## 3. Deep Learning Model

OpenAI의 jukebox 모델을 참고하여 음악을 생성하는 모듈을 구성했으며, 해당 모듈을 이용하여 음악 파일들을 생성했습니다.

jukebox 모델은 일반적인 음악 생성 dnn과 같이 encoder decoder구조로 이루어져 있습니다. 인코딩 후에 가사를 추가하여 다시 upsampling 과정을 거치며, 각각 top-level, middle-level, bottom-level 레벨의 encoder와 decoder를 사용했습니다.

## 4. Server

파일 전송 등의 작업이 이루어지는 서버로 fastAPI가 적합하다고 생각했습니다.

get요청을 통해 데이터베이스상에 저장된 파일 시스템 내 음악 파일명을 반환합니다.

```python
@app.get("/classic/all")
async def getClassicList():
    query_args = {"CATEGORY": "classic"}
    result = exec_fetch_query(SEARCHLIST_QUERY, query_args)
    if not result:
        return JSONResponse(content={"data": []}, status_code=404)
    return JSONResponse(content={"data": result}, status_code=200)
```

get요청에 포함된 url parameter로 파일명을, url에 포함된 카테고리명에서 카테고리명을 얻어 서버 파일 시스템 내의 음악 파일을 반환합니다.

```python
@app.get("/classic/{filename:path}")
async def getClassicItem(filename: str):
    query_args = {"CATEGORY": "classic", "FILENAME":filename}
    result = exec_fetch_query(SEARCHFILE_QUERY, query_args)
    if not result:
        return 404, "file not found"
    file_path = "classic/" + filename + ".mp3"
    return FileResponse(status_code=200, path=file_path)
```

서버는 aws의 ec2인스턴스 상에 nginx, gunicorn gateway 서버를 이용하여 구동된 상태입니다.
