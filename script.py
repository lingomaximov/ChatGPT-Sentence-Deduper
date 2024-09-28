final = []

seen_words = []

dupes = 0

with open("words.txt", encoding="utf8") as file:
    text = file.readlines()

    mode = " - "

    for line in text:
        if "–" in line:
            line = line.replace("–", "-")
        split = line.split(mode)
        if split[0] not in seen_words:
            seen_words.append(split[0])
            final.append(line)
        else:
            dupes += 1

with open("cleaned.txt", "w+", encoding="utf8") as file:
    file.writelines(final)

print(f"Successfully removed {dupes} dupes.")