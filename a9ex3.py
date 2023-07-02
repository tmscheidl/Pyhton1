"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 3
"""

import subprocess

arg_list = []
encode_list = ['-e']
par_pname = input("Enter program or press ENTER to exit: ")

if par_pname:
    arg_list.append(par_pname)
    par_arg = input("Enter argument or press ENTER to skip: ")

    while par_arg:
        arg_list.append(par_arg)
        par_arg = input("Enter argument or press ENTER to skip: ")

    if not par_arg:
        par_encod = input("Enter encoding or press ENTER to skip: ")
        encode_list.append(par_encod)

        if arg_list and par_encod:
            print(f"Running program '{par_pname}' with arguments '{arg_list}' and encoding '{par_encod}'")
        elif par_encod and not arg_list:
            print(f"Running program '{par_pname}' without any arguments and encoding '{par_encod}'")
        elif arg_list and not par_encod:
            print(f"Running program '{par_pname}' with arguments '{arg_list}' and no encoding")
        else:
            print(f"Running program '{par_pname}' without any arguments and no encoding")

        collected_arg = arg_list + encode_list

        try:
            p = subprocess.Popen(collected_arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outs, errs = p.communicate(timeout=5)

            if errs:
                print(f"The program finished with exit code {p.returncode}")
                print(f"The programproduced the following error output:\n {errs}")
            if outs:
                print(f"The program finished with exit code {p.returncode}")
                print(f"The program produced the following standard output:\n {outs}")

        except LookupError as lu_err:
            print(lu_err)
            print(f"The specified encoding '{par_encod}' could not be found\n")

        except FileNotFoundError as fnf_err:
            print(fnf_err)
            print(f"The specified program '{par_pname}' could not be found")

else:
    exit()



