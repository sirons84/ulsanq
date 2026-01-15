import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

# Streamlit 페이지 설정
st.set_page_config(
    page_title="📸 OCR 맞춤법 교정기",
    page_icon="📝",
    layout="centered"
)

# API 키 설정
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("⚠️ API 키를 설정해주세요. Streamlit secrets에 GEMINI_API_KEY를 추가하세요.")
    st.stop()

# 제목 및 설명
st.title("📸 OCR 맞춤법 교정기")
st.markdown("""
사진 속 텍스트를 인식하고 맞춤법을 교정해드립니다.
- 📷 이미지 파일을 업로드하거나 카메라로 촬영하세요
- 🔍 AI가 텍스트를 읽고 분석합니다
- ✅ 맞춤법 오류를 자동으로 교정합니다
""")

# 입력 방식 선택
input_method = st.radio(
    "입력 방식을 선택하세요:",
    ["📁 파일 업로드", "📷 카메라 촬영"],
    horizontal=True
)

# 이미지 입력
image = None
if input_method == "📁 파일 업로드":
    uploaded_file = st.file_uploader(
        "이미지 파일을 업로드하세요",
        type=["jpg", "jpeg", "png", "webp"],
        help="JPG, PNG, WEBP 형식을 지원합니다"
    )
    if uploaded_file:
        image = Image.open(uploaded_file)
else:
    camera_photo = st.camera_input("사진을 촬영하세요")
    if camera_photo:
        image = Image.open(camera_photo)

# 이미지가 있을 때 처리
if image:
    # 이미지 표시
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="업로드된 이미지", use_column_width=True)
    
    # 분석 버튼
    if st.button("🔍 텍스트 인식 및 맞춤법 교정", type="primary"):
        with st.spinner("AI가 이미지를 분석 중입니다..."):
            try:
                # Gemini 모델 설정 (Gemini 2.5 Flash 사용)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # 프롬프트 작성
                prompt = """
이 이미지에 있는 모든 텍스트를 읽고 다음 작업을 수행해주세요:

1. **원본 텍스트**: 이미지에서 인식된 텍스트를 그대로 추출
2. **맞춤법 교정**: 맞춤법, 띄어쓰기, 문법 오류를 교정한 텍스트 제공
3. **수정 내역**: 어떤 부분이 수정되었는지 간단히 설명

다음 형식으로 응답해주세요:

## 📄 원본 텍스트
[인식된 텍스트]

## ✅ 교정된 텍스트
[맞춤법이 교정된 텍스트]

## 📝 수정 내역
[수정된 부분에 대한 설명]
"""
                
                # 이미지 분석 요청
                response = model.generate_content([prompt, image])
                
                # 결과 표시
                st.success("✨ 분석이 완료되었습니다!")
                st.markdown("---")
                st.markdown(response.text)
                
                # 다운로드 버튼
                st.download_button(
                    label="📥 결과 다운로드 (TXT)",
                    data=response.text,
                    file_name="ocr_correction_result.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ 오류가 발생했습니다: {str(e)}")
                st.info("API 키가 올바른지 확인하고, Gemini API가 활성화되어 있는지 확인하세요.")

# 사이드바 정보
with st.sidebar:
    st.header("ℹ️ 사용 방법")
    st.markdown("""
    1. **API 키 설정**
       - Google AI Studio에서 API 키 발급
       - Streamlit secrets에 추가
    
    2. **이미지 준비**
       - 텍스트가 선명한 이미지 사용
       - 조명이 밝고 글자가 명확한 사진
    
    3. **분석 실행**
       - 이미지 업로드 또는 촬영
       - 분석 버튼 클릭
    
    4. **결과 확인**
       - 원본 텍스트와 교정 결과 비교
       - 필요시 TXT 파일로 다운로드
    """)
    
    st.markdown("---")
    st.markdown("**💡 팁**")
    st.info("""
    - 손글씨보다 인쇄된 텍스트가 더 정확합니다
    - 이미지가 흔들리지 않게 촬영하세요
    - 텍스트가 잘리지 않도록 주의하세요
    """)
