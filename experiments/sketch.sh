cd ..

# python run_painterly_render.py \
#   -c diffsketcher-sketch.yaml \
#   -eval_step 10 -save_step 10 \
#   -update "token_ind=2 num_paths=96 num_iter=800" \
#   -pt "a sketch image of human face" \
#   -respath ./workdir/sketch_w_real_image \
#   -d 8019 \
#   --download \
#   --img_path ../sketch2head/data/real_pic/00000/00000-7.png

  python run_painterly_render.py \
  -c diffsketcher-sketch.yaml \
  -eval_step 10 -save_step 10 \
  -update "token_ind=2 num_paths=96 num_iter=300" \
  -pt "a sketch image of human face" \
  -respath ./workdir/dataset_test \
  -d 8019 \
  --download \
  --img_path ../sketch2head/data/sketch/00000/00000-7.png\
  --clipasso_loss False\
  --dataset True