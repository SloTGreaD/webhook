from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        payload = await request.json()
        # Обработка данных из Shopify
        df = pd.json_normalize(payload)
        df.to_excel("shopify_webhook_data.xlsx", index=False)
        return JSONResponse(status_code=200, content={"message": "Webhook received successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
