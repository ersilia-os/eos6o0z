import random
import os
import numpy as np
import torch
import pandas as pd
from rdkit import RDLogger
from pathlib import Path
import tempfile

from .grover.util.parsing import get_newest_train_args
from .task.predict import make_predictions
from .grover.data.torchvocab import MolVocab
import grover.scripts.save_features as sf

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def setup(seed):
    # frozen random seed
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True

def smiles_to_dataframe(txt_file_path):

    
    df = pd.read_csv(txt_file_path, header=None,  names=['smiles'])
    
    dummy_labels = pd.Series(np.zeros(df.shape[0]))

    names =    ['u0_atom']
    
    for n in names:
        df[n] = dummy_labels.values

    input_csv_path = txt_file_path.split(".")[0] + ".csv"
    df.to_csv(input_csv_path, index=False)
    
    return input_csv_path

    
tmp_folder = tempfile.mktemp()
features_path = os.path.join(tmp_folder, "features.npz")

def grover_predict(input_txt_path, output_path):
    # setup random seed
    setup(seed=42)
    # Avoid the pylint warning.
    a = MolVocab
    # supress rdkit logger
    lg = RDLogger.logger()
    lg.setLevel(RDLogger.CRITICAL)

    # Initialize MolVocab
    mol_vocab = MolVocab
    csv_path = smiles_to_dataframe(input_txt_path)

    s = os.path.dirname(os.path.abspath(__file__))
    p = Path(s)
    model_path = str(p.parent.parent.parent.absolute()) + '/checkpoints'
    trained_path= model_path+'/finetune/qm7'

    args = Namespace(batch_size=32, checkpoint_dir= trained_path, checkpoint_path=None, checkpoint_paths=[trained_path + '/fold_0/model_0/model.pt', trained_path + '/fold_2/model_0/model.pt',trained_path + '/fold_1/model_0/model.pt'], cuda=False, data_path=csv_path, ensemble_size=3, features_generator=None, features_path=[features_path], fingerprint=False, gpu=0, no_cache=True, no_features_scaling=True, output_path=output_path, parser_name='predict')


    sf.save_features_main(csv_path,features_path)

    train_args = get_newest_train_args()
    avg_preds, test_smiles = make_predictions(args, train_args)
    os.remove(csv_path)
    return avg_preds, test_smiles
