def main():
    name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56, "jordan": 23}
    print(get_names_by_age_limit(name_to_age, 30))

    
def get_names_by_age_limit(name_to_age, age_limit):
    return (name for name, age in name_to_age.items() if age <= age_limit)


if __name__ == '__main__':
    main()
