text=input(("Enter a sentence:"))
text=text.split()
bigWordLen=0
for wrd in text:
    wrdLen=len(wrd)
    if wrdLen>bigWordLen:
        bigWordLen=wrdLen
print("\nLargest Word EVER!:")
for wrd in text:
    wrdLen=len(wrd)
    if wrdLen==bigWordLen:
        print(wrd)