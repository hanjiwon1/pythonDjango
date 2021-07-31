#/usr/bin/env python3

from local_lib import path

def main():
	dirc = path.Path("new_dir")
	try:
		dirc.mkdir()
	except:
		print("The directory name already exists.")
	fil_e = path.Path(f"{dirc}/new_file")
	fil_e.touch()
	fil_e.write_text("Hello")
	print(fil_e.read_text())

if __name__ == '__main__':
	main()