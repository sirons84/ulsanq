# 📸 OCR 맞춤법 교정기

Gemini API를 활용하여 이미지 속 텍스트를 인식하고 맞춤법을 교정하는 웹 애플리케이션입니다.

## ✨ 주요 기능

- 📷 **이미지 업로드 또는 카메라 촬영** 지원
- 🔍 **AI 기반 OCR** - Gemini 2.5 Flash 모델 사용
- ✅ **자동 맞춤법 교정** - 띄어쓰기, 문법 오류 수정
- 📝 **수정 내역 표시** - 어떤 부분이 바뀌었는지 명확히 표시
- 📥 **결과 다운로드** - TXT 파일로 저장 가능

## 🚀 배포 방법

### 1. GitHub Repository 준비

```bash
# 프로젝트 구조
your-repo/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml (로컬 테스트용)
```

### 2. Google AI Studio에서 API 키 발급

1. [Google AI Studio](https://aistudio.google.com/apikey)에 접속
2. "Get API Key" 버튼 클릭
3. API 키 복사

### 3. Streamlit Cloud 배포

1. [Streamlit Cloud](https://streamlit.io/cloud)에 로그인
2. "New app" 클릭
3. GitHub repository 선택
4. Main file path: `app.py`
5. **Advanced settings > Secrets** 클릭
6. 다음 내용 입력:

```toml
GEMINI_API_KEY = "여기에-발급받은-API-키-입력"
```

7. "Deploy!" 클릭

### 4. 로컬 테스트 (선택사항)

```bash
# 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# .streamlit/secrets.toml 파일 생성 및 API 키 입력

# 앱 실행
streamlit run app.py
```

## 📋 사용 방법

1. **이미지 준비**
   - 텍스트가 포함된 이미지 파일 준비
   - 또는 웹캠으로 직접 촬영

2. **분석 실행**
   - 파일 업로드 또는 카메라 촬영 선택
   - "텍스트 인식 및 맞춤법 교정" 버튼 클릭

3. **결과 확인**
   - 원본 텍스트와 교정된 텍스트 비교
   - 수정 내역 확인
   - 필요시 TXT 파일로 다운로드

## 💡 사용 팁

- ✅ 선명하고 밝은 이미지 사용
- ✅ 텍스트가 명확하게 보이는 사진
- ✅ 흔들림 없이 촬영
- ⚠️ 손글씨보다 인쇄된 텍스트가 더 정확함
- ⚠️ 텍스트가 잘리지 않도록 주의

## 🔧 기술 스택

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Image Processing**: Pillow (PIL)
- **Deployment**: Streamlit Cloud

## 📄 라이선스

MIT License

## 🤝 기여

이슈나 PR은 언제나 환영합니다!

## 📞 문의

문제가 있거나 제안사항이 있으시면 Issue를 등록해주세요.