from cv import CV


def main():
    name = input("Enter your name: ")
    cv = CV()

    choice = input("Do you want to add skills? (yes/no): ")
    if choice.lower() == "yes":
        cv.add_skill()

    cv.add_education()
    cv.add_experience()

    print("\n")
    print("CV for", name)
    cv.display_cv()


if __name__ == "__main__":
    main()