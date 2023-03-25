from fastapi import FastAPI, HTTPException, Response
import yaml

app = FastAPI()


@app.get("/")
async def root(uuid: str) -> str:
    if not uuid:
        raise HTTPException(status_code=422, detail="validation error")
    
    with open('config.yaml','r') as f:
        config = yaml.safe_load(f)
    
    config['proxies'][0]['uuid'] = uuid
    
    return Response(content=yaml.dump(config, sort_keys=False), media_type="application/yaml")