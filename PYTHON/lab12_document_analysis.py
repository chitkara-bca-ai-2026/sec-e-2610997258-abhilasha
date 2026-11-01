# Lab 12 - Document Analysis System

print("==================================================")
print("             DOCUMENT ANALYSIS REPORT             ")
print("==================================================")

sentence = input("Enter a sentence: ")

total_chars = len(sentence)
words = sentence.split()
total_words = len(words)
vowels = "aeiouAEIOU"
total_vowels = sum(1 for char in sentence if char in vowels)
total_consonants = sum(1 for char in sentence if char.isalpha() and char not in vowels)
total_digits = sum(1 for char in sentence if char.isdigit())
total_spaces = sum(1 for char in sentence if char.isspace())
total_special = sum(1 for char in sentence if not char.isalnum() and not char.isspace())
total_letters = total_vowels + total_consonants
if total_letters > 0:
    vowel_percentage = (total_vowels / total_letters) * 100
else:
    vowel_percentage = 0.0
print(f"Sentence: {sentence}")
print(f"Total characters: {total_chars}")
print()
print("--- Character Breakdown ---")
print(f"Words: {total_words}")
print(f"Vowels: {total_vowels}")
print(f"Consonants: {total_consonants}")
print(f"Digits: {total_digits}")
print(f"Spaces: {total_spaces}")
print(f"Special characters: {total_special}")
print()
print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print("==================================================")
print("Analysis Complete!")
print("==================================================")