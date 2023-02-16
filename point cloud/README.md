
## Point Cloud Plane Segmentation on Construction Site 

## Description

This task is an implementation of doing segmentation on photogrammetric point cloud of one floor of a construction site

## Requirements

Necessary packages to install

    Python=3.8.10
    numpy==1.21.6
    laspy==2.0.0
    open3d==0.13.0
    matplotlib==3.6.3


## Usage

 Open "point cloud plane segmentation.ipnyb"

 It use laspy to read point cloud data and visualize the data using open3d. Convert the .laz to an Open3D point cloud object and save Open3D point cloud object as a .ply file

 Load the exported json and draw the extracted boundaries on the respective image.

 Segment plane using RANSAC and extract inliers and outliers.

 DBSCAN used to group points with similiar property and identify planes within a point cloud.


## Approach followed

 RANSAC and DBSCAN for segmenting a point cloud to identify planes. RANSAC is a robust algorithm for estimating model parameters, and can be best used to identify planes in a point cloud.

 Once a plane model is estimated using RANSAC, DBSCAN can be used to cluster points on the plane and extract it from the rest of the point cloud.

 DBSCAN is a density-based clustering algorithm that can group nearby points into clusters, which can be useful for identifying planar surfaces in a point cloud. Together, RANSAC and DBSCAN can be used to segment a point cloud to identify planes.


## Conclusion

 The RANSAC algorithm is a powerful method for segmenting planes in point clouds, and is commonly used in combination with other techniques like DBSCAN clustering to accurately identify planes and remove outliers.

 However, there are many alternative approaches such as Region Growing, Convex Hull, Normal Estimation. The choice of approach will depend on the specific application and the characteristics of the point cloud data, and should be chosen carefully to achieve the best possible segmentation performance.




