import sys
import os
from PIL import Image
from PIL import GifImagePlugin
import time
import shutil

gif_name = sys.argv[1]
hashed_dir_name = hash(gif_name)
storage_dir = os.path.join(os.path.expanduser("~"), ".geh")

for folder in os.listdir(storage_dir):
  if not folder == "gifs":
    shutil.rmtree(os.path.join(storage_dir, folder))

if not os.path.exists(storage_dir):
  os.mkdir(storage_dir)

gif_dir = os.path.join(storage_dir, "gifs")
if not os.path.exists(gif_dir):
  os.mkdir(gif_dir)

if not gif_name in os.listdir(gif_dir):
  print(f"gif '{gif_name}' not located in {gif_dir}")
  move_gif = input(f"would you like to move '{gif_name}' to {gif_dir}? (y, n): ")

  if move_gif in ["y", "Y", "yes", "YES"]:
    os.system(f"mv {gif_name} {gif_dir}")
  else:
    exit()

image_object = Image.open(os.path.join(gif_dir, gif_name))

current_bg_dir = os.path.join(storage_dir, str(hashed_dir_name))
os.mkdir(os.path.join(storage_dir, str(hashed_dir_name)))

for frame in range(image_object.n_frames):
  image_object.seek(frame)
  image_object.save(os.path.join(current_bg_dir, f"{frame}.png"))

def partition(arr, low, high):
  i = low - 1
  arr_high = int(arr[high].split(".")[0])
  pivot = arr_high

  for j in range(low, high):
    if int(arr[j].split(".")[0]) <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1

def quick_sort(arr, low, high):
  if len(arr) == 1:
    return arr
  if low < high:
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi+1, high)

gif_dir = os.listdir(current_bg_dir)
quick_sort(gif_dir, 0, len(gif_dir) - 1)

while True:
  for picture in gif_dir:
    os.system(f"feh --bg-scale {os.path.join(current_bg_dir, picture)}")