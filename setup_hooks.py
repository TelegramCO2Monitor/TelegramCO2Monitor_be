import shutil
import os

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def copy_hooks():
  src_dir = "hooks"
  dst_dir = ".git/hooks"

  if not os.path.exists(dst_dir):
    print(f"{RED}[ERROR] The directory {dst_dir} not exitsts.{RESET}")
    return

  for filename in os.listdir(src_dir):
    src_file = os.path.join(src_dir, filename)
    dst_file = os.path.join(dst_dir, filename)

    if (os.path.isfile(src_file)):
      shutil.copy(src_file, dst_file)
      print(f"{GREEN}[SUCCESS] {src_file} copied successfully{RESET}")

  print(f"{GREEN}[SUCCESS] All hooks copied successfully{RESET}")

if __name__ == "__main__":
  copy_hooks()