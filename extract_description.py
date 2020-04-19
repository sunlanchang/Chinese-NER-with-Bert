import json
import glob


def extract_Cnnvd_LK():
    file_paths = glob.glob('data/tmp_Cnnvd_LK/*.json')
    file_paths.sort()
    # print(file_paths)
    # f_writer = open('data/tmp_word_Cnnvd_LK.txt', 'w')
    f_writer = open('data/test.txt', 'w')
    for file_path in file_paths:
        with open(file_path) as f:
            data = json.load(f)
            info = data['漏洞简介']
            # 不同文件数据以空行分隔，添加占位符O
            info = ' O\n'.join(info)+' O\n\n'
            f_writer.write(info)
    f_writer.close()


def extract_CNVD():
    file_paths = glob.glob('data/tmp_CNVD-Json_LK/*.json')
    file_paths.sort()
    # f_writer = open('data/tmp_word_Cnnvd_LK.txt', 'w')
    f_writer = open('data/test.txt', 'w')
    for file_path in file_paths:
        with open(file_path) as f:
            data = json.load(f)
            info = data['description']
            # 不同文件数据以空行分隔，添加占位符O
            info = ' O\n'.join(info)+' O\n\n'
            f_writer.write(info)
    f_writer.close()


if __name__ == "__main__":
    extract_Cnnvd_LK()
