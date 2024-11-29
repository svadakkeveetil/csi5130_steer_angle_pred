class DataConfig(object):
    data_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/model_files/"
    data_name = "hsv_gray_diff_ch4"
    img_height = 192
    img_width = 256
    num_channels = 4
    
class TrainConfig(DataConfig):
    model_name = "comma_6"
    batch_size = 8
    epochs = 10
    val_part = 4
    X_train_mean_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/data/X_train_gray_diff2_mean.npy"
class TestConfig(TrainConfig):
    model_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/checkpoints/final_model.hdf5"
    angle_train_mean = -0.004179079
    image_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/"

class VisualizeConfig(object):
    pred_path = "submissions/final.csv"
    true_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/data/CH2_final_evaluation.csv"
    img_path = "phase2_test/center/*.jpg"
