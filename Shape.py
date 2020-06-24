#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

class shape:

    def draw(self):
        pass


raw_data = args.split()
input_file = raw_data[0]
file_type = raw_data[1]
try:
    os.path.isdir(input_file)
    os.path.isfile(input_file)
    work_dir = os.path.dirname(input_file)
    file = input_file[len(work_dir) + 1:]

except FileNotFoundError:
    print("wrong path, try again")

else:

    if file_type == 'svg':
        command = "pyreverse {0} -o svg -p diagram".format(file)
        print("input_dir:{0} input_file:{1}".format(work_dir, file))
        print("command:" + command)
        subprocess.run(command, cwd=work_dir, shell=True)
    elif file_type == 'fig':
        command = "pyreverse {0} -o fig -p diagram".format(file)
        print("input_dir:{0} input_file:{1}".format(work_dir, file))
        print("command:" + command)
        subprocess.run(command, cwd=work_dir, shell=True)
    elif file_type == 'dot':
        command = "pyreverse {0} -o dot -p diagram".format(file)
        print("input_dir:{0} input_file:{1}".format(work_dir, file))
        print("command:" + command)
        subprocess.run(command, cwd=work_dir, shell=True)
    else:
        print(" You only have 3 options which are svg, dot and fig in the file types")