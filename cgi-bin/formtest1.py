#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
form = cgi.FieldStorage() # cgiオブジェクト作成
v1 = form.getfirst('value1') # nameがvalue1の値を取得
v2 = form.getfirst('value2') # nameがvalue2の値を取得

#入力値が数字ならその積を返す関数
def times(a, b):
    try:
        a=int(a)
        b=int(b)
        return str(a*b)
    except ValueError:
        return('数値じゃないので計算できません(>_<)')

# ブラウザに戻すHTMLのデータ
print("Content-Type: text/html")
print()
htmlText = '''
<!DOCTYPE html>
<html>
    <head><meta charset="shift-jis" /></head>
<body bgcolor="lightyellow">
    <h1>こんにちは</h1>
    <p>入力値の積は&nbsp; %s<br/></p>
    <hr/>
    <a href="../form1.html">戻る</a>　
</body>
</html>
'''%(times(v1,v2,v3)) # 入力値の積を%sの箇所に埋める
print( htmlText.encode("cp932", 'ignore').decode('cp932') )