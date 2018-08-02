# Interview transcript Splitter

Split transcript text and associate it with the correct speaker


## Processing flow

**dl\_sample\_video.sh**

Downloads samples videos to **samples** folder

**converters\\video2images.py**

Samples video every second to image files and stores them in **frames** folder

**converters\\mass_img_convert.py**

Converts all image formats in a folder

**converters\\detect_face.py**

Detects all faces within the **frames** folder and stores them in **faces** folder

**converters\\cluster_faces.sh**

Clusters all faces in **faces** folder based on similarity of facial features based on **face_clustering.py**. The faces are clustered and stored in **face_clusters** folder

**converters\\cluster_pct.py**

Calculate percentage time a face cluster has occupied in a video based on frame count in **frames** folder