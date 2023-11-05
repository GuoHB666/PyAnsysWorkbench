from os import (path,mkdir)

def foderCreate(folder_path):
    if not path.exists(folder_path): #判断文件夹是否存在
        mkdir(folder_path) #创建文件夹


def filesInit(wbpj_name="py_ansys.wbpj"):
    wbpj_folder = '.\Software'
    geometry_folder = '.\Geometry'
    foderCreate(geometry_folder)
    foderCreate(wbpj_folder)
    wbpj_path = path.abspath(wbpj_folder + '\\' + wbpj_name)
    return wbpj_path