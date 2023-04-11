dict_trans = {"А":"A", "Б":"B", "В":"V", "Г":"G", "Д":"D", 
         "Е":"E", "Ё":"E", "Ж":"ZH", "З":"Z", "И":"I",
         "Й":"I", "К":"K", "Л":"L", "М":"M", "Н":"N", 
         "О":"O", "П":"P", "Р":"R", "С":"S", "Т":"T", 
         "У":"U", "Ф":"F", "Х":"KH", "Ц":"TS", "Ч":"CH",
         "Ш":"SH", "Щ":"SHCH", "Ы":"Y", "Ь":"", "Ъ":"IE",
         "Э":"E", "Ю":"U", "Я":"YA"}

def translit(text: str):
    rez = ""
    for i_ch in text:
        if i_ch.isalpha:
            if i_ch.islower():
                if i_ch.upper() in dict_trans:
                    rez += dict_trans.get(i_ch.upper()).lower()
                else:
                    rez += i_ch
            else:
                if i_ch in dict_trans:
                    rez += dict_trans.get(i_ch)
                else:
                    rez += i_ch
        else:
            rez += i_ch

    return rez

def trancate(text: str):
    if len(text) <= 15:
        return text
    arr = text.split("_")
    if len(arr) == 4:
        arr[1] = arr[1][:7]
        rez = "_".join(arr)
        return rez
    else:
        return text[:15]