import os
import whisper
import json
ext=[".mp3",".mp4","wav",".mkv",".m4v","mpeg",".m4a",".webm"]
def search(dir_name,ext):
    files_list=[]
    for root,directory,files in os.walk(dir_name):
        for file in files:
            for extension in ext:
                if extension in file:
                    files_list.append(os.path.join(root,file))
    return files_list

def transcribing(files_list,result_dir):
    if not os.path.exists(result_dir):  
        os.makedirs(result_dir) 
    for curr_file in files_list:
        try:
            result=whisper.load_model("small").transcribe(curr_file)
            transcript = result['text']
            result_file=os.path.join(result_dir,os.path.basename(curr_file)+".json")
            with open(result_file,'w',encoding='utf-8') as f:
                json.dump({"file":curr_file,"transcription":transcript},f)
        except Exception as e:
            print(e)
            continue

if __name__=='__main__':
    curr_dir = os.getcwd()
    files_list = search(curr_dir,ext)
    transcribing(files_list,os.path.join(curr_dir,"results"))