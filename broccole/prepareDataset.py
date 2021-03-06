import argparse
import os

from broccole.CocoDataset import CocoDataset
from broccole.CocoDatasetBuilder import CocoDatasetBuilder
from broccole.logUtils import init_logging

def parse_args():
    parser = argparse.ArgumentParser(description='train U-Net')
    parser.add_argument('--datasetDir', help='path to directory with dataset', type=str)    
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    datasetDir = args.datasetDir
    # datasetDir = '../data' # for debug assign your datafolder

    init_logging('prepare.log')

    humanDataset = CocoDatasetBuilder(os.path.join(datasetDir, 'train2017'), os.path.join(datasetDir, 'annotations/instances_train2017.json')).addClasses([1]).build()
    CocoDataset.save(humanDataset, os.path.join(datasetDir, 'human')) #, startIndex=(61600 + 2515))

    nonHumanDataset = CocoDatasetBuilder(os.path.join(datasetDir, 'train2017'), os.path.join(datasetDir, 'annotations/instances_train2017.json')).selectAll().filterNonClasses([1]).build(shuffle=True)
    CocoDataset.save(nonHumanDataset, os.path.join(datasetDir, 'nonHuman')) #, startIndex=28288)

    valHumanDataset = CocoDatasetBuilder(os.path.join(datasetDir, 'val2017'), os.path.join(datasetDir, 'annotations/instances_val2017.json')).addClasses([1]).build()
    CocoDataset.save(valHumanDataset, os.path.join(datasetDir, 'valHuman'))

    valNonHumanDataset = CocoDatasetBuilder(os.path.join(datasetDir, 'val2017'), os.path.join(datasetDir, 'annotations/instances_val2017.json')).selectAll().filterNonClasses([1]).build(shuffle=True)
    CocoDataset.save(valNonHumanDataset, os.path.join(datasetDir, 'valNonHuman'))

if __name__ == '__main__':
    main()
