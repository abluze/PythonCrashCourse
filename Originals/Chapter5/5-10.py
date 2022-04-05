current_users = ['void','pixxel','admin','fliponpc','spectros']
new_users = ['turbo','pixxel','att9ck','spectros','pinappl']

for new_user in new_users:
  if new_user in current_users:
    print("Your username is unavailable. Please choose a new one.")
  else:
    print("Your username is available, you may continue.")