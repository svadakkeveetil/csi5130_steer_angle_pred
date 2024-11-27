class DataConfig(object):
    data_path = "/home/dhavan/AI_Project/Data/"
    data_name = "hsv_gray_diff_ch4"
    img_height = 192
    img_width = 256
    num_channels = 4
    
class TrainConfig(DataConfig):
    model_name = "comma_prelu"
    batch_size = 4
    epochs = 10
    val_part = 6
    X_train_mean_path = "/home/dhavan/AI_Project/Data/X_train_gray_diff2_mean.npy"
    
class TestConfig(TrainConfig):
    model_path = "/home/dhavan/AI_Project/Data/final_model.hdf5"
    angle_train_mean = -0.004179079

class VisualizeConfig(object):
    pred_path = "submissions/final_model.csv"
    true_path = "/home/svadakkeveetil/ros/src/csi5130_steer_angle_pred/rambo/data/CH2_final_evaluation.csv"
    img_path = "phase2_test/center/*.jpg"
