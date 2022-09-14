from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from hashing import Hash
import schemas, database, models, tokens
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db) ):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")
    
    access_token = tokens.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


