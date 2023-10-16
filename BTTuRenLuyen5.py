def problem2():
    """Solve problem 2"""
    def countUpper(s):
        """Count the number of uppercase letters in string s"""
        count = 0
        for i in range(len(s)):
            if s[i].isupper():
                count += 1
        return count

    def countLower(s):
        """Count the number of lowercase letters in string"""
        count = 0
        for i in range(len(s)):
            if s[i].islower():
                count += 1
        return count

    def countDigit(s):
        """Count the number of digits in string"""
        count = 0
        for i in range(len(s)):
            if s[i].isnumeric():
                count += 1
        return count

    def countSpecial(s):
        """Count the number of special characters in string"""
        count = 0
        for i in range(len(s)):
            if not s[i].isalnum() and s[i] != " ":
                count += 1
        return count

    def countSpace(s):
        """Count the number of whitespaces in string"""
        count = 0
        for i in range(len(s)):
            if s[i] == " ":
                count += 1
        return count

    def isVowel(c):
        """Check if a character is a vowel"""
        if c in ("a", "e", "i", "o", "u"):
            return True
        return False

    def countVowel(s):
        """Count the number of vowels in string"""
        count = 0
        for i in range(len(s)):
            if isVowel(s[i].lower()):
                count += 1
        return count

    # def countConsonant(s):
    #     """Count the number of consonants in string"""
    #     count = 0
    #     for i in range(len(s)):
    #         if s[i].isalpha() and not isVowel(s[i]):
    #             count += 1
    #     return count

    s = input("Nhập chuỗi không dấu: ")
    print("Số ký tự in hoa:", countUpper(s))
    print("Số ký tự in thường:", countLower(s))
    print("Số ký tự là chữ số:", countDigit(s))
    print("Số ký tự đặc biệt:", countSpecial(s))
    print("Số ký tự là khoảng trắng:", countSpace(s))
    print("Số ký tự là nguyên âm:", countVowel(s))
    print("Số ký tự là phụ âm:", countUpper(s) + countLower(s) - countVowel(s))


def problem3():
    """Solve problem 3"""
    def NegativeNumberInString(s):
        arr = s.split("-")
        print(arr)
        negativeNum = []
        for word in arr:
            if word != '':
                if word.isnumeric() and eval(word) != 0:
                    negativeNum.append(eval(word) * -1)
                elif word[0].isnumeric():
                    i = 0
                    num = ""
                    while i < len(word) and word[i].isnumeric():
                        num += word[i]
                        i += 1
                    if eval(num) != 0:
                        negativeNum.append(-1 * eval(num))
        return negativeNum

    s = input("Nhập chuỗi: ")
    print(NegativeNumberInString(s))


def problem4():
    """Solve problem 4"""
    def optimal(s):
        """Remove unnecessary white spaces and capitalize the first letter of each word"""
        s = s.strip()
        x = ""
        for word in (s.split(' ')):
            if word != '':
                x += word + " "
        s = x.strip().title()
        return s

    phrase = input("Nhập chuỗi danh từ: ")
    print("Chuỗi danh từ tối ưu:", optimal(phrase))


print("BÀI TẬP TỰ RÈN LUYỆN (CHUỖI)".center(50, "*"))
print("""2. Viết chương trình cho phép nhận vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ in hoa
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là nguyên âm
- Bao nhiêu chữ là phụ âm""")
print("""3. Viết một hàm đặt tên là NegativeNumberInStrings(str).
Hàm này có đối số truyền vào là một chuỗi bất kỳ.
Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
vd:   Input:  'abc-5xyz-12k9l--p'
      Output: '-5 -12'""")
print("""4. Viết chương trình tối ưu Chuỗi danh từ:
vd:   Input:  '      TRần     duY     thAnH    '
      Output  'Trần Duy Thanh'""")
print("0. Kết thúc")
while True:
    n = int(input("Nhập lựa chọn: "))
    match n:
        case 2:
            problem2()
        case 3:
            problem3()
        case 4:
            problem4()
        case 0:
            print("Kết thúc chương trình")
            exit()