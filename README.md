# XPE-Memory Framework
Official repository for the research paper: **"XPE-Memory: An Explainable, Time-Aware AI Architecture for Zero-Day Memory Malware Detection"**.

## Overview
XPE-Memory is a hierarchical, cloud-scalable AI pipeline designed for the detection of zero-day memory-resident malware. This framework introduces:
1. **Temporal Behavioral Synthesis:** EMA-based feature extraction for detecting stealthy injections.
2. **SHAP-RFE:** A novel feature selection algorithm for forensic-grade dimensionality reduction.
3. **Hierarchical SMOTE:** Balancing architecture for multi-class malware classification.

## Dataset (XPE-Memory-DS)
The dataset (`XPE-Memory-DS.csv`) is a high-fidelity benchmark generated from the CIC-MalMem-2022 dataset using our AI pipeline.
- **Instances:** 14,036
- **Features:** 7 SHAP-optimized temporal/static features.
- **Classes:** 4 (Benign, Trojan, Spyware, Ransomware) - Perfectly balanced via SMOTE.

## How to Run
1. Clone the repository: `git clone https://github.com/AhmedLotfy9513/XPE-Memory-Framework.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the generator: `python src/pipeline_generator.py`

## Citation
10.5281/zenodo.21457507

@article{lotfi2026xpe,
  title={XPE-Memory: An Explainable, Time-Aware AI Architecture for Zero-Day Memory Malware Detection},
  author={Ahmed Lotfi, Ahmed Maher, Mohamed Abdelmonem Elshafei},
  journal={Military Technical College Research},
  year={2026}
}
