def get_num_words(text):
    words=text.split()
    wordnr=len(words)
    return wordnr
def get_count_char(text):
    text=text.lower()
    char_list=set()
    for char in text:
        if char not in char_list:
            char_list.add(char)
    charac={}
    for char in char_list:
        charac[char]=text.count(char)
    return charac
def sort_list(char_list):
    def sort_on(items):
        return items["num"]
    charac=[]
    for char in char_list:
        if char.isalpha():
            charac.append({"char":char,"num":char_list[char]})
    charac.sort(reverse=True, key=sort_on)
    return charac
