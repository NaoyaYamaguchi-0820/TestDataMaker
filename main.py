import csv
import random
import string
import datetime

# 社員番号生成
def createEmployeeNum():
    return random.randint(0,99999)

# 名字生成
def createLastName():

    # returnするlist。0番目に漢字、1番目にひらがなを入れる。
    LastNameList = ['', '']

    # 1文字目を生成
    with open('LastNameOne.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        LastNameList[0] = LastNameList[0] + lists[index][0]
        LastNameList[1] = LastNameList[1] + lists[index][1]

    # 2文字目を生成
    with open('LastNameTwo.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        LastNameList[0] = LastNameList[0] + lists[index][0]
        LastNameList[1] = LastNameList[1] + lists[index][1]

    return LastNameList

# 名前生成
def createFirstName():

    # returnするlist。0番目に漢字、1番目にひらがなを入れる。
    FirstNameList = ['', '']

    # 1文字目を生成
    with open('FirstNameOne.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        FirstNameList[0] = FirstNameList[0] + lists[index][0]
        FirstNameList[1] = FirstNameList[1] + lists[index][1]

    # 2文字目を生成
    with open('FirstNameTwo.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        FirstNameList[0] = FirstNameList[0] + lists[index][0]
        FirstNameList[1] = FirstNameList[1] + lists[index][1]

    return FirstNameList

# 電話番号生成
def createPhoneNumber():

    result = ''

    result = '0' + str(random.randint(7,9)) + '0-' + str(random.randint(1000, 9999)) + '-' + str(random.randint(1000, 9999))

    return result

# メールアドレス生成
def createEmail():
    result = ''
    with open('Email.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        result = result + lists[index][0] + '@example.com'
        return result

# パスワードを生成
def createPassword():
    n = random.randint(8, 16)
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

# 誕生日を生成
def createBirthday():
    return str(random.randint(1900, 2020)) + '-' + str(random.randint(1, 12)) + '-' +  str(random.randint(1, 31))

# 性別を生成
def createGender():
    result = ''
    with open('Gender.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        result = lists[index][0]
        return result


# 部署を生成
def createSection():
    result = ''
    with open('Section.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        result = lists[index][0]
        return result

# 自己紹介を生成
def createJikoshokai():
    result = ''
    with open('Jikoshokai.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        lists = [row for row in reader]

        # 何行目のデータを採用するか決定
        index = random.randint(0, len(lists)-1)

        result = lists[index][0]
        return result

# Main
with open('result.csv', 'w', encoding='Shift_JIS', newline='') as f:

    writer = csv.writer(f)

    for i in range(100):

        data = []
        data.append(createEmployeeNum())
        LastName = createLastName()
        FirstName = createFirstName()
        data.append(LastName[0])
        data.append(FirstName[0])
        data.append(LastName[1])
        data.append(FirstName[1])
        data.append(createPhoneNumber())
        data.append(createEmail())
        data.append(createPassword())
        data.append(createBirthday())
        data.append(createGender())
        data.append(createSection())
        data.append(createJikoshokai())

        writer.writerow(data)