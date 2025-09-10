from fastapi import FastAPI
from mangum import Mangum
import sys
import os

# backend files import karne ke liye path add karo
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app  # ✅ tumhara FastAPI app

handler = Mangum(app)