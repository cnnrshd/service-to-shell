import logging
import subprocess

from fastapi import FastAPI, Query, Response

app = FastAPI()
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


@app.get("/")
async def root():
    return {"message": "Working DNSSearcher"}


@app.get("/dns")
def dns(domainname: str):
    logger.info(f"DNS lookup for {domainname}")
    # basically DVWA but with nslookup instead of ping
    ret = subprocess.run(f"nslookup {domainname}", shell=True, capture_output=True)
    logger.info(f"Response status code: {ret.returncode}")
    if ret.returncode:
        logger.warn(f"stderr: {ret.stderr.decode('utf-8')}")
    return Response(content=ret.stdout.decode("utf-8"), media_type="text/plain")


@app.get("/dns2")
def dns2(
    domainname: str = Query(
        ...,
        pattern=r"^[a-zA-Z0-9][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9]{0,1}\.([a-zA-Z]{1,6}|[a-zA-Z0-9-]{1,30}\.[a-zA-Z]{2,3})$",
    ),
):
    logger.info(f"DNS lookup for {domainname}")
    # basically DVWA but with nslookup instead of ping
    ret = subprocess.run(f"nslookup {domainname}", shell=True, capture_output=True)
    logger.info(f"Response status code: {ret.returncode}")
    if ret.returncode:
        logger.warn(f"stderr: {ret.stderr.decode('utf-8')}")
    return Response(content=ret.stdout.decode("utf-8"), media_type="text/plain")


@app.get("/ping")
def ping(target: int):
    logger.info(f"Target is type: {type(target)}")
    logger.info(f"Target memory size is {target.__sizeof__()}")
    logger.info(f"Ping {target}")
    ret = subprocess.run(f"ping -c 1 {target}", shell=True, capture_output=True)
    logger.info(f"Response status code: {ret.returncode}")
    if ret.returncode:
        logger.warn(f"stderr: {ret.stderr.decode('utf-8')}")
    return Response(content=ret.stdout.decode("utf-8"), media_type="text/plain")
