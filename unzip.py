import pyzipper

def _unzip():
    file_list = os.listdir(압축해제 대상 파일이 존재하는 폴더)
    try:
        print("[+] 압축해제 시작")
        for ef in file_list:
            unzip.unzip_fun(f"압축해제 대상 파일이 존재하는 폴더\\{ef}")
        print("[+] 압축해제 완료!")
    except:
        print("[+] 압축해제 대상 파일이 존재하지 않습니다.")
        
      
if __name__=="__main__":
    _unzip()
