import argparse

parser = argparse.ArgumentParser(description = "SVD IMG")

svd_arg = parser.add_argument_group("SVD_IMG")
svd_arg.add_argument("--components",type=int,default=50)
svd_arg.add_argument("--path",type=str,default="./c6c08053-9f02-4e81-81b5-032039e76ddc.jpeg")

def get_config():
    config,unparsed = parser.parse_known_args()
    return config,unparsed