from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from db import *
from query import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "FastAPI data Server"


@app.get("/classic/all")
async def getClassicList():
    query_args = {"CATEGORY": "classic"}
    result = exec_fetch_query(SEARCHLIST_QUERY, query_args)
    if not result:
        return JSONResponse(content={"data": []}, status_code=404)
    return JSONResponse(content={"data": result}, status_code=200)
    
@app.get("/hiphop/all")
async def getClassicList():
    query_args = {"CATEGORY": "hiphop"}
    result = exec_fetch_query(SEARCHLIST_QUERY, query_args)
    if not result:
        return JSONResponse(content={"data": []}, status_code=404)
    return JSONResponse(content={"data": result}, status_code=200)

@app.get("/pop/all")
async def getClassicList():
    query_args = {"CATEGORY": "pop"}
    result = exec_fetch_query(SEARCHLIST_QUERY, query_args)
    if not result:
        return JSONResponse(content={"data": []}, status_code=404)
    return JSONResponse(content={"data": result}, status_code=200)

@app.get("/classic/{filename:path}")
async def getClassicItem(filename: str):
    query_args = {"CATEGORY": "classic", "FILENAME":filename}
    result = exec_fetch_query(SEARCHFILE_QUERY, query_args)
    if not result:
        return 404, "file not found"
    file_path = "classic/" + filename + ".mp3"
    return FileResponse(status_code=200, path=file_path)


@app.get("/hiphop/{filename:path}")
async def getClassicItem(filename: str):
    query_args = {"CATEGORY": "hiphop", "FILENAME":filename}
    result = exec_fetch_query(SEARCHFILE_QUERY, query_args)   
    if not result:
        return 404, "file not found"
    file_path = "hiphop/" + filename + ".mp3"
    return FileResponse(status_code=200, path=file_path)


@app.get("/pop/{filename:path}")
async def getClassicItem(filename: str):
    query_args = {"CATEGORY": "pop", "FILENAME":filename}
    result = exec_fetch_query(SEARCHFILE_QUERY, query_args)
    if not result:
        return 404, "file not found"
    file_path = "pop/" + filename + ".mp3"
    return FileResponse(status_code=200, path=file_path)


@app.exception_handler(DBConnectionFailException)
async def db_connection_fail_exception_handler(request: Request, exc: DBConnectionFailException):
    return JSONResponse(status_code=400, content=exc.response_content)

@app.exception_handler(DBRequestFailException)
async def db_request_fail_exception_handler(request: Request, exc: DBRequestFailException):
    return JSONResponse(status_code=400, content=exc.response_content)

@app.exception_handler(DBPrimaryKeyDuplicateException)
async def db_primarykey_duplicate_exception_handler(request: Request, exc: DBPrimaryKeyDuplicateException):
    return JSONResponse(status_code=400, content=exc.response_content)

