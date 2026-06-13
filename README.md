# Compressing-Convolutional-Neural-Networks-for-Offline-Educational-Deploymen
An Empirical Study of Pruning and INT8 Quantization
Access to artificial intelligence tools in rural and
low-resource educational settings is fundamentally constrained
by hardware: most schools have, at best, low-end smartphones or
shared desktop computers, and rarely have internet connectivity
reliable enough for cloud-based inference. This paper presents
a fully reproducible empirical study of two standard model-
compression techniques—magnitude-based weight pruning and
post-training 8-bit (INT8) quantization—applied to a compact
convolutional neural network (CNN) trained for handwritten
digit recognition on the MNIST dataset. Using a controlled
experimental design in which an independently cloned copy of a
trained baseline model is pruned and fine-tuned, we measure the
accuracy, model size, and compression ratio of four deployment
configurations. The baseline CNN achieves 98.78% test accuracy
on the full 10,000-image test set with a 224,892-byte TensorFlow
Lite footprint. INT8 quantization reduces this to 61,800 bytes
(a 3.64x reduction) with a negligible 0.09 percentage-point shift
in accuracy. Iterative pruning to 70% sparsity with fine-tuning
matches the baseline almost perfectly at 98.77%, while leaving
the FP32 file size unchanged—a result we explain in terms of
the dense storage format used by standard TensorFlow Lite
flatbuffers. Combining pruning with quantization achieves the
same 3.64x compression as quantization alone, restoring accuracy
to exactly 98.78%. These results provide a transparent, low-
cost, and entirely reproducible reference point for deploying
handwriting-recognition tools on inexpensive edge hardware
without requiring GPUs or cloud services.
