from fastapi import FastAPI

app = FastAPI(title="BeautyGlow Inventory API", description="뷰티글로우 통합 재고관리 시스템 API")

@app.get("/")
async def root():
    return {"message": "BeautyGlow Inventory API is running"}
