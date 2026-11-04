weight = 60
reps = 10
sets = 3

# ↓ここに計算と表示を書く
print(weight * reps * sets)

def check_weight(kg):
    if kg >= 100:
        return '上級者'
    elif kg >= 60:
        return '中級者'
    else:
        return '初心者'

print(check_weight(120))
print(check_weight(70))
print(check_weight(40))