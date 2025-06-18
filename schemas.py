from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: int
    name: str
    email: str
    password: str
    role: str
    active: bool
    full name: str


class ReadUsers(BaseModel):
    id: int
    name: str
    email: str
    password: str
    role: str
    active: bool
    full name: str
    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    Name: str


class ReadUser(BaseModel):
    id: int
    Name: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    role: str = Field(..., max_length=100)
    active: bool = Field(...)

    class Config:
        from_attributes = True

