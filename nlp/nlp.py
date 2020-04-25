from csv_creation import *
import nltk

# Uncomment when initially downloading packages
# nltk.download('averaged_perceptron_tagger')

file_name = "transformers"
file_directory = "data/"
output_directory = "csv/"

# Opens text file
file = open(file_directory + file_name + '.txt', "r", encoding="utf8")
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

# Write CSV for (Index, Section_Index, File_Name)
write_section_csv(unfiltered_sections)


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

# Write CSV for (Index, Section_Title, Content)
section_df = pd.DataFrame(list(zip(section_titles, filtered_sections)), columns=['Section_Title', 'Content'])
section_df.index.name = "Index"
section_df.to_csv(output_directory + "section.csv")

# Write CSV for (Index, Section_Index, Word, Frequency)
write_section_statistics_csv(filtered_sections)

# Replace \n with a space
text = text.replace("\\n", " ")

# Tokenize text
text_tokens = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in text_tokens if not w in stop_words]
filtered_tokens = [word for word in filtered_tokens if word.isalnum()]


# Write CSV for (Index, Word, Frequency)
write_document_word_statistics(filtered_tokens)

# Write CSV for (Index, Word, Frequency)
# Only writes top 10% of words based on frequency
write_important_document_word_statistics(filtered_tokens)

# Write CSV for (Index, Word, Frequency)
write_noun_document_word_statistics(filtered_tokens)

# Write CSV for (Index, Section_Index, Total Word Frequency)
write_section_total_word_count(filtered_sections)







