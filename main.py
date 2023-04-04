"""Member class is for storing member information, has two child class
  SingleClubMember and MultiClubMember"""

import datetime
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def check_in(self, Club ):
        # self.club = Club.__name__
        pass  # implemented in child classes
        return

class SingleClubMember(Member):
    def __init__(self, member_id, name, club):
        self.member_id = member_id
        self.name = name
        self.club = club

    def check_in(self, club):
        if club.name != self.club.name:
            print(f"Alert! {self.name} is a member of {self.club.name}.Please check in at your club{self.club.name}.")
            return False
        else:
            print(f"Welcome {self.name} to {club.name}!")
            return True


class MultiClubMember(Member):
    def __init__(self, member_id, name, membership_points=0):
        self.member_id = member_id
        self.name = name
        self.membership_points = membership_points

    def check_in(self, club):
        self.membership_points += 1
        print(f"Welcome {self.name} to {club.name}! Membership points: {self.membership_points}")
        return True
#added from today
class Club():
    def __init__(self,Name,Address):
        self.name = Name
        self.address = Address


class FitnessCenter:
    def __init__(self):
        self.members = []
        self.clubs = [Club("Club A", "Address A"), Club("Club B", "Address B"), Club("Club C", "Address C"),
                      Club("Club D", "Address D")]
        self.promotion_start_date = datetime.date(2023, 4, 1)
        self.promotion_end_date = datetime.date(2023, 4, 30)

    # def add_member(self):
    #     name = input("Enter name of member: ")
    #     membership_type = input("Enter membership type (Single/Multi): ").lower()
    #     member_id = len(self.members) + 1
    #     if membership_type == "single":
    #         club = self.choose_club()
    #         member = SingleClubMember(member_id, name, club)
    #     else:
    #         member = MultiClubMember(member_id, name)
    #     self.members.append(member)
    #     print(f"{name} has been added as a {membership_type}-club member with ID {member_id}.")

    def add_member(self):
        name = input("Enter name of member: ")
        membership_type = input("Enter membership type (Single/Multi): ").lower()
        member_id = len(self.members) + 1
        if membership_type == "single":
            club = self.choose_club()
            member = SingleClubMember(member_id, name, club)
        else:
            member = MultiClubMember(member_id, name)
        if self.is_promotion_period():
            print("You have signed up during the promotion period!")
            if isinstance(member, SingleClubMember):
                cost = 40
            else:
                cost = 80
            print(f"Total cost: ${cost}")
        else:
            print(f"{name} has been added as a {membership_type}-club member with ID {member_id}.")
            if isinstance(member, SingleClubMember):
                cost = 50
            else:
                cost = 100
            print(f"Total cost: ${cost}")
        self.members.append(member)


    def is_promotion_period(self):
        today = datetime.date.today()
        return self.promotion_start_date <= today <= self.promotion_end_date

    def remove_member(self):
        # print(self.members)
        member_id = int(input("Enter ID of member to remove: "))
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member with ID {member_id} has been removed.")
                return
        print(f"No member found with ID {member_id}.")

    def display_member_info(self):
        member_id = int(input("Enter ID of member to display: "))
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member ID: {member.member_id}")
                print(f"Name: {member.name}")
                if isinstance(member, SingleClubMember):
                    print(f"Membership Type: Single-Club")
                    print(f"Club: {member.club.name}")
                else:
                    print(f"Membership Type: Multi-Club")
                    print(f"Points: {member.membership_points}")
                return
        print(f"No member found with ID {member_id}.")
    def choose_club(self):
     while True:
        print("Choose a club:")
        for i, club in enumerate(self.clubs):
            print(f"{i + 1}. {club.name} - {club.address}")
        choice = input()
        try:
            index = int(choice) - 1
            if index >= 0 and index < len(self.clubs):
                return self.clubs[index]
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid choice. Please choose again.")

    def check_in_member(self):
        member_id = int(input("Enter ID of member to check in: "))
        for member in self.members:
            if member.member_id == member_id:
                if isinstance(member, SingleClubMember):
                    club = member.club
                else:
                    club = self.choose_club()
                if not member.check_in(club):
                    print("Check-in failed.")
                    self.check_in_member()  # prompt again to check in
                else:
                    print("Check-in successful.")
                return
        print(f"No member found with ID {member_id}.")

    def generate_bill(self):
     member_id = int(input("Enter ID of member to generate bill: "))
     for member in self.members:
        if member.member_id == member_id:
            print(f"Member ID: {member.member_id}")
            print(f"Name: {member.name}")
            if isinstance(member, SingleClubMember):
                print(f"Membership Type: Single-Club")
                print(f"Club: {member.club.name}")
                cost = 50  # cost for single-club membership
            else:
                print(f"Membership Type: Multi-Club")
                print(f"Points: {member.membership_points}")
                cost = 100  # cost for multi-club membership
                if member.membership_points > 10:
                    discount = 0.1  # 10% discount for more than 10 points
                    cost *= (1 - discount)
                    print(f"You have received a 10% discount for having more than 10 points.")
            print(f"Total cost: ${cost}")
            return
     print(f"No member found with ID {member_id}.")

    def run(self):
     while True:
        print("What would you like to do?")
        print("1. Add member")
        print("2. Remove member")
        print("3. Display member information")
        print("4. Check in member")
        print("5. Generate bill")
        print("6. Quit")
        choice = input()
        if choice == "1":
            self.add_member()
        elif choice == "2":
            self.remove_member()
        elif choice == "3":
            self.display_member_info()
        elif choice == "4":
            self.check_in_member()
        elif choice == "5":
            self.generate_bill()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
fitness_center = FitnessCenter()
fitness_center.run()




