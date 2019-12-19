from prac6cp1404.programming_language import ProgrammingLanguage

programming_language = []

java = ProgrammingLanguage("Java", "Static", True, 1995)
programming_language.append(java)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
programming_language.append(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
programming_language.append(visual_basic)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
programming_language.append(ruby)
C = ProgrammingLanguage("C++", "Static", False, 1995)
programming_language.append(C)

print("The dynamically typed language are:")
for item in programming_language:
    value = item.is_dynamic()
    if value:
        print(item.get_name())


print(java)
print(C)
print(python)
print(visual_basic)
print(ruby)

