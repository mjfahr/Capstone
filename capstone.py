from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import sqlite3
import matplotlib
import nltk

file_name = "transformers"

# Connects with sqlite database
conn = sqlite3.connect(file_name + '.db')
c = conn.cursor()

# Opens text file
file = open(file_name + '.txt', "r", encoding="utf8")
text = file.read()

# Add sections and section titles to list
unfiltered_sections = []
section_titles = []
section_index = 0
while 1:
    tag_start_index = text.find('\\ntag:', section_index)
    tag_end_index = text.find('\n', tag_start_index + 1)
    if tag_start_index == -1:
        break
    else:
        unfiltered_sections.append(text[section_index:tag_start_index])
        section_titles.append(text[tag_start_index:tag_end_index])
        section_index = tag_end_index

# Fixes start of unfiltered section from containing new lines
for i in range(0, len(unfiltered_sections)):
    while unfiltered_sections[i][0:1] == "\n":
        unfiltered_sections[i] = unfiltered_sections[i][2::]


# Grab files for table from each section
# for i in range(0, len(unfiltered_sections)):
#     while 1:
#         start_index = unfiltered_sections[i].find('[file')
#         end_index = unfiltered_sections[i].find(']')
#
#         if start_index == -1:
#             break
#         print(text[start_index:end_index])


# Create filtered sections for tokenizing
filtered_sections = []
for i in range(0, len(unfiltered_sections)):
    section = unfiltered_sections[i]
    section = section.replace("\n", "")
    section = section.replace("\\n", " ")
    filtered_sections.append(section)

# Remove \ntag from section titles
for i in range(0, len(section_titles)):
    section_titles[i] = section_titles[i].replace("\\ntag:", "")




# Replace \n with a space
text = text.replace("\\n", " ")



# Tokenize text
text_tokens = word_tokenize(text)
print("Tokenized:\n", text_tokens, "\n")


# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in text_tokens if not w in stop_words]
print("Filtered:\n", filtered_tokens, "\n")

print(len(filtered_tokens))
print(sorted(set(filtered_tokens)))

# Frequency Distribution
fdist = FreqDist(filtered_tokens)
print(fdist)
print(fdist.most_common(50))


