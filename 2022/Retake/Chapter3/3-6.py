guest_list = ['daisy', 'sophia', 'zohan', 'tyler', 'tejas', 'zoe']

guest = guest_list

def display_guests ():
    for guest in guest_list:
        print(f"Hey {guest.title()}, you're invited to my dinner party!")
    return

print(f"\n")

display_guests()
print(f"\nIt turns out that {guest_list[-1].title()} can't make it!\n")

guest_list[-1] = "athena"

display_guests()
print(f"\nGuess what? I found a bigger dinner table. I'm inviting more guests!\n")

guest_list.insert(0, 'ada')
guest_list.insert(3, 'james')
guest_list.append('Korey')

print(f"\n")
display_guests()