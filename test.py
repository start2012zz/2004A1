import re

def countingSort(l1, l2):
    l1_store = []
    for word in l1:
        temp = [0]*26
    for letter in word:
        ind = ord(letter) - ord('a')
        temp[ind] += 1
        l1_store.append(temp)

    l2_store = []
    for word in l2:
        temp = [0]*26
    for letter in word:
        ind = ord(letter) - ord('a')
        temp[ind] += 1
        l2_store.append(temp)

    res = []
    for ind, val1 in enumerate(l1_store):
        for val2 in l2_store:
            if val1 == val2:
                res.append(l1[ind])
            break
    return res

def check_max_word_size(words):
    m_length = 0
    for word in words:
        if len(word) > m_length:
            m_length=len(word)

    return m_length

def set_same_size(words, max_size):
    new_list=[]
    for word in words:
        new_arr = ['.' * (max_size - len(word))]
        new_list.append(word.lower()+''.join(new_arr))

    return new_list

def radix_sort(words, max_size, index):
    if(index == max_size+1):
        return words
    dic = []
    dict_letters = {}
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_index=0
    tmp_list = []

    for x in range(26):
        dict_letters.update({letters[letter_index]:(x+1)})
        letter_index+=1
        dict_letters.update({'.':1000})
    for word in words:
        if(dict_letters[word[max_size-index].lower()] < 1000 ):
            dic.append([word.lower(), dict_letters[word[max_size-index].lower()] ])
    for x, y in dic:
        tmp_list.append([x,y])
        tmp_list.sort(key=lambda x: x[1])
    return_list=[]
    for item in tmp_list:
        return_list.append(item[0])

    for item in words:
        if item not in return_list:
            return_list.append(item.lower())

    return radix_sort(return_list, max_size, index+1)

l1 = ['spot', 'tops', 'dad', 'simple', 'dine', 'cats']
l2 = ['pots', 'add', 'simple', 'dined', 'acts', 'cast']

res = countingSort(l1,l2)
max_size = check_max_word_size(res)
new_list = set_same_size(res, max_size)
new_list = radix_sort(new_list, max_size-1, 0)
index = 0
for word in new_list: # Removing dots in word
    new_list[index]= re.sub('[.]', '', word)
    index+=1
print(new_list)