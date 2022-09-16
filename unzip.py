import os
import zipfile
import traceback

def Unzip_fun(path):
    if os.path(path):
        # 파일 목록 획득
        file_list = os.listdir(path)
        file_list_zip = [file for file in file_list if file.endswith(".zip")]

        # 각 파일 압축해제 루틴
        for i in range(len(file_list_zip)):
            full_path = path + file_list_zip[i]
            # 압축 파일 오픈
            zip_file = open(full_path, 'rb')
            Target_zip = zipfile.ZipFile(zip_file)
            #패스워드 지정
            Target_zip.setpassword('지정된 비밀번호')
            for k in Target_zip.namelist():
                try:
                    Target_zip.extract(k, path+"\\"+file_list_zip[i])
                except Exception:
                    traceback.print_exc()
            zip_file.close()
    else:
        print("존재하지 않는 경로")
