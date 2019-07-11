# ---------------------------------4. HAFTA, 5. ODEV---------------------------------
tChars = ['ç', 'ö', 'ğ', 'ü', 'ı', 'Ş', 'Ç', 'Ö', 'Ğ', 'Ü', 'İ', 'š', 'Š', 'è', 'é', 'æ']

eChars = ['c', 'o', 'g', 'u', 'i', 'S', 'C', 'O', 'G', 'U', 'I', 's', 'S', 'e', 'e', 'ae']

futbolcular = open('futbolcular.txt', 'r', encoding='cp1254')
fin = open('Names_in_English.txt', 'a+')
teamList = futbolcular.read()
with open('Names_in_English.txt', 'w') as fin:
        for letter in tChars:
                if letter in teamList:
                        names = teamList.replace(letter, eChars[tChars.index(letter)])
                        fin.write(names)

type(names)