def main():
    location = input("Are you studying in Goa?yes/no: ").lower()

    if location == "yes":
        studying = input("Are you in the 13 group?yes/no: ").lower()

        if studying == "yes":
            group_number = input("Which group number are you in? ")

            if group_number == "13":
                mentor = input("Is Gabriel your mentor?yes/no: ").lower()

                if mentor == "yes":
                    print("Great! It seems we're in the same group, and Gabriel is our mentor.")
                else:
                    print("Hmm, it seems Gabriel is not your mentor. I must say, you're not telling the truth.")
            else:
                print("Hmm, you're not in group 13. I'm onto you! .")
        else:
            print("You're not in the 13 group, are you?.")
    else:
        print("So, you're not studying in Goa. Interesting!.")


if __name__ == "__main__":
    main()
