# IJCAI2016

This repository is for the replication of our published paper [Protein Secondary Structure Prediction Using Cascaded Convolutional and Recurrent Neural Networks](https://www.ijcai.org/Proceedings/16/Papers/364.pdf) on IJCAI2016. Our whole pipeline is listed as follows.
<p align="center"><img width="100%" src="image/pipeline.png" /></p>

# Download data

For cb513+profile_split1.npy.gz, cullpdb+profile_6133_filtered.npy.gz, please download from this [website](http://www.princeton.edu/~jzthree/datasets/ICML2014/).    
For CASP10 and CASP11, please download from this [website](https://goo.gl/tjJttR).     
Download data and put them in ./data folder.

# Project Settings

1. Install the requirements (you can use pip or [Anaconda](https://www.continuum.io/downloads)):

    ```
    conda install pip h5py cython numpy scipy
    conda install -c conda-forge theano 
    conda install -c toli lasagne
    ```

2. You can do training/validation/test through this IPython notebook ./Train_validation_test_release.ipynb.    
PS: The demo code use splited cullpdb+profile_6133_filtered for training/validation and then test on CB513 and CASP dataset. You can use whole cullpdb+profile_6133_filtered for training to obtain better performace.

## Progress
- [x] README for training 
- [x] README for project settings
- [x] Dynamic training codes
- [x] Dynamic evaluation codes
- [ ] Multi-GPU support

## Acknowledgement

We thank [Jian Zhou](http://www.princeton.edu/~jzthree/) and [Sheng Wang](http://ttic.uchicago.edu/~wangsheng/) for CASP dataset generation.

## Reference
If you find this code useful for your research, please cite

```
@inproceedings{li2016protein,
  title={Protein secondary structure prediction using cascaded convolutional and recurrent neural networks},
  author={Li, Zhen and Yu, Yizhou},
  booktitle={Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence},
  pages={2560--2567},
  year={2016},
  organization={AAAI Press}
}
```