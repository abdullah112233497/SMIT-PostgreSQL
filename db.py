from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Neon PostgreSQL URL
DATABASE_URL = "postgresql://neondb_owner:npg_32iktEAoOVDr@ep-restless-mode-a1a7hl1a-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Engine
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()