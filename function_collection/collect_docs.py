import glob
import ntpath
import os


def parse_files(filelist: list[str]) -> dict[str: str]:
    docs_list = {}
    for f in filelist:
        docs = ''
        with open(f) as of:
            line_data = of.readlines()
            problem_name = None
            reading = False
            try:
                if line_data[0].startswith('"""'):
                    for l in line_data:
                        if problem_name and reading and l.startswith('"""'):
                            reading = False
                            break
                        if reading:
                            docs += l
                        if l.startswith('"""'):
                            problem_name = ntpath.basename(f) + ': ' + l.strip('""" ')
                            reading = True
                else:
                    continue
            except IndexError:
                continue
        if problem_name:
            docs_list.update( {problem_name: docs} )
    return docs_list


if __name__ == '__main__':
    file_path = os.path.realpath(__file__)
    project_path = os.getcwd()

    filelist = glob.glob(f'{project_path}/*.py')

    res = parse_files(filelist)

    output_file = 'docs.txt'
    with open(output_file, 'w') as out:
        out.write('')  # we create an empty file (or clean it, if it already exists)

    for header_,text_ in res.items():
        with open(output_file, 'a') as out:
            out.write('====================================================\n')
            out.write(header_ + '\n')
            out.write(text_)
            out.write('\n')