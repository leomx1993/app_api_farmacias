import secrets
from fastapi import Header, HTTPException

access_token = None

def generate_token():
    global access_token
    
    token_length = 10
    access_token = secrets.token_hex(token_length)
    return {"access_token": access_token}

def get_current_user(authorization: str = Header(None)):
    global access_token
    
    if access_token is None:
        raise HTTPException(status_code=401, detail="É necessário enviar seu token de acesso")
    
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    token = authorization.replace("Bearer ", "")
    if token != access_token:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    return token
