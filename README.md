# Podcast highlight extraction for Sounder.fm

## Installation
The repo was developed on MacBook M1 chip laptop. Thus, Python 3.8 and most packages, as well as the virtual 
environment, are managed using Conda. The list of packages is shown in the file requirements.txt.

### Problem
sentencepiece might not be able to be import on Apple M1

arch -arm64 brew install cmake
pip install --no-cache-dir sentencepiece


## Data
Sound data are stored under the directory ./sound

## Step 1: Speaker segmentation (find_speaker_segment.py)
Using SpeechBrain's speaker embeddings from the HuggingFace repo of "spkrec-ecapa-voxceleb".
See https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb

## Step 2: Audio tagging by AudioSet (assign_audioset_labels.py)
- The sound oncology is shown in the following link:
https://research.google.com/audioset/ontology/index.html
- Vggish and YAMNet
Download those two models for AudioSet from a directory within TensorFlow repo (Trick: DownGit)
https://github.com/tensorflow/models/tree/master/research/audioset

## Step 3: Find highlight through the combination of sentence embedding (BERT embeddings) and music presence
- Huggingface's sentence transformer
https://huggingface.co/sentence-transformers/sentence-t5-large
- Final score  = Alpha * Music Score (0 or 1) + (1 - Alpha) * Sentence similarity

