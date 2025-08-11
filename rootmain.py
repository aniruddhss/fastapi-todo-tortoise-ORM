import uvicorn 


if __name__ == "__main__":
    # For local development
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
else:
    # For production deployment (Render)
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)