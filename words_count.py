word = input("What on your mind today?: ")
def countword():
    count = len(word) - word.count(" ")
    print (f"oh nice, you just told me what's on your mind in {count} words!")
countword()