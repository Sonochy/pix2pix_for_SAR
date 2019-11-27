python tools/dockrun.py python pix2pix.py --mode train --output_dir Model_hh_batch_1_scale_1142_crop_1024 --max_epochs 2000 --scale_size 1142 --batch_size 1 --crop_size 1024 --input_dir Train_images/train --which_direction BtoA

python tools/dockrun.py python pix2pix.py --mode train --output_dir Model_hh_batch_1_scale_1142_crop_512 --max_epochs 1000 --scale_size 1142 --batch_size 1 --crop_size 512 --input_dir Train_images/train --which_direction BtoA

python tools/dockrun.py python pix2pix.py --mode train --output_dir Model_hh_batch_2_scale_1142_crop_1024 --max_epochs 1000 --scale_size 1142 --batch_size 2 --crop_size 1024 --input_dir Train_images/train --which_direction BtoA

python tools/dockrun.py python pix2pix.py --mode train --output_dir Model_hh_batch_2_scale_1142_crop_512 --max_epochs 1000 --scale_size 1142 --batch_size 2 --crop_size 512 --input_dir Train_images/train --which_direction BtoA




