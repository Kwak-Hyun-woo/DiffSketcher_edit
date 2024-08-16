cd ..

  python run_painterly_render.py \
  -c diffsketcher-sketch.yaml \
  -eval_step 10 -save_step 10 \
  -update "token_ind=2 num_paths=128 num_iter=300" \
  -pt "a sketch image" \
  -npt "colored image"\
  -d 8019 \
  --download \
  --clipasso_loss False\
  --dataset True \
  --start_idx 45000 \
  --end_idx 53000
