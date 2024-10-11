with open("Shakespear.txt", mode="r") as s_file:
    all_words = []
    for line in s_file.readlines():
        stripped_string = line.strip()
        words  = stripped_string.split(" ")
        all_words +=words
    unique_words = set(all_words)
    print(len(unique_words))

    with open("unique_words.text", mode="w") as write_file:
        for item in sorted(unique_words):
            write_file.write(item)
            write_file.write('\n')


print("finished!")