usernames = ['void','pixxel','admin','fliponpc','spectros']
for username in usernames:
  if username == 'admin':
    print(f"Hello {username.title()}, would you like a status report?")
  else:
    print(f"Hello {username.title()}, thanks for logging in again!")