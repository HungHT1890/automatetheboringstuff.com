#    >>> import shutil, os
#    >>> from pathlib import Path
#    >>> p = Path.home()
# ➊ >>> shutil.copy(p / 'spam.txt', p / 'some_folder')
#    'C:\\Users\\Al\\some_folder\\spam.txt'
# ➋ >>> shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
#    WindowsPath('C:/Users/Al/some_folder/eggs2.txt')


import shutil , os
source = r'C:\Users\hungh\OneDrive\Desktop\automatetheboringstuff.com\ORGANIZING FILES\source\demo_source.txt'
destination = r'C:\Users\hungh\OneDrive\Desktop\automatetheboringstuff.com\ORGANIZING FILES\destination'
# trường hợp 1 : file chưa có sẵn chương trình sẽ tiến hành tạo file mới
# trường hợp 1 : file có sẵn chương trình sẽ tiến hành copy file và ghi đè lên file cũ
# hàm copy sẽ trả về đường dẫn chứa file mới

path_new_file = shutil.copy(source,destination)
print(path_new_file)