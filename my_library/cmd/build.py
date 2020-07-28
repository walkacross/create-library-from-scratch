#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def main():
    print("hello build")
    os.system("echo downloading ......")
    
    deault_data_path = os.path.expanduser('~/.mytest/bundle/')
    if not os.path.exists(deault_data_path):
        os.makedirs(deault_data_path)
    output = os.system("cp -r /simons/bundle/. {}".format(deault_data_path))
    if output == 0:
        os.system("echo download successfully...")
    else:
        os.system("echo download failed...")
        
if __name__ == "__main__":
    main()