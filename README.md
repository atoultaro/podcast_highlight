# Podcast highlight extraction for Sounder.fm

## Installation
The repo was developed on MacBook M1 chip laptop. Thus, Python 3.8 and most packages, as well as the virtual 
environment, are managed using Conda. The list of packages is shown in the file requirements.txt.

## Speaker segmentation
Using SpeechBrain's speaker embeddings from the HuggingFace repo of "spkrec-ecapa-voxceleb".
See https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb

## AudioSet 
- The sound oncology is shown in the following link:
https://research.google.com/audioset/ontology/index.html
- Vggish and YAMNet
Download those two models for AudioSet from a directory within TensorFlow repo (Trick: DownGit)
https://github.com/tensorflow/models/tree/master/research/audioset

