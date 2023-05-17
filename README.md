# CDSC_AL: A Clustering-based Data Stream Classification framework using Active Learning

Yan, Xuyang and Homaifar, Abdollah and Sarkar, Mrinmoy and Girma, Abenezer and Tunstel, Edward. "A Clustering-based 
framework for Classifying Data Streams." In Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI2021).

## ARM-Stream Base Classifier Server

This is a wrapper that exposes the CDSC-AL functionality through an HTTP server, allowing it to be integrated with 
[ARM-Stream](https://github.com/douglas444/arm-stream-framework) using the [ARM-Stream HTTP](https://github.com/douglas444/arm-stream-framework/tree/main/arm-stream-http) 
module.

### Requirements

* Python 3.x
* [pip](https://pip.pypa.io/en/stable/installation/)

### How to install

Run the command line bellow from the root of the project:

```
pip install -r requirements.txt
```

### How to start the server

Run the command line bellow from the root of the project:

```
python server.py
```

### How to integrate to ARM-Stream

To integrate it to ARM-Stream, follow [this](https://github.com/douglas444/arm-stream-framework/blob/main/arm-stream-impl/src/main/java/br/ufu/facom/armstream/ref/cdscal/ArmCdscal.java)
reference implementation.

Working experiments integrating ARM-Stream to CDSC-AL are available [here](https://github.com/douglas444/arm-stream-framework/tree/main/arm-stream-exp).

Value for [remoteBaseClassifierUrl](https://github.com/douglas444/arm-stream-framework/blob/c0f81a739c968d32df27fe8a0ca9d0beadebb90b/arm-stream-http/src/main/java/br/ufu/facom/armstream/http/RemoteBaseClassifier.java#L19): 
``http://localhost:5000/start``.

Values for [parameters](https://github.com/douglas444/arm-stream-framework/blob/c0f81a739c968d32df27fe8a0ca9d0beadebb90b/arm-stream-http/src/main/java/br/ufu/facom/armstream/http/RemoteBaseClassifier.java#L22):

- `dataset_filename`: The name of the dataset file (String)
- `buffer_size`: The buffer size to use when processing the dataset (String of an integer)
- `normalize`: Whether to normalize the dataset (String of 0 or 1)
- `module`: The name of the module to run (either `main_final_draft.py` or `main_final_draft4.py`) (String)
