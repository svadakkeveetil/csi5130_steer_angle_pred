Change `data_path` value in `config.py` to point to this data directory.

# Pre-processing

The raw images are of size 640 x 480. In our final model, we resized the images to 256 x 192, converted from RGB color format to grayscale, 
computed lag 1 differences between frames and used 2 consecutive differenced images.
For example, at time t we used [x_{t} - x_{t-1}, x_{t-1} - x_{t-2}] as input where x corresponds to the grayscale image. 
No future frames were used to predict the current steering angle.

To pre-process phase 2 training data, run:

```
python preprocess_train_data.py
```

To pre-process phase 2 test data, run:

```
python preprocess_test_data.py
```

These pre-processing scripts convert image sets to numpy arrays.

# Model
To train different models, run:

```
python train.py
```

You can change these parameters in the `config.py` file:

* `--data` - alias for pre-processed data. There are multiple ways to pre-process the data (how many consecutive frames to use, image size, etc).
This parameter value gives us information what data set to use.
* `--num_channels` - number of channels the data has. For example, if you use 4 consecutive frames, then `num_channels` must be 4.
* `--img_height` - image height in pixels, default is 192.
* `--img_width` - image width in pixels, default is 256.
* `--model` - model definition file, see `models.py` for different models.
* `--test_part` - which part of the data to use as validation set.
* `--batch_size` - minibatch size, default is 32.
* `--num_epoch` - number epochs to train, default is 10.
* `--data_path` - folder path to pre-processed numpy arrays.

To predict steering angles from test data, run:

```
python predict.py
```


# Inspecting the model

* Automatic report

![](assets/report.png)

To get an automatic report with predicted steering angle distributions and error visualizations, run the following R script:

```
Rscript render_reports.R
```
You might want to change variables `submission_filename, img_path, output_filename` in the `render_reports.R` file.

* Visualizing predicted steering angles

To visualize model predictions on test data, run:

```
python visualize.py
```

White circle shows the true angle, black circle shows the predicted angle.
You might need to change the variable `VisualizeConfig` in `config.py` to point to the location of phase 2 images.

These visualizations can help us understand the weaknesses of the model.
For example, human steering movements are smoother on straight road while the model zig-zags.
