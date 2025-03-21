def count_text_words(file_contents):
    separate = file_contents.split()
    return len(separate)

def count_letters(file_contents):
    lowered = file_contents.lower()
    how_many = {}
    for i in lowered:
        if i in how_many:
            how_many[i] += 1
        else:
            how_many[i] = 1
    return how_many 

def sorted_charcount(count_letters):
    char_list = []
    for char, count in count_letters.items():
        char_list.append({'char': char, 'count': count}) #creating a new dictionary for each iteration
    
    #helper function to sort by count value
    def sort_on(items):
        return items['count']

    char_list.sort(reverse=True, key=sort_on)

    return char_list 
