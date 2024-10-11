""" py -m venv Environment
 Environment\Scripts\activate.bat
 PS C:\Users\Lenovo\Desktop\Django> cd DJANGO-Class
PS C:\Users\Lenovo\Desktop\Django\DJANGO-Class> Environment\scripts\activate.bat
PS C:\Users\Lenovo\Desktop\Django\DJANGO-Class> pip install Django
Requirement already satisfied: Django in c:\users\lenovo\appdata\local\programs\python\python312\lib\site-packages (5.1)Requirement already satisfied: asgiref<4,>=3.8.1 in c:\users\lenovo\appdata\local\programs\python\python312\lib\site-packages (from Django) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in c:\users\lenovo\appdata\local\programs\python\python312\lib\site-packages (from Django) (0.5.1)
 Django) (2024.1)

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip
PS C:\Users\Lenovo\Desktop\Django\DJANGO-Class> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\lenovo\appdata\local\programs\python\python312\lib\site-packages (24.0)
Collecting pip
  Downloading pip-24.2-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-24.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 1.3 MB/s eta 0:00:00
Installing collected packages: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-24.2
PS C:\Users\Lenovo\Desktop\Django\DJANGO-Class> django-admin startproject Myproject
CommandError: 'C:\Users\Lenovo\Desktop\Django\DJANGO-Class\Myproject' already exists
PS C:\Users\Lenovo\Desktop\Django\DJANGO-Class>Django-admin --version
5.1
PS C:\Users\Lenovo\Desktop\Django> cd Myproject
PS C:\Users\Lenovo\Desktop\Django\DJANGo-Class\Myproject> django-admin startapp Myapp
CommandError: 'C:\Users\Lenovo\Desktop\Django\DJANGo-Class\Myproject\Myapp' already exists
PS C:\Users\Lenovo\Desktop\Django\DJANGo-Class\Myproject>  

"""