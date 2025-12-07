# PDF to PPTX 변환 서비스 (NotebookLM Support)

이 프로젝트는 **Google NotebookLM**에서 생성된 슬라이드 PDF 파일을 편집 가능한 **PowerPoint (.pptx)** 형식으로 변환하여, 사용자들이 보다 쉽게 자료를 활용할 수 있도록 돕기 위해 개발되었습니다.

기존의 이미지 기반 PDF 슬라이드를 AI OCR 기술을 통해 텍스트와 이미지로 분리하고, 편집 가능한 프레젠테이션 파일로 재구성해줍니다.

> **🌟 Live Demo**: [https://joo.is/ppt2ppt](https://joo.is/ppt2ppt)
> **Original**: [https://pdf2pptx-r5gd-ge9pmnpwq-techkwons-projects.vercel.app/](https://pdf2pptx-r5gd-ge9pmnpwq-techkwons-projects.vercel.app/)

## ✨ 주요 기능

- **NotebookLM 최적화**: NotebookLM이 생성한 슬라이드 형식에 맞춰 변환을 지원합니다.
- **AI 초정밀 OCR**: [Upstage Document AI](https://www.upstage.ai/)를 활용하여 이미지 속 텍스트를 높은 정확도로 추출합니다.
- **완벽한 편집 지원**: 단순 이미지가 아닌, 수정 가능한 텍스트 박스와 개별 이미지로 변환됩니다.
- **모던한 UI 디자인**: 최신 Apple 스타일의 Glassmorphism과 다크 모드를 지원하는 아름다운 웹 인터페이스를 제공합니다.
- **안전한 처리**: 변환된 파일은 안전하게 처리되며 제공된 링크를 통해서만 다운로드 가능합니다.

## 🛠 기술 스택

- **Frontend**: React, Vite, Tailwind CSS (Glassmorphism 디자인)
- **Backend**: Python, FastAPI
- **AI Engine**: Upstage Document Parser API
- **PPTX Engine**: `python-pptx`

## 📂 프로젝트 구조

```bash
pdf-to-pptx-service/
├── backend/          # Python FastAPI 서버
│   ├── app/          # 애플리케이션 로직
│   ├── outputs/      # 생성된 PPTX 파일 저장소
│   ├── uploads/      # 업로드된 PDF 임시 저장소
│   └── requirements.txt
└── frontend/         # React 프론트엔드
    ├── src/          # React 컴포넌트 및 스타일
    ├── tailwind.config.js
    └── package.json
```

## 🚀 시작하기

### 사전 요구 사항

- Python 3.8 이상
- Node.js 16 이상
- Upstage API Key ([Upstage Console](https://console.upstage.ai/)에서 발급)

### 1. 백엔드 설정 (Backend)

1. 백엔드 디렉토리로 이동합니다:
   ```bash
   cd backend
   ```
2. 가상 환경을 생성하고 실행합니다:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   # venv\Scripts\activate  # Windows
   ```
3. 라이브러리를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```
4. 환경 변수를 설정합니다:
   - `.env.example` 파일을 복사하여 `.env` 파일을 만듭니다:
     ```bash
     cp .env.example .env
     ```
   - `.env` 파일을 열어 API 키를 입력합니다:
     ```env
     UPSTAGE_API_KEY=발급받은_API_키_입력
     ```
5. 서버를 실행합니다:
   ```bash
   uvicorn app.main:app --reload --port 8001
   ```

### 2. 프론트엔드 설정 (Frontend)

1. 프론트엔드 디렉토리로 이동합니다:
   ```bash
   cd frontend
   ```
2. 패키지를 설치합니다:
   ```bash
   npm install
   ```
3. 개발 서버를 실행합니다:
   ```bash
   npm run dev
   ```
4. 브라우저에서 `http://localhost:5173`으로 접속합니다.

## ☁️ 배포 가이드 (Deployment)

이 프로젝트는 **Backend(Render)**와 **Frontend(Vercel)** 조합으로 무료 배포에 최적화되어 있습니다.

### 1단계: Github에 코드 올리기
1. Github에 새 Repository를 생성합니다 (예: `pdf-to-pptx-service`).
2. 아래 명령어로 코드를 푸시합니다:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for deployment"
   git branch -M main
   git remote add origin <당신의_GITHUB_주소>
   git push -u origin main
   ```

### 2단계: Backend 배포 (Render)
1. **[Render Dashboard](https://dashboard.render.com/)**에 접속하여 'New' -> **'Blueprint'**를 클릭합니다.
2. Github 레포지토리를 연결하면, 자동으로 `render.yaml`을 인식합니다.
3. **Apply**를 누르기 전에, `UPSTAGE_API_KEY` 환경변수 값을 입력합니다.
4. 배포가 시작됩니다.
5. 배포 완료 후, 서비스 이름 아래에 있는 **URL** (예: `https://pdf-to-pptx-backend.onrender.com`)을 복사해둡니다.

> **참고**: Render 무료 서버는 15분간 요청이 없으면 절전 모드에 들어갑니다. 하지만 우리 프론트엔드에는 **서버 자동 깨우기(Auto Wake-up)** 기능이 탑재되어 있어 걱정 없습니다!

### 3단계: Frontend 배포 (Vercel)
1. **[Vercel Dashboard](https://vercel.com/new)**에 접속하여 'Add New Project'를 클릭합니다.
2. 동일한 Github 레포지토리를 Import 합니다.
3. **Framework Preset**은 `Vite`로 자동 설정될 것입니다.
4. **Root Directory**를 `Edit` 눌러서 `frontend` 폴더를 선택합니다.
5. **Environment Variables** (환경 변수) 섹션을 펼쳐서 추가합니다:
   - **Key**: `VITE_API_URL`
   - **Value**: 아까 복사한 Render 백엔드 주소 (예: `https://pdf-to-pptx-backend.onrender.com`)
   - **주의**: 주소 뒤에 슬래시(`/`)는 빼주세요.
6. **Deploy** 버튼을 클릭합니다.

### 🎉 완료!
이제 Vercel이 제공하는 도메인으로 접속하면 나만의 PDF 변환 서비스가 작동합니다.

## 📄 라이선스

MIT License
