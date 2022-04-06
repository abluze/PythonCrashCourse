guest_list = ['daisy', 'sophia', 'zohan', 'tyler', 'tejas', 'zoe']

guest = guest_list
for guest in guest_list:
    print(f"Hey {guest.title()}, you're invited to my dinner party!")

print(f"\nIt turns out that {guest_list[-1].title()} can't make it!\n")

guest_list[-1] = "athena"

for guest in guest_list:
    print(f"Hey {guest.title()}, you're invited to my dinner party!")