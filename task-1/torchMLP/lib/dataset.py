import numpy as np

import os

import torch
from torch.utils.data import Dataset


class MRIDataset(Dataset):
    def __init__(self, split='train'):
        super().__init__()
        assert split in ['train', 'valid'], f'Split parameters "{split}" must be either "train" or "valid".'
        # Read either train or validation data from disk based on split parameter using np.load.
        # Data is located in the folder "data".
        # Hint: you can use os.path.join to obtain a path in a subfolder.
        # Save samples and annotations to class members self.samples and self.annotations respectively.
        # Samples should be an Nx2 numpy array. Annotations should be Nx1.

        #Should we use other path?
        data = np.load(os.path.join("data", "X_train.csv")) #data is a dictionnary with two entries, one for each file 
        print(data)
        self.samples = data["samples"]
        self.annotations = data["annotations"]
            
    def __len__(self):
        # Returns the number of samples in the dataset.
        return self.samples.shape[0]
    
    def __getitem__(self, idx):
        # Returns the sample and annotation with index idx.
        sample = self.samples[idx]
        annotation = self.annotations[idx]
        
        # Convert to tensor.
        return {
            'input': torch.from_numpy(sample).float(),
            'annotation': torch.from_numpy(annotation[np.newaxis]).float()
        }