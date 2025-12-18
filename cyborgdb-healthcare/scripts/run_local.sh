#!/bin/bash
export $(cat config/env.sample | xargs)
uvicorn src.app.main:app --reload --port 8000
