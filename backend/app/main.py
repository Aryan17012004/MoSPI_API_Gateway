from fastapi import FastAPI
from .config.settings import settings
from .api.v1 import query_routes, metadata_routes, auth_routes, payment_routes, usage_routes

app = FastAPI(
    title="MoSPI API Gateway",
    version="1.0.0",
    description="API Gateway for MoSPI datasets with RBAC, payments, privacy compliance, and visualization"
)

# API routes
app.include_router(query_routes.router, prefix="/api/v1/query", tags=["Query"])
app.include_router(metadata_routes.router, prefix="/api/v1/metadata", tags=["Metadata"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(payment_routes.router, prefix="/api/v1/payment", tags=["Payment"])
app.include_router(usage_routes.router, prefix="/api/v1/usage", tags=["Usage"])

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "MoSPI API Gateway running"}
