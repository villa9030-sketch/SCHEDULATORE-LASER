"""Backend initialization"""
from .app import app
from .models import initialize_database

# Inizializza database all'importazione
try:
    initialize_database()
except Exception as e:
    print(f"Warning: Database initialization: {e}")

__all__ = ['app', 'initialize_database']
