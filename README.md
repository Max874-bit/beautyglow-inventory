# 뷰티글로우 통합 재고관리 시스템

## 프로젝트 개요
이 프로젝트는 뷰티글로우의 통합 재고관리 시스템으로, 제품, 공급업체, 창고, 프로모션 등을 효율적으로 관리하기 위한 백엔드 API를 제공합니다.

## 주요 기능
- 제품 및 재고 관리
- 공급업체 관리
- 창고 및 위치 관리
- 프로모션 관리 (할인, 묶음상품, 사은품 등)
- 재고 실사 및 분석

## 기술 스택
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic (데이터베이스 마이그레이션)
- Python 3.8+

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 추가:
```
DATABASE_URL=postgresql://user:password@localhost/inventory_db
```

4. 데이터베이스 마이그레이션
```bash
alembic upgrade head
```

5. 서버 실행
```bash
uvicorn api.main:app --reload
```

## API 문서
서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 프로젝트 구조
```
inventory_management_system/
├── api/
│   └── main.py
├── database/
│   ├── database.py
│   └── models.py
├── services/
│   └── promotion_service.py
├── alembic/
├── requirements.txt
└── README.md
```

## 라이선스
이 프로젝트는 비공개 소프트웨어입니다. 모든 권리는 뷰티글로우에 있습니다. 