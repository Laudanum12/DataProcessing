import requests
from ftplib import FTP
import urllib.request
from zipfile import ZipFile
import  os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error' + directory)
#urllib.request.urlretrieve('ftp://free:free@ftp.zakupki.gov.ru/fcs_regions/Adygeja_Resp/addinfo/addinfo_Adygeja_Resp_2016010100_2016020100_001.xml.zip',
                             # 'my_zip.zip')

#user_agent_url = 'ftp://free:free@ftp.zakupki.gov.ru/fcs_regions/Adygeja_Resp/addinfo/addinfo_Adygeja_Resp_2016010100_2016020100_001.xml.zip'
#print(requests.get(user_agent_url))


#urllib.request.urlretrieve('ftp://free:free@ftp.zakupki.gov.ru/fcs_regions/Adygeja_Resp/plangraphs/', 'all_data.txt')

with open('all_data.txt', 'r') as file:
    names = list()
    lines = file.readlines()
    for line in lines:
        names.append((line.split(' ')[-1])[:-1])
    name_of_folder = (names[0].split('_'))[0]
    path_of_project = os.path.dirname(os.path.abspath(__file__))
    path = path_of_project + '\\' + str(name_of_folder)
    createFolder(path)

    for s, d, f in os.walk(path_of_project):
        for file in f:
            if '.zip' in file:
                createFolder(path_of_project + '\\' + str(name_of_folder) +'\\' + file)
                with ZipFile(file, 'r') as zip_file:
                    zip_file.extractall(path=path_of_project + '\\' + str(name_of_folder) + '\\' + file)

    # Все скачивает все файлы с названиями
    # for name in names:
    #     urllib.request.urlretrieve('ftp://free:free@ftp.zakupki.gov.ru/fcs_regions/Adygeja_Resp/plangraphs/'+ str(name),
    #                                name)



