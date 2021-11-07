# import library
from tensorflow import keras
import os

# save model into h5 file in specific location
def save_model(model, model_save_dir, model_name):
    model.save(os.path.join(model_save_dir,model_name))

# load the model from a specific location
def load_model(model_save_dir, model_name):
    reconstructed_model = keras.models.load_model(os.path.join(model_save_dir,model_name))
    return reconstructed_model



