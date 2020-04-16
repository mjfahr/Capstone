from csv_creation import *
import nltk

def create_section_csv(file_name, file_directory, output_directory):
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
    write_section_csv(unfiltered_sections, output_directory)

def create_section_stat_csv(file_name, file_directory, output_directory):
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

    # Write CSV for (Index, Section_Index, Word, Frequency)
    write_section_statistics_csv(filtered_sections, output_directory)