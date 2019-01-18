import os

DIR = os.path.join(os.getenv("HOME"), "Downloads", "opgave0")


def get_input(num):
    with open(os.path.join(DIR, "nio0-{}.txt".format(num))) as f_p:
        l = f_p.readlines()
        return l


def check_output(p_output, num, ex):
    with open(os.path.join(DIR, "nio0-{}{}.uit".format(num, ex))) as f_p:
        c = f_p.read()
        return p_output == c
