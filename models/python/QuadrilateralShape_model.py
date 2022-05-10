'''
x-y 平面上の 4 つの点、A（ax,ay）、B（bx,by）、C（cx,cy）、D（dx,dy）が与えられるので、ABCD の形を文字列で返す、getShapeType という関数を作成
'''

import math

# 座標
class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

# 3点が同一直線上にあるかどうかを判定
def OnLine(p1, p2, p3):
    return p1.y * ( p2.x - p3.x ) + p2.y * ( p3.x - p1.x ) + p3.y * ( p1.x - p2.x )


# 線分
class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    # 線分の長さ
    def length(self):
        return math.sqrt((self.startPoint.x - self.endPoint.x) ** 2 + (self.startPoint.y - self.endPoint.y) ** 2)

    # 線分の傾き
    def slope(self):
        if self.endPoint.x - self.startPoint.x  == 0:
            return None  # y軸に平行
        else:
            return (self.endPoint.y - self.startPoint.y) / (self.endPoint.x - self.startPoint.x)


# 角度
# 線分から角度を求める
def obtainAngle(length_a, length_b, length_c):
    # 処理1:余弦定理でcosAを求める
    cosA = (( length_b ** 2) + ( length_c ** 2) - (length_a ** 2)) / (2 * length_b * length_c)
    # 処理2:arccos(cosA)
    return round(math.degrees(math.acos(cosA)))

def getShapeType(ax,ay,bx,by,cx,cy,dx,dy):
    #ここから書きましょう

    # Pointオブジェクト
    # 座標
    pointA = Point(ax, ay)
    pointB = Point(bx, by)
    pointC = Point(cx, cy)
    pointD = Point(dx, dy)

    # 3点が同一直線上にあるかどうかを判定
    onLineA = OnLine(pointB,pointC,pointD)
    onLineB = OnLine(pointC,pointD,pointA)
    onLineC = OnLine(pointD,pointA,pointB)
    onLineD = OnLine(pointA,pointB,pointC)

    # 点と点を結んだ直線状に点があるときを除外する
    if(onLineA == False or onLineB == False or onLineC == False or onLineD == False):
        return "not a quadrilateral"

    # Lineオブジェクト
    # 線分
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)
    lineCD = Line(pointC, pointD)
    lineDA = Line(pointD, pointA)

    # 対角線
    lineAC = Line(pointA, pointC)
    lineBD = Line(pointB, pointD)

    # 線分の長さ
    lengthAB = Line.length(lineAB)
    lengthBC = Line.length(lineBC)
    lengthCD = Line.length(lineCD)
    lengthDA = Line.length(lineDA)

    # 対角線の長さ
    lengthAC = Line.length(lineAC)
    lengthBD = Line.length(lineBD)

    # 線分の傾き
    slopeAB = Line.slope(lineAB)
    slopeBC = Line.slope(lineBC)
    slopeCD = Line.slope(lineCD)
    slopeDA = Line.slope(lineDA)

    # 対角線の傾き
    slopeAC = Line.slope(lineAC)
    slopeBD = Line.slope(lineBD)

    # 同じ座標に位置する点があるとき、つまり線分の長さが0のときを除外する
    if lengthAB == 0 or lengthBC == 0 or lengthCD == 0 or lengthDA == 0 or lengthAC == 0 or lengthBD == 0:
        return "not a quadrilateral"

    # 角度
    angleA = obtainAngle(lengthBD, lengthDA, lengthAB)
    angleB = obtainAngle(lengthAC, lengthAB, lengthBC)
    angleC = obtainAngle(lengthBD, lengthBC, lengthCD)
    angleD = obtainAngle(lengthAC, lengthCD, lengthDA)

    # デバッグ用ログ
    print("長さ")
    lengths = [lengthAB, lengthBC, lengthCD, lengthDA, lengthAC, lengthBD]
    print(lengths)

    print("傾き")
    slopes = [slopeAB, slopeBC, slopeCD, slopeDA, slopeAC, slopeBD]
    print(slopes)

    print("角度")
    angles = [angleA, angleB, angleC, angleD]
    print(angles)

    # すべての辺の長さが等しい
    if lengthAB == lengthBC and lengthBC == lengthCD and lengthCD == lengthDA and lengthDA == lengthAB :
        if angleA == 90 and angleB == 90 and angleC == 90 and angleD == 90:
            # すべての辺の長さが等しい　かつ　すべての角が直角
            return "square（正方形）"
        else:
            # すべての辺の長さが等しい　かつ　角が直角でない
            return "rhombus（ひし形）"

    elif slopeAB == slopeCD and slopeBC == slopeDA :

        if angleA == 90 and angleB == 90 and angleC == 90 and angleD == 90:
            # 向かい合う二組の辺が平行　かつ　すべての角が直角
            return "rectangle（長方形）"
        else:
            # 向かい合う二組の辺が平行　かつ　角が直角でない
            return "parallelogram（平行四辺形）"

    elif (slopeAB == slopeCD or slopeBC == slopeDA) and (angleA + angleB + angleC + angleD == 360):
        # 向かい合う一組の辺が平行
        return "trapezoid（台形）"


    elif lengthAB == lengthBC and lengthCD == lengthDA or lengthDA == lengthAB and lengthBC == lengthCD:
        # 隣り合う辺の長さが等しい
        return "kite（凧）"

    else:
        # その他の4本の直線で囲まれた平面上の図形
        return "other（その他）"
