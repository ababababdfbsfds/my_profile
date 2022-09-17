import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/ababababdfbsfds/introduce" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["blue", "red"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이성은")
write("description", "대천중학교 3학년 5반")
write("button", "github 링크")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2007년 08월 27일",
  "하고픈 언어": "C언어",
  "선호 음식": "치킨",
  "선호 게임": " TFT "
}
information(informations)
