import os

# 템플릿 구조 정의
base_path = "/mnt/data/docsify-template"
files = {
    "index.html": """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Docs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- Docsify -->
    <script src="https://unpkg.com/docsify/lib/docsify.min.js"></script>
    
    <!-- KaTeX for math rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/docsify-katex@1.0.3/dist/docsify-katex.min.js"></script>
  </head>
  <body>
    <div id="app">Loading...</div>
    <script>
      window.$docsify = {
        name: 'My Docs',
        repo: '',
        loadSidebar: true,
      };
    </script>
  </body>
</html>
""",
    "README.md": """# 수식 테스트 문서

이 문서는 Obsidian에서 작성된 마크다운을 기반으로 하며, Docsify + KaTeX를 통해 GitHub Pages에서 수식도 표현됩니다.

## 인라인 수식 예시

피타고라스 정리: $a^2 + b^2 = c^2$

## 블록 수식 예시

$$
\\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{-\\frac{(x - \\mu)^2}{2\\sigma^2}}
$$
""",
    "_sidebar.md": """- [홈](/)
- [수식 예제](README.md)
- [추가 문서](sample.md)
""",
    "sample.md": """# 추가 문서 예제

여기에도 수식이 포함될 수 있습니다.

예: $E = mc^2$
"""
}

# 디렉토리 및 파일 생성
os.makedirs(base_path + "/images", exist_ok=True)
for filename, content in files.items():
    with open(os.path.join(base_path, filename), "w", encoding="utf-8") as f:
        f.write(content)

"템플릿 생성 완료"
