from django.shortcuts import render
from django.http import HttpResponse
from .models import User




# User.objects.create(email='student3@mail.ru', first_name='student3_fname', last_name='student3_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student4@mail.ru', first_name='student4_fname', last_name='student4_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student5@mail.ru', first_name='student5_fname', last_name='student5_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student6@mail.ru', first_name='student6_fname', last_name='student6_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student7@mail.ru', first_name='student7_fname', last_name='student7_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student8@mail.ru', first_name='student8_fname', last_name='student8_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student9@mail.ru', first_name='student9_fname', last_name='student9_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student10@mail.ru', first_name='student10_fname', last_name='student10_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student11@mail.ru', first_name='student11_fname', last_name='student11_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student12@mail.ru', first_name='student12_fname', last_name='student12_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)
# User.objects.create(email='student13@mail.ru', first_name='student13_fname', last_name='student13_lname', password='pbkdf2_sha256$216000$wGHVMtB8d6dy$9qIamB4IQWzzWvm+CT5mUXhAsSxuE+D3a+vZa0D3M6Y=', is_student=True)