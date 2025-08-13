# 📊 MoSPI API Gateway for Data Dissemination

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi)
![Build Status](https://img.shields.io/badge/Build-working-brightgreen)

---

## 📌 Overview

The **MoSPI API Gateway** is a scalable, privacy-compliant platform for **secure, real-time access to microdata** collected by the **Ministry of Statistics and Programme Implementation (MoSPI)**.

It enables:
- **Researchers** to run SQL queries directly on microdata
- **Government agencies** to enforce privacy and role-based access
- **Public users** to access open datasets in multiple formats

---

## 🚀 Key Features

| Feature | Description |
|---------|-------------|
| ⚡ **Real-Time Queries** | Execute SQL queries directly on MoSPI microdata |
| 🔑 **Role-Based Access** | Different permissions for citizens, researchers, and agencies |
| 🛡 **Privacy-First Architecture** | Cell suppression, query blocking, and aggregation filters |
| 🛠 **Configurable Survey Framework** | Add new surveys with minimal changes |
| 📊 **Multi-Format Output** | JSON, CSV, and ready-to-use visual charts |
| 📈 **High Scalability** | Designed for millions of queries |

---

## 🗂 Project Structure

```plaintext
mospi-api-gateway/
│── backend/
│── frontend/
│── Docker/
│── scripts/
│── requirements.txt
│── .env.example
